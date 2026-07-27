# Price 关：Earnings Power 估值方法与计算模板

来源：Adam Seessel, *Where the Money Is* (2022) ch7-9。页码为印刷版页码。

## 1. 工具箱取舍（ch7）

- **弃用 P/B 及一切资产类指标**：数字经济中物理资产基本无关（p123-124）。仅在极端市场恐慌时拿出来（Seessel 在 dot-com 崩盘按清算价值买 Apple、2009 年买 net-net Movado）。
- **弃用均值回归/板块轮动**："这次不一样"在数字时代是准确陈述；很多科技公司不是围绕均值波动，而是 "just now achieving escape velocity"（p125）。
- **保留但改造 P/E**：北极星仍是现金收益（John Burr Williams DCF 原理），但远期现金流不可测，用 P/E 简写（p125-126）。

## 2. 对 P/E 的两处改造（p126）

1. **收入向前滚 3 年**（不是 5 年、10 年）。**前提**：moat 强、渗透率低、增长可见度高（"What is the likelihood that Alphabet will grow its business over the next thirty-six months?"）。增速假设取比历史增速保守一档（AWS 历史 35% → 用 30%）。
2. **用 earnings power 替代报表利润**。

## 3. Earnings Power 概念（p83-84）

"Earnings power is neither a profit forecast nor an earnings estimate. Instead, earnings power attempts to quantify a digital company's latent, underlying ability to generate profits."

三个目标：① 让科技公司与成熟公司短期内直接可比；② 去除会计扭曲、"de-penalize" 对未来的投资；③ 作为长期创富能力的 "rough but directionally accurate proxy"。

**GAAP 扭曲机理**（p127-129）：R&D 与 sales & marketing 几乎 100% 当期费用化，而厂房设备折旧 20-30 年。工业公司投 $1 亿建厂当年只确认 $400 万费用、利润 $9600 万；科技公司花 $1 亿做 R&D 当年利润为零。如今科技支出多为 "D"（development，已验证想法的实施）而非投机性 "R"，一年寿命假设荒谬。

背景比率：软件公司天然盈利能力是普通美国公司 3-4 倍——90% 毛利率常见，成熟软件公司（Oracle）营业利润率近 50%，约 Coca-Cola 两倍（p79）。

**费用资本化参考框架**：
- Bennett Stewart EVA 法：R&D 按 5 年摊、marketing 按 3 年摊（p129, p144-145）
- 公司内部视角：LTV/CAC（Intuit 要求 LTV ≥ 3×CAC、marketing 支出至少 50% 回报，p82, p130）
- 先例：Buffett 1999 年明说 GEICO 的营销支出故意压低当期利润（p130-131）

精度要求："approximately right rather than precisely wrong"。

## 4. 计算模板

### 模板 A：Common-size 对标法（Intuit vs Campbell's，p79-85）

适用：成长期公司有清晰的成熟对标。方法：两家按收入=100% 同口径对比，把成长期公司的 marketing/R&D 压到成熟对标水平（假想 harvest mode）。

| | Campbell's | Intuit 报表 | Intuit adjusted |
|---|---|---|---|
| Cost of goods | 65% | 18% | — |
| Gross profit | 35% | 82% | 82% |
| Marketing | 11% | 27% | **11%** |
| R&D | 1% | 18% | **1%** |
| Admin/other | 10% | 9% | 9% |
| Operating income | 13% | 28% | **61%** |
| EPS | $2.50 | $6.92 | $14.92 |
| P/E | 20x | 43x | **20x** |

表观 43x → earnings power 20x，earnings yield 与 Campbell's 相同（5%），且实际更便宜（几年后利润再高 50%）。

### 模板 B：分部 margin 重构法（Amazon，ch8, p132-142）

适用：多分部公司，报表利润被亏损/投资期分部掩盖。数据来自年报分部披露（Amazon 2019 年报 p67-68）。

Step 1：各分部收入滚 3 年（AWS 35%→保守 30%；电商 20%）。

Step 2：给各分部指定 "reasonable operating margin"（成熟化假设，可比公司三角定位）：

