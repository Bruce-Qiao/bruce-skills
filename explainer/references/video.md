# Video method: 3b1b-style explainer video (Manim + CosyVoice)

## Toolchain (verified 2026-10-12)

| Part | Command / location | Notes |
|---|---|---|
| Animation | `uvx --python 3.12 --from manim manim render ...` | Manim CE, no global install; uv caches it, so only the first run downloads |
| Narration | `~/Coding/CosyVoice/.venv/bin/python <skill>/scripts/tts_batch.py` | Loads the model once (~30 s), RTF ≈ 1.3 |
| Checks | `ffmpeg` / `ffprobe` | Pull frames, check lengths |

**No LaTeX**: `MathTex` / `Tex` will throw errors. Write formulas with `Text` / `MarkupText` and Unicode (`×` `÷` `²` `ⁿ` `√` `≈` `→`). Use `<sup>` in `MarkupText` for superscripts. Don't suggest installing MacTeX (that is a global install).

**Chinese font**: `Text(..., font="PingFang SC")`. Verified to render correctly.

## Workflow

### 1. Script `video/script.json`

```json
{
  "title": "复利",
  "scenes": [
    {"id": "s1", "narration": "……口语旁白……", "visual": "画面描述：出现什么、怎么动"},
    {"id": "s2", "narration": "……", "visual": "……"}
  ]
}
```

- 4–8 scenes, 1–3 minutes total. CosyVoice reads Chinese at about **4 characters/second**, so each scene's narration is 40–120 characters (10–30 s).
- Write narration as **spoken** language: short sentences, nothing written-only. Read formulas out in words ("本金乘以一加利率的n次方"). Don't put symbols in narration.
- Each scene has **one** visual idea. In 3b1b order: give intuition first, then the formula, then a counterexample or boundary.
- When the STE text exists, build the narration from it, rewritten as spoken language. When the diagram exists, use its structure as the storyboard.

### 2. Synthesize audio

```bash
~/Coding/CosyVoice/.venv/bin/python ~/.claude/skills/explainer/scripts/tts_batch.py \
  "$OUT/video/script.json" "$OUT/video/audio"
# Voice cloning: add --ref my.wav --ref-text "原话"; style: --instruct "请用稍慢的语速说。"
```

This produces `audio/s1.wav ...` and `audio/durations.json`. Run it in the background (6 scenes ≈ 3–4 minutes) and write `scene.py` meanwhile.

### 3. Write `video/scene.py`: audio-sync template

```python
from manim import *
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
DUR = json.loads((HERE / "audio" / "durations.json").read_text())
FONT = "PingFang SC"
PAD = 0.4  # breath after each narration segment


class Explainer(Scene):
    def begin(self, sid):
        self.add_sound(str(HERE / "audio" / f"{sid}.wav"))
        self._sid, self._t0 = sid, self.renderer.time

    def end(self):
        used = self.renderer.time - self._t0
        left = DUR[self._sid] + PAD - used
        if left > 0:
            self.wait(left)
        else:
            print(f"WARN {self._sid}: animation {used:.1f}s > audio {DUR[self._sid]:.1f}s")

    def construct(self):
        self.begin("s1")
        # ... self.play(..., run_time=x)
        self.end()

        self.begin("s2")
        # ...
        self.end()
```

- The animation `run_time`s in each section **add up to slightly less** than `DUR[sid]`; `end()` fills the gap. Animations that run too long leave silence; `end()` prints a WARN, so cut `run_time` to fix it.
- Make the timing follow the narration: when the narration reaches a word, the matching object appears. Estimate where in the segment the word falls (character position ÷ total characters × duration).

### 4. Render, check, render the final version

```bash
cd "$OUT/video"
uvx --python 3.12 --from manim manim render -ql --disable_caching --media_dir media scene.py Explainer
# Output: media/videos/scene/480p15/Explainer.mp4
```

Check frames: take the midpoint time of each scene (running total of `DUR + PAD`), pull one frame per scene with `ffmpeg -ss T -i ... -frames:v 1 fN.png`, and look at every frame with Read. Check for:
- Text or shapes going off the edge of the frame (the visible frame is 14.2 × 8 units)
- Objects overlapping or covering each other
- Leftovers from the previous scene that weren't cleared
- Missing or garbled Chinese characters

After fixing, render the final version with `-qh` (1080p60), then copy it to `$OUT/video.mp4`.

Length check: `ffprobe -v error -show_entries stream=codec_type,duration -of csv video.mp4`. The video length should be within 0.5 s of `Σ(DUR + PAD)`. Audio being one PAD shorter than the video is normal (the last segment's breath). If the video is much longer than expected, some scene's animation ran too long; look for WARN in the render output.

Clean up: `rm -rf "$OUT/video/media" "$OUT/video/__pycache__"` (this is the skill's own render cache). Keep `script.json`, `scene.py`, and `audio/`.

## 3b1b visual conventions

- **Dark background** (Manim's default black). Use **3–4 colors** for the whole video, with fixed meanings, e.g. BLUE = principal, YELLOW = return, RED = cost, WHITE = neutral.
- **Objects move; avoid text cards.** Express concepts with geometry, coordinates, number lines, and stacked blocks. On-screen text is only for labels (≤ 10 characters) and titles (≤ 15 characters).
- **Build up step by step**: show one part, then add the next. Use `Indicate` / `Circumscribe` to point at the part being discussed.
- **Show changes with transforms**: `Transform` / `ReplacementTransform` / `TransformMatchingShapes` show how one form turns into another. Don't let objects simply appear and disappear.
- **Change a parameter live**: `ValueTracker` + `always_redraw` show "when x changes, y follows". This is the most 3b1b-like technique.
- At a scene boundary, either `FadeOut(*self.mobjects)` to clear everything, or keep the objects deliberately to carry into the next scene. Don't leave things behind by accident.
- Font sizes: titles 44–56, labels 28–36. Use `.scale_to_fit_width()` to keep wide objects inside the frame.
