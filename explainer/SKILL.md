---
name: explainer
description: "Turn any topic into an easy-to-understand explanation using the four output methods from Karpathy's tweet (2026-10): ste (ASD-STE100 controlled-language writing), diagram (Mermaid/SVG), html (interactive single-file web page), video (3b1b-style Manim animation + CosyVoice local narration). Any one method or any combination, saved to Obsidian. Use when user invokes /explainer, or says '用STE解释'、'画图讲解'、'做个讲解网页'、'做个讲解视频'、'explainer'. NOT FOR 概念八维解剖（用 ljg-learn）、白话改写（用 ljg-plain）、卡片海报（用 ljg-card）。"
user_invocable: true
version: "1.0.0"
---

# explainer: four ways to make a topic easy to understand

Source: Karpathy's tweet https://x.com/karpathy/status/2105819303471976479 . In order, each method beats the one before it:

1. **ste**: write in ASD-STE100 controlled language. Short sentences, one idea per sentence, no ambiguity.
2. **diagram**: draw a picture instead of writing text.
3. **html**: an interactive web page.
4. **video**: a 3b1b-style explainer video with narration. Narration uses **local CosyVoice** (not ElevenLabs).

## Invocation

```
/explainer [modes] [options] <topic | file path | URL>
```

**modes** (any combination, joined with `+`, spaces, or commas):

| mode | Chinese alias | Output |
|---|---|---|
| `ste` | 文字 | STE text, written in the entry note |
| `diagram` | 图 | A Mermaid code block in the entry note, or `diagram.svg` |
| `html` | 网页 | `index.html` |
| `video` | 视频 | `video.mp4` |

- **No mode given → `ste+diagram+html`.** Video only runs when asked explicitly (it takes several minutes).
- `all` / `全部` = all four.

**options**:
- `严格` / `strict`: 100% STE (default 80%; see `references/ste.md`)
- `英文` / `english`: write in English (default: follow the input language)
- Narration voice: **defaults to the user's own voice** (`~/Coding/CosyVoice/my_voice.wav` + the transcript `my_voice.txt` next to it; if either file is missing, CosyVoice's sample voice is used). `内置声音` / `--builtin-voice` = use the sample voice this time; `--ref <wav> --ref-text "原话"` = use another voice this time; `--instruct "请用稍慢的语速说。"` = narration style

**Input**: a topic name → research and explain it yourself; a file path / URL → read it first, then explain what it says. When a fact needs checking, look it up online. Don't make up numbers.

Before starting, state the parsed result in one line, e.g. "主题：复利 ｜ 方法：ste+video ｜ STE 80% ｜ 中文", then go straight to work without waiting for confirmation.

## Output location

```
OUT=~/obsidian_vault/Explainers/{主题} {YYYY-MM-DD}/
```

(When used on a machine other than bruce's, change this to your own notes folder.) Create the folder if it doesn't exist. If a folder with the same name already exists (same topic, same day), add a suffix ` 2`. **Never overwrite earlier output.**

| File | When it is produced |
|---|---|
| `{主题}.md` | Always: the entry note |
| `diagram.svg` | When diagram chooses SVG |
| `index.html` | When html is chosen |
| `video.mp4` + `video/` (`script.json`, `scene.py`, `audio/`) | When video is chosen |

Entry note template (write only the sections for the chosen methods):

```markdown
# {主题}

> 来源：{话题 / 文件 / URL} ｜ 方法：{modes} ｜ {YYYY-MM-DD}

## 文字（STE）
...

## 图
```mermaid
...
```
（或 ![[diagram.svg]]）

## 网页
[打开 index.html](index.html)

## 视频
![[video.mp4]]
```

Write preview screenshots used for checking to a temp folder (`mktemp -d`), not into the vault.

## Order of work

Several methods run in the order **ste → diagram → html → video**. Later steps reuse earlier results:
- The STE text is the **content baseline**. The diagram, page, and video must not contradict it.
- The diagram's structure → the page's interactive core → the video's storyboard.

Even when ste is not chosen, first write a short internal STE draft to get the facts and the logical chain straight. Don't put it in the note.

## 1. ste

Read `references/ste.md` and follow its rules. After writing, **you must** go through its self-check list. Fix anything that fails before writing it into the note.

## 2. diagram

**Choose the form:**
- Flows, structures, hierarchies, causal chains, timelines → **Mermaid** (rendered natively by Obsidian, so put it straight into the note)
- Spatial relationships, geometry, quantity comparisons, curves, anything Mermaid can't show → **hand-written SVG** → `diagram.svg`

**Rules:**
- One diagram, one main idea. Too much information → split into 2 diagrams, not one crowded one.
- Labels ≤ 10 characters. Arrows must carry a verb or causal word ("推高", "导致"); don't draw bare arrows.
- Mermaid: ≤ 12 nodes; node text uses `["..."]` quotes so Chinese and symbols don't break the syntax.
- SVG: set `viewBox`, put `font-family="PingFang SC, sans-serif"`, use ≤ 4 colors with fixed meanings, white background.

**Check (required):** write the Mermaid to a temp `.mmd`, then:
```bash
~/.claude/skills/explainer/scripts/preview.sh <file.mmd|diagram.svg> <tmp>/diagram.png [w] [h]
```
Look at the PNG with Read. Check for overlaps, cut-off text, crossed arrows, and messy layout. Fix and check again.

## 3. html

**Goal:** a page that makes the concept "move". Not the article pasted into a web page.

**Hard requirements:**
- A single file, `index.html`, with inline CSS/JS and **no external dependencies** (works offline).
- **At least one core interaction**: a slider that changes a parameter, step-through, or hover/click to expand. Changing the parameter must change the concept itself (e.g. dragging the interest rate redraws the compound curve in real time).
- Structure: one-sentence definition → interactive core → explanation (written in STE style) → number example → common misunderstandings.
- Dark mode via `prefers-color-scheme`; readable at 390px mobile width with no horizontal scrolling.
- Draw charts with `<canvas>` or inline SVG; don't pull in a chart library.

**Check (required):**
```bash
~/.claude/skills/explainer/scripts/preview.sh "$OUT/index.html" <tmp>/desk.png 1280 900
~/.claude/skills/explainer/scripts/preview.sh "$OUT/index.html" <tmp>/mobile.png 390 844
```
Look at both screenshots. Also open the page with `open "$OUT/index.html"` so the user can try the interaction.

## 4. video

Read `references/video.md` and follow its workflow: script → CosyVoice synthesis (`scripts/tts_batch.py`, run in the background) → `scene.py` → `-ql` preview + frame-by-frame check → `-qh` final render → length check → delete the `media/` cache.

Time estimate: a 2-minute video ≈ 3 minutes for synthesis + 1–3 minutes for rendering. Before starting, tell the user it will take a few minutes.

## Final reply

Keep it short:
- Output folder path + the list of files produced
- Each method in one sentence: what it shows (e.g. "视频 1:52，6 个场景，从本金堆叠讲到 72 法则")
- Any part that failed or was downgraded must be stated plainly (e.g. "SVG 有一处标签重叠未能完全消除")
