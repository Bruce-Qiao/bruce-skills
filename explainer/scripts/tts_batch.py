#!/usr/bin/env python3
"""Synthesize every narration segment of a video script with one CosyVoice model load.

Run with CosyVoice's own interpreter:
  ~/Coding/CosyVoice/.venv/bin/python tts_batch.py video/script.json video/audio
Voice: <CosyVoice>/my_voice.wav + my_voice.txt (its exact transcript) if both exist,
otherwise CosyVoice's sample voice.
  ... --ref other.wav --ref-text "录音里说的原话"  # use another voice this time
  ... --builtin-voice                            # force CosyVoice's sample voice
  ... --instruct "请用稍慢的语速说。"              # style instruction

script.json: {"scenes": [{"id": "s1", "narration": "...", ...}, ...]}
Writes <out_dir>/<id>.wav for each scene and <out_dir>/durations.json ({id: seconds}).
"""
import argparse
import json
import os
import sys
import time

ROOT = os.environ.get('COSYVOICE_DIR', os.path.expanduser('~/Coding/CosyVoice'))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'third_party', 'Matcha-TTS'))

PREFIX = 'You are a helpful assistant.'
MODEL_DIR = os.path.join(ROOT, 'pretrained_models', 'Fun-CosyVoice3-0.5B')
BUILTIN_REF = os.path.join(ROOT, 'asset', 'zero_shot_prompt.wav')
BUILTIN_REF_TEXT = '希望你以后能够做的比我还好呦。'
# The user's own voice becomes the default when both files exist in the CosyVoice dir
MY_REF = os.path.join(ROOT, 'my_voice.wav')
MY_REF_TEXT_FILE = os.path.join(ROOT, 'my_voice.txt')


def main():
    p = argparse.ArgumentParser(description='Batch TTS for explainer videos (CosyVoice3)')
    p.add_argument('script', help='script.json with a "scenes" list')
    p.add_argument('out_dir', help='directory for <id>.wav and durations.json')
    p.add_argument('--ref', help='reference voice recording (.wav, 3-10 s)')
    p.add_argument('--ref-text', help='exact transcript of the reference recording')
    p.add_argument('--instruct', help='style instruction, e.g. "请用稍慢的语速说。"')
    p.add_argument('--speed', type=float, default=1.0, help='speaking speed, 0.5-2.0')
    p.add_argument('--builtin-voice', action='store_true', help="use CosyVoice's sample voice even if my_voice.wav exists")
    a = p.parse_args()

    with open(a.script, encoding='utf-8') as f:
        scenes = json.load(f)['scenes']
    if a.ref:
        ref, ref_text = os.path.abspath(a.ref), a.ref_text
    elif not a.builtin_voice and os.path.exists(MY_REF) and os.path.exists(MY_REF_TEXT_FILE):
        with open(MY_REF_TEXT_FILE, encoding='utf-8') as f:
            ref, ref_text = MY_REF, f.read().strip()
    else:
        ref, ref_text = BUILTIN_REF, BUILTIN_REF_TEXT
    print(f'Voice: {ref}', flush=True)
    if not os.path.exists(ref):
        p.error(f'reference audio not found: {ref}')
    os.makedirs(a.out_dir, exist_ok=True)

    import torch
    import soundfile as sf
    from cosyvoice.cli.cosyvoice import AutoModel

    t0 = time.time()
    model = AutoModel(model_dir=MODEL_DIR)
    kw = dict(stream=False, speed=a.speed)
    durations = {}
    for s in scenes:
        text = s['narration'].strip()
        if a.instruct:
            gen = model.inference_instruct2(text, f'{PREFIX} {a.instruct}<|endofprompt|>', ref, **kw)
        elif ref_text is not None:
            gen = model.inference_zero_shot(text, f'{PREFIX}<|endofprompt|>{ref_text}', ref, **kw)
        else:
            gen = model.inference_cross_lingual(f'{PREFIX}<|endofprompt|>{text}', ref, **kw)
        wav = torch.cat([j['tts_speech'] for j in gen], dim=1).squeeze(0).cpu().numpy()
        sf.write(os.path.join(a.out_dir, f"{s['id']}.wav"), wav, model.sample_rate)
        durations[s['id']] = round(len(wav) / model.sample_rate, 3)
        print(f"{s['id']}: {durations[s['id']]:.1f} s", flush=True)

    with open(os.path.join(a.out_dir, 'durations.json'), 'w', encoding='utf-8') as f:
        json.dump(durations, f, indent=2)
    print(f'Done: {len(scenes)} segments, {sum(durations.values()):.1f} s of audio, took {time.time() - t0:.1f} s')


if __name__ == '__main__':
    main()
