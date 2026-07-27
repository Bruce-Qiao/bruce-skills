---
name: bmp
description: "用 Adam Seessel《Where the Money Is》的 BMP 方法（Business–Management–Price）对单个公司做投资标的体检：排除清单预检 → Business 三问 → Management 两问 → 评分门 → earnings power 估值一票否决，输出 Back up the truck / Wait and watch / Reject 三档结论并存入 Obsidian。Use when user invokes /bmp, or says '用BMP分析 XX'、'BMP筛选'、'跑一下BMP'、'BMP体检'. Quick mode（只跑 B+M 不做估值）triggered by '/bmp quick' or 'BMP快筛'."
user_invocable: true
version: "1.0.0"
---

# bmp: BMP 投资标的体检

按 Adam Seessel《Where the Money Is: Value Investing in the Digital Age》的 BMP checklist，对一家公司做完整体检。方法忠实于原书，不掺其他框架。

这**不是选股器**，是逐家体检。作者的命中率预期：看过的公司约 9/10 不合格（p146）。保持这个严格度——"If your initial research to idea hit rate is high, you're not looking at enough companies, or being too lenient."

## 触发与模式

- **Full mode**（默认）：`/bmp 公司名`，或"用BMP分析 XX"。走完全部四关，含 earnings power 估值。
- **Quick mode**：`/bmp quick 公司名`，或"BMP快筛 XX"。只走第 0-2 关（排除预检 + Business + Management + 评分门），不做 earnings power 计算。用于快速淘汰，结论只有两种：**Reject / 值得进入 full mode**。Quick mode 永远不给买入结论——Price 是一票否决题，没跑过就不能说买。

一次只体检一家公司。用户给多家时逐家跑 quick mode，通过的再问是否跑 full。

## 语言

跟随用户输入语言。bruce 中文输入用中文回复；术语、公司名、指标保留英文。

## 方法论文件（先读再干活）

- `references/methodology.md` — B/M 两关的完整判断标准、moat 分类学、排除清单、非科技公司附加三问、checklist 原文（带原书页码）
- `references/earnings-power.md` — Price 关的估值方法：earnings power 概念、GAAP 调整规则、书中 Amazon/Alphabet/Intuit/Campbell's 四个计算模板

开始体检前把两个文件读入（quick mode 只需 methodology.md）。

## 数据获取纪律

体检需要联网查证，不许凭记忆编数字：

- 最新年报/10-K 的分部收入与利润、公司 IR 披露的 TAM 与市占率
- 内部人持股比例、CEO 任职以来的持股变化
- 年度股权激励稀释率（新增期权+RSU ÷ 流通股）
- 回购与 M&A 历史、ROC（NOPAT ÷ Invested Capital）
- Price 关：可比公司的营业利润率（用于成熟化 margin 三角定位）

用 WebSearch/WebFetch 查。**查不到的数据明确标「缺数据，此题存疑」，对应题目答 No 或降级处理，不编数字填坑。** 公司自报的 TAM 默认有水分，主动砍（书中先例：Seessel 把 Intuit 自称的 8 亿 TAM 砍到 2 亿，p162-163）。

## 工作流

### 第 0 关：排除清单预检

对照 methodology.md 的排除清单快速扫一遍：无差异化热门产品、tech hardware、商品化互杀行业、数字鸿沟错误一侧的旧经济、meme stock、雇佣兵型 CEO、加密货币本身。

命中 → 直接出 Reject 报告，写明命中哪条和书中对应案例，结束。不浪费研究成本。

### 第 1 关：Business（3 题，只答 Yes/No）

按 methodology.md 的标准逐题判定，每题给依据和数据来源：

1. **低市占率？** 自己拼分子分母算，砍 TAM 水分。
2. **大且增长的市场？**
3. **可持续竞争优势？** 必须落到 moat 分类学的具体一种（低成本 / 品牌 / 平台与转换成本 / 先发+二级moat / 网络效应）。"高增长"本身不是优势。

**非科技公司**：先过附加三问（tech-proof？/ 科技让它更好？/ 服务被数字革命抛下的人群？），默认有罪推定，三问全败直接 Reject。

### 第 2 关：Management（2 题）

1. **像所有者一样思考和行动？** 检验点：持股与利益绑定、花钱方式、M&A 纪律、回购史、期权稀释（一般公司 >1%/年超发，科技公司容忍 3-5%）。
2. **理解什么驱动企业价值？** 检验点：ROC 水平（20% 优秀 / 10% 平庸 / 4% 差）、资本配置记录、是否按 per-share value 思考。

### 评分门（BMP Scorecard，p76-77）

