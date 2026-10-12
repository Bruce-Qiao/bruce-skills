# STE writing rules (ASD-STE100, adapted)

ASD-STE100 (Simplified Technical English) is a controlled language from aerospace maintenance manuals. Its goal is one reading only: the reader can't misunderstand the text. This file summarizes the core rules and adapts them for Chinese.

## Two strengths

| Mode | When | Difference |
|---|---|---|
| **80% (default)** | Most explanations | Everyday words are fine; a sentence may go slightly over length if splitting it would hurt understanding; one **concrete** analogy is allowed |
| **strict** | User says `严格` / `strict` | Every rule below is a hard rule; no analogies; any sentence over the limit must be split |

## Core rules (English, from the spec)

**Words**
1. One word, one meaning. Pick one term for a concept and never swap in a synonym.
2. Use simple, common words. Technical names (e.g. "KV cache", "P/E ratio") are allowed but must be defined the first time they appear.
3. Verb tenses: only simple present, simple past, simple future, imperative. No -ing forms (except in technical names). No phrasal verbs (`set up` → `prepare`, `find out` → `learn`).
4. A noun cluster has at most 3 words (`model output token probability` ✗ → `the probability of each output token` ✓).

**Sentences**
5. One sentence, one topic.
6. Length: procedural sentences ≤ 20 words, descriptive sentences ≤ 25 words.
7. Use active voice. Steps are written as imperatives ("Divide A by B.").
8. Don't omit articles or connecting words; don't write telegraphic shorthand.
9. Put warnings and conditions first: "If X, do Y." not "Do Y if X."

**Paragraphs**
10. One topic per paragraph, at most 6 sentences.
11. Use a numbered list for steps and a bulleted list for parallel items.
12. Put extra information after a **Note:**, apart from the main text.

## Chinese adaptation (used for Chinese output)

The spec is for English. Translated into Chinese writing habits:

| # | Rule | ✗ | ✓ |
|---|---|---|---|
| 1 | Descriptive sentences ≤ 35 characters, step sentences ≤ 30 characters | 一个长句里塞因果+条件+转折 | Split into 2–3 sentences |
| 2 | One sentence, one thing | 利率上升导致估值下降并且影响融资 | 利率上升。估值因此下降。融资成本也上升。 |
| 3 | **Always state the subject** (Chinese often drops it, which causes ambiguity) | 买入后持有十年 | 投资者买入后持有十年 |
| 4 | Active voice; avoid 被 | 价格被市场压低 | 市场压低了价格 |
| 5 | One term for one concept throughout | 复利 / 利滚利 / 指数增长 mixed | Always say 复利 |
| 6 | At most 2 的 in one sentence | 公司的核心业务的利润的增长 | 核心业务的利润增长 |
| 7 | No empty verbs | 进行分析、实现增长、开展研究 | 分析、增长、研究 |
| 8 | No vague hedges | 在一定程度上、某种意义上、相对而言 | Give the condition or the number |
| 9 | No idioms, four-character rhetoric, or metaphors (in strict mode) | 水涨船高、一石二鸟 | 说出具体的因果 |
| 10 | Prefer concrete numbers | 收益很高 | 年化收益 12% |
| 11 | Steps as numbered imperatives | 首先需要做的是计算…… | 1. 计算 A。 |
| 12 | Paragraphs ≤ 6 sentences; supplementary information goes after **注：** | — | — |

Use English punctuation and English terms as they are (e.g. "ROIC"). Explain each one in Chinese the first time.

## Suggested structure

Not required. If the topic fits it, use this order:

1. **What it is**: a one-sentence definition (≤ 35 characters).
2. **What it is made of**: list the parts.
3. **How it works**: numbered steps or a causal chain.
4. **A number example**: walk through it with concrete numbers.
5. **注 (Note)**: common misunderstandings and where it does not apply.

## Self-check (required after writing)

Go through these items one by one. Fix anything that fails before you deliver:
- [ ] Any sentence over the length limit? (Count by eye; in strict mode count characters exactly.)
- [ ] Any sentence with two or more topics?
- [ ] Any sentence with no subject, or passive voice?
- [ ] Is each term used consistently from start to end?
- [ ] Any empty verbs, vague hedges, or more than 2 的 in a row?
- [ ] Is every technical term defined the first time it appears?
