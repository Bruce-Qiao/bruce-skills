# bruce-skills

一组为 [Claude Code](https://claude.com/claude-code) 编写的 skill，作者 bruce。

## Skills 清单

- **clarify** —— 三层思维澄清器（维特根斯坦分解 → 苏格拉底追问 → 波兰尼默会知识捕获）。把一个模糊的念头变成精准的想法，并附上一份可直接喂给 AI 的 prompt。  
  *本 skill 基于以下文章编写：<https://x.com/Jaden_riku/status/2041013292005773507>*

- **bruce-money** —— 产品 idea 挣钱体检。对话式六步追问，把模糊念头逼成具体填空，再用『购买理由』四要素 + 三个共性 + 供需失衡 + Alpha 窗口 + 红线扫描砸一遍，给红/黄/绿三档结论 + 下一步动作。  
  *本 skill 基于刘小排课程《AI编程》编写*

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