B+M 五题合计：

- **4-5 分** → "Could be a great long-term holding." 进入 Price 关（quick mode 到此为止，结论：值得跑 full mode）
- **3 分** → "Wait and watch. 'Nos' could become 'yesses.'" 写明哪些 No 有可能翻转、翻转的观察信号是什么
- **0-2 分** → Reject

### 第 3 关：Price——一票否决（仅 full mode）

按 earnings-power.md 的方法计算，步骤：

1. 收入向前滚 3 年（**仅当** moat 强 + 渗透率低 + 增长可见度高时才允许；增速假设要比历史增速保守）
2. 按分部指定"成熟化 operating margin"，每个假设用可比上市公司三角定位并写明依据
3. 成长期公司的 marketing/R&D 压到成熟对标水平，或按 EVA 法（R&D 摊 5 年、marketing 摊 3 年）
4. 算 earnings power EPS → 现价对应的倍数与 earnings yield

**硬门槛：earnings yield ≥ 5%（≤ 20x earnings power）。** 过了 → Back up the truck。没过 → 结论只能是 Wait and watch + 给出达标价位（"等 Mr. Market 给这个价"）。**没有"虽然贵但公司好所以买"的出口。**

**敏感性测试**：把最激进的 1-2 个假设砍一档重算。结论翻转 → 降档为 Wait and watch 并写明脆弱假设是哪个。书的标准是 "approximately right rather than precisely wrong"——结论必须扛得住单个假设的摆动（p144-145）。

## 报告落盘

写入 `/Users/bruceqiao/obsidian_vault/BMP Screens/`（非 bruce 本机使用时，改为你自己的笔记目录），文件名 `{Ticker或公司名} BMP {YYYY-MM-DD}.md`（quick mode 加后缀 ` quick`）。同一公司重跑不覆盖旧报告——新日期新文件，旧报告就是历史判断记录。目录不存在则创建。

报告结构（full mode；quick mode 砍掉 Price 部分）：

```markdown
# {公司名} ({Ticker}) — BMP 体检

日期：YYYY-MM-DD ｜ 模式：full/quick ｜ 现价：$XX

## 结论：🟢 Back up the truck / 🟡 Wait and watch / 🔴 Reject

（一句话判断，30 字内）

## 第 0 关：排除预检
（通过 / 命中哪条）

## BMP Checklist

### Business
| # | 问题 | 答案 | 依据（含数据来源） |
|---|------|------|------|
| B1 | 低市占率？ | Yes/No | 分子/分母 = X%，TAM 砍水分过程 |
| B2 | 大且增长的市场？ | Yes/No | |
| B3 | 可持续竞争优势？ | Yes/No | moat 类型 + 证据 |

### Management
| # | 问题 | 答案 | 依据 |
|---|------|------|------|
| M1 | 像所有者思考和行动？ | Yes/No | 持股 X%、稀释 X%/年、回购/M&A 记录 |
| M2 | 理解什么驱动企业价值？ | Yes/No | ROC = X%、资本配置记录 |

**Scorecard：X / 5** → （门判定）

## Price（一票否决）
### Earnings Power 计算
（分部表：收入 → 3 年滚动 → 指定 margin + 依据 → earnings power）
- Earnings power EPS：$X
- 现价倍数：Xx ｜ Earnings yield：X%
- **门槛判定：≥5% yield？Yes/No**
- 达标买入价：$X 以下

### 敏感性测试
（砍哪个假设、砍成什么、结论是否翻转）

## 缺数据与存疑项
（列出查不到的数据和因此降级的题目）

## 翻转观察点
（哪些 No 未来可能变 Yes，看什么信号；Wait and watch 时必填）
```

## 风格纪律

- 不奉承，不铺垫。结论先行。
- 每个 Yes/No 必须有可核查的依据，写明数据来源（年报页码、IR 材料、新闻源）。
- 判 Yes 比判 No 需要更强的证据。默认怀疑：TAM 有水分、护城河存疑、管理层是 caretaker，除非证据推翻。
- Price 关不达标就是不达标，不给"但是"。书里 Seessel 自己按"看着贵"卖飞 Amazon 六次，教训是反向的——但买入门槛从不松动。
- 本书**没有量化卖出规则**，skill 不给卖出建议；用户问就如实说书里没有。
- 报告写完只在对话里给结论摘要 + 文件路径，不把全文重贴一遍。

## 引用来源

方法论 1:1 来自 Adam Seessel, *Where the Money Is: Value Investing in the Digital Age* (2022)。references 内所有页码为印刷版页码。本 skill 仅做流程化封装，不替代原文阅读。
