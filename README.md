# bruce-skills

一组为 [Claude Code](https://claude.com/claude-code) 编写的 skill，作者 bruce。

## Skills 清单

- **clarify** —— 三层思维澄清器（维特根斯坦分解 → 苏格拉底追问 → 波兰尼默会知识捕获）。把一个模糊的念头变成精准的想法，并附上一份可直接喂给 AI 的 prompt。  
  *本 skill 基于以下文章编写：<https://x.com/Jaden_riku/status/2041013292005773507>*

- **bruce-money** —— 产品 idea 挣钱体检。对话式六步追问，把模糊念头逼成具体填空，再用『购买理由』四要素 + 三个共性 + 供需失衡 + Alpha 窗口 + 红线扫描砸一遍，给红/黄/绿三档结论 + 下一步动作。  
  *本 skill 基于刘小排课程《AI编程》编写*

- **bmp** —— BMP 投资标的体检。按 Business（低份额/大市场/护城河三问）→ Management（所有者思维/懂价值驱动两问）→ Price（earnings power 估值一票否决，≥5% earnings yield）四道关卡对单个公司做联网体检，输出 Back up the truck / Wait and watch / Reject 三档结论并落盘 Obsidian。附 quick 模式（只跑 B+M，快速淘汰）。判 Yes 比判 No 需要更强证据，命中率预期 9/10 不合格。  
  *本 skill 基于 Adam Seessel《Where the Money Is: Value Investing in the Digital Age》(2022) 编写，方法论细则与四个估值计算模板见 `bmp/references/`（含原书页码）*

- **darwin** —— 达尔文投资体检（Nalanda 流程）。按「先拒绝、后分析」五道关卡对单个公司做联网体检：六大禁区一票否决 → 10 年 ROCE 硬筛（自算口径，持续 >20%）→ 稳健性七要素 + 趋同验证 + 长期市场份额 → 诚实/廉价信号审计 → 往绩 PE 估值（永远最后，≤市场平均），输出 永久持有候选 / 观察名单 / Reject 三档结论并落盘 Obsidian。附 quick 模式（只跑禁区+ROCE）与 hold 模式（按书中仅有的三条卖出理由检视持仓，估值过高永远不是卖出理由）。  
  *本 skill 基于 Pulak Prasad《What I Learned About Investing from Darwin》(2023，中文版《我从达尔文那里学到的投资知识》) 编写，方法论细则与原则金句见 `darwin/references/methodology.md`*

- **podcast-transcribe** —— 苹果播客转写。给一个 Apple Podcasts 单集链接，自动经 iTunes Lookup API 解析出音频直链，下载后用本地 whisper.cpp（large-v3-turbo 模型，Metal 加速）转成逐字稿，按段落整理后存入 Obsidian vault，全程本地处理、音频不出本机。1 小时节目约 4 分钟转完。  
  *依赖：`brew install whisper-cpp jq ffmpeg` + [ggml-large-v3-turbo 模型](https://huggingface.co/ggerganov/whisper.cpp)（约 1.5GB，放 `~/.cache/whisper.cpp/`）。输出目录硬编码为作者的 Obsidian vault，使用前请修改 `SKILL.md` 中的路径*

## 安装

一键安装全部 skill：

```bash
git clone https://github.com/Bruce-Qiao/bruce-skills.git
cd bruce-skills
./install.sh
```

安装完成后请**重启 Claude Code 窗口**，新 skill 才会被识别。

### 只装单个 skill

如果只想要其中某个 skill，把对应目录拷到 `~/.claude/skills/` 即可：

```bash
cp -r clarify ~/.claude/skills/
```

## 使用

每个 skill 通过对应的 slash command 触发，例如 `/clarify`。具体说明见各 skill 目录下的 `SKILL.md`。

## License

MIT
