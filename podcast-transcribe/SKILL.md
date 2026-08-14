---
name: podcast-transcribe
description: 苹果播客转写。给一个 Apple Podcasts 链接（podcasts.apple.com），自动找到音频、用本地 whisper.cpp 转成逐字稿，存入 Obsidian vault 的 Podcasts/ 目录。Use when user shares a podcasts.apple.com link, or says '转写这期播客', '播客逐字稿', 'transcribe this podcast episode'. NOT FOR YouTube（用 summarize）、摘要（转写完可另行分析）。
---

# Podcast Transcribe

Apple Podcasts 链接 → 本地转写 → Obsidian 逐字稿笔记。全程本地处理，音频不出本机。

## 依赖（已安装，缺失时提示用户，不要自行安装）

- `whisper-cli`（brew whisper-cpp）
- 模型：`~/.cache/whisper.cpp/ggml-large-v3-turbo.bin`
- `jq`、`ffmpeg`、`curl`

## 输出约定

- 目录：`/Users/bruceqiao/obsidian_vault/Podcasts/`
- 文件名：`<播客名> - <单集标题>.md`（去掉 `/ : ? # |` 等非法字符；过长截到 ~80 字符）
- 临时音频放 scratchpad，转写完成后删除
- 逐字稿默认无时间戳；用户要时间戳时用 `-osrt` 另存 `.srt`

## 流程

### 1. 解析链接，拿到音频地址

Apple 链接形如 `https://podcasts.apple.com/cn/podcast/xxx/id<播客ID>?i=<单集ID>`。

```bash
# 播客 ID: id 后的数字；单集 ID: i= 参数
curl -s "https://itunes.apple.com/lookup?id=<播客ID>&entity=podcastEpisode&limit=200" \
  | jq '.results[] | select(.trackId == <单集ID>) | {trackName, collectionName, releaseDate, trackTimeMillis, episodeUrl}'
```

- `episodeUrl` 就是音频直链；同时记下单集标题、播客名、发布日期、时长（毫秒）。
- **链接没有 `i=` 参数**（只给了播客不是单集）：列出最近几集的 `trackName + releaseDate` 问用户要哪期。
- **200 条里找不到该单集**（老节目）：`curl -s "https://itunes.apple.com/lookup?id=<播客ID>" | jq -r '.results[0].feedUrl'` 拿 RSS，在 RSS 里按标题模糊匹配 `<enclosure url=...>`。

### 2. 下载音频

```bash
curl -sL -o "$SCRATCHPAD/episode.mp3" "<episodeUrl>"
```

用 `file` 确认实际格式。whisper-cli 支持 flac/mp3/ogg/wav；若是 m4a/aac 则先转：

```bash
ffmpeg -y -i episode.m4a -ar 16000 -ac 1 episode.wav
```

### 3. 转写

```bash
whisper-cli -m ~/.cache/whisper.cpp/ggml-large-v3-turbo.bin \
  -f "$SCRATCHPAD/episode.mp3" \
  -l auto -t 8 -np -otxt -of "$SCRATCHPAD/transcript"
```

- 1 小时节目约 3-5 分钟，用 run_in_background 跑，期间不要空等。
- 中文播客若输出繁体，加 `--prompt "以下是简体中文的转写。"` 重跑。
- 转写失败或输出为空：报告错误原因，不要静默给空文件。

### 4. 写入 Obsidian

文件 `/Users/bruceqiao/obsidian_vault/Podcasts/<播客名> - <单集标题>.md`：

```markdown
---
podcast: <播客名>
episode: <单集标题>
published: <YYYY-MM-DD>
duration: <HH:MM:SS>
source: <Apple Podcasts 原链接>
transcribed: <今天日期>
engine: whisper.cpp large-v3-turbo
---

# <单集标题>

<逐字稿正文，按语义分段，不要一大坨>
```

正文处理：whisper 输出是逐行短句，合并成自然段落（说话人换话题/明显停顿处分段），不改动内容本身。

### 5. 收尾

- 删除 scratchpad 里的音频和中间文件
- 告诉用户：笔记路径 + 时长 + 一句话说明内容大致是什么（读开头结尾即可，不做完整摘要）

## 红线

- 不安装任何新依赖；依赖缺失就停下来告诉用户
- 不覆盖 Podcasts/ 下已有同名文件——同名说明转写过，直接给出已有文件路径
- 转写内容一字不改（繁简转换除外），摘要/分析是别的 skill 的事