| 分部 | 2019 收入 | 指定 margin | 依据 | Earnings power |
|---|---|---|---|---|
| Online retail | $141B | **10%** | Walmart 6% + 2pt（无折旧包袱）+ 1pt（无 shrink）≈9%；公司自己长期目标 10-13% | $14B |
| Physical stores | $17B | 2% | 不重要（materiality standard） | $0.3B |
| Subscriptions | $19B | **0%** | loss leader，当 breakeven | — |
| Third-party seller | $54B | **25%** | 对标 eBay 25%（eBay 高营销费 ≈ Amazon 高物流费，互抵） | $14B |
| Advertising ("Other") | $14B | **50%** | 真实 margin 近 100%，保守取 50% | $7B |
| 零售合计 | $245B | **14%** | vs 报表 2% | **$35B**（报表 $5.3B 的近 7 倍） |
| AWS | $35B | 26%（已 at scale，不调） | | $9.2B |

合并 + 3 年滚动：2022E 收入 $500B × 16% = $80B 营业利润 → EPS $132 → $2,000 股价 = **15x earnings power**（vs 报表 87x），yield 1% → 7%。低于 20x → "table-pounding buy"（p145）。

方法论要点：
- 核心自问："这家公司如果是 harvest mode 的成熟公司会报出什么利润率？"用同类上市公司三角验证（p133）。
- 分部要过 materiality standard，不重要的分部不精算（p137-138）。
- 识破报表悖论："Walmart 利润率是 Amazon 电商的 3 倍——有人真信吗？"（p127, p135）

### 模板 C：整体 margin 修正法（Alphabet 2016，ch9, p154-156）

适用：单一主业但 margin 被亏损业务/低效支出拖累。

三个修正依据：① 同为 toll bridge 的 Facebook/Alibaba 有 40-50% 营业利润率，Alphabet 收入是它们 5 倍却只 25%，不合理；② Other bets 年亏 $3.5B，加回 → 25%→30%；③ YouTube/Android 当时亏钱但商业属性注定盈利。

处理：整体指定 **40% 营业利润率**（对齐 Facebook）；收入按历史 20% 滚 3 年；**从股价扣每股现金**（cash-adjusted price；脚注承认可争议——不扣则 9x 变 12x，结论不变，p168 脚注）。

结果：2015 报表 EPS $23.11、28x → 2018 earnings power EPS ~$64、**9x**；市场平均 20x → "backed up the truck"（p155）。

### 模板 D：驱动因子分拆法（Intuit 2020，ch9, p163-165）

适用：需要 mix shift 建模的公司（高增长业务占比逐年上升）。

- QBO 订户 +30%/年（低于历史 35-40%）；ARPU +9%/年；成熟业务（TurboTax、QB Desktop）+6%/年
- 营业利润率 25% → **40%**（介于现状 25% 与 harvest 模式 60% 之间——"60% 太激进，Intuit 短期不会进 harvest mode"；40% 约等于 EVA 资本化处理的结果）
- 股本 -3%/年（有回购史才允许这条假设）
- 结果：2019 EPS $5.89、51x → 2022E EPS $15.44、**19x** < 20x → $300 买入（p166-168）

关键教训：初版模型只是延续 9% 整体增速，错在没把 QBO 的 mix shift 放进前景——"我还在做 financial analyst 而不是 business analyst"（p164）。

## 5. 模板选择指引

| 情况 | 模板 |
|---|---|
| 有清晰成熟对标的单业务成长公司 | A：common-size 对标 |
| 多分部、报表利润被投资期分部掩盖 | B：分部 margin 重构 |
| 单一主业、margin 被亏损业务拖累 | C：整体 margin 修正 |
| 业务组合 mix shift 明显 | D：驱动因子分拆 |

可组合使用（如 B 里的单个分部用 A 的对标思路定 margin）。

## 6. 硬规则汇总

1. **门槛：earnings yield ≥ 5%，即 ≤ 20x earnings power**（p78）。"If I can't get to a 5% earnings yield, I won't make the investment."
2. 不达标 → **Wait and watch + 给出达标价位**。没有例外出口。
3. 收入只滚 3 年，增速假设比历史保守一档。
4. 每个 margin 假设必须有可比公司依据，写进报告。
5. **敏感性测试**：砍最激进的 1-2 个假设一档重算（书中示范：Amazon 在线零售 margin 10%→5%，倍数 15x→18x，结论不变，p144-145）。结论翻转 → 降档 Wait and watch。
6. 现金扣减（cash-adjusted price）可用但要在报告里标注，并给不扣现金的对照数。
