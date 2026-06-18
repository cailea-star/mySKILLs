---
name: introduction-writing
description: Build and revise academic or technical introductions and opening reports with quote-first keyword chains, confirmed core reference pools, verified original quotations, section/paragraph progression, paragraph-by-paragraph prose drafting, Chinese-corpus style calibration, and approval-gated write-in. Use when working on 开题报告, research background, introduction structure, literature evidence, keyword chains, 正文草稿, paragraph-by-paragraph reference support, or formal prose from verified quotations.
---

# Introduction Writing

## 1. Skill 定位

Use this skill to build 开题报告 / introduction logic from authoritative references instead of secondary unsupported claims.

Core workflow:

```text
core reference pool
-> local evidence discovery
-> section progression
-> paragraph progression
-> quote-first keyword chains
-> review
-> prose
```

Core principles:

```text
Core references constrain field logic.
Original quotations generate claims.
Chinese keywords organize relations only.
Keyword relations are built from quotation sets.
Paragraph functions organize accepted quote-chains.
Section progression organizes paragraph functions.
```

`【关键词链】` is a concept-relation chain, not a keyword list.

Quote-first definition:

```text
中文 A -> 中文 B（关系）：original quotation set only.
```

Hard rules:

- Keep Chinese content limited to keyword nodes and relation type.
- Do not write Chinese explanatory claim sentences inside quote-first keyword chains.
- Let original quotations carry the claim or viewpoint.
- Support each keyword chain with original quotations from at least three different references in the confirmed core reference pool: at least one from Abstract/Introduction and at least two from Conclusion/Discussion/Summary/Outlook/Perspectives when those sections exist.
- Prefer 20-40 words per quotation when source and copyright constraints allow.
- Use complete argumentative units: each quotation must contain a predicate and independently express the relation.

## 2. 证据源规则

For nuclear physics, unless the user changes it, use this default authoritative pool:

```text
RMP / PPNP / ARNPS / PR / NRP / PRL / PLB
```

Confirm a core reference pool for the active section or paragraph before building quote-chains. Group references by role when useful:

```text
main review
method review
experimental or phenomenological evidence
foundational theory
recent progress
```

Evidence discovery order:

1. Existing project files and target draft.
2. Local reference notes, especially `原文 / 译文 / 解读` blocks and brief source traceability lines.
3. Relevant key-section notes for method-heavy or evidence-heavy paragraphs.
4. Original papers, trusted local full-text extracts, Zotero full text, or publisher pages cited by notes.
5. External authoritative search only when local/original evidence is missing, too indirect, outdated, contradicted, or explicitly requested.

Local `.md` notes are discovery aids, not final evidence, unless the user explicitly asks to cite notes. Final quote evidence must be checked against original article text, trusted full-text extraction, Zotero full text, or publisher pages.

Quotation evidence rules:

- Each keyword relation must have original quotations from at least three different references in the confirmed core reference pool: at least one from Abstract/Introduction and at least two from Conclusion/Discussion/Summary/Outlook/Perspectives when those sections exist.
- Each quotation must prove a relation: definition, cause, decomposition, limitation, evidence, method, validation, transition, or application.
- Each quotation must be a complete viewpoint-bearing clause or sentence, not a noun phrase, title fragment, topic label, or isolated term.
- Reject weak evidence such as `("Q-value")`, `("Fine structure")`, `("important probe")`, or `("Shape coexistence in nuclei")` unless the relation is only naming.
- Mark paraphrase as paraphrase. Do not format paraphrase as direct quote.
- Do not use a sentence as evidence when it is only a secondary citation or a report of another paper's result. If a useful sentence depends on a cited source such as `Refs.`, `as shown in Ref.`, or `see Ref.`, inspect whether it is the author's own synthesis or a pure second-hand claim; for pure second-hand claims, follow the citation one level deeper and use the primary source instead. Mark allowed review-level synthesis as `review_synthesis`.
- Use the smallest complete quotation set that supplies enough original wording for later prose. Do not overquote.

Mandatory re-read before any new chain, review, prose, or write-in:

1. Re-read the active paragraph or section.
2. Re-read the confirmed core reference pool, using local notes only to locate original evidence.
3. State briefly which core references were consulted and which keyword relations their original quotations support.
4. Do not mark a relation `ready_strong` unless it has 3+ strong original quotations from different core-pool references, including >=1 Abstract/Introduction source and >=2 Conclusion/Discussion/Summary/Outlook/Perspectives sources, with no pure secondary citation sentence.

Evidence status:

```text
ready_strong = 3+ strong original quotations from different core-pool references, with >=1 Abstract/Introduction source and >=2 Conclusion/Discussion/Summary/Outlook/Perspectives sources, and no pure secondary citation sentence
ready_min = 2+ strong original quotations from different core-pool references; temporary only, mark the missing evidence slot
needs_core_second_source = only one core-pool reference verified
supplemented_not_ready = one core-pool reference plus non-core support
paraphrase_only = no verified original quotation
weak_quote = quotation incomplete or topic-only
conflict_check = core references frame the relation differently
review_synthesis = allowed review-level synthesis, not pure second-hand claim
```

## 3. 六步工作流

### Gate 1：题目、研究对象、研究方法与核心参考文献池

Establish the working title, genre, target document, core research object, core research method, and active section/paragraph. Extract 2-5 core keywords from the title, research object, research method, and draft. Confirm the active core reference pool before building structure or quote-chains, and ensure it supports both the research object and research method.

Output:

```text
title / genre / target document
active section or paragraph
core research object
core research method
core keywords
confirmed core reference pool by role
```

### Gate 2：本地文献笔记建立与使用

Create or use `Original/` for original PDFs and full-text files. Name original evidence files as `refX_title.pdf` or `refX_title.txt`. Create or use `Note/` for local reference notes.

Inspect local notes, original PDFs, full-text extracts, and reference lists for the confirmed core pool. Select local reference-note entries based on the Gate 1 title, core research object, and core research method. Use the active project's existing note style when it is already clear. When creating or normalizing notes, prefer the minimal three-part structure `原文 / 译文 / 解读`; keep metadata such as source, DOI, arXiv, page, section, or evidence status only as brief traceability lines, not as extra analytical sections.

Build or update local notes only when needed to locate original evidence. In each note, make the evidence status explicit: original full-text extraction, normalized full-text extraction, compressed paraphrase, focused reading note, or interpretation. Local notes remain discovery aids unless the relevant passage is explicitly verified against original article text, trusted full-text extraction, Zotero full text, or a publisher page.

Output:

```text
Original paths for original PDFs / full-text
Note paths for local reference notes
available 原文 / 译文 / 解读 blocks
original evidence source paths or URLs
candidate sections for quotation extraction
```

### Gate 3：章节推进链

Design section-level progression before paragraph detail. For each section, state function, main conceptual progression, and exit pressure: why the next section is required. Also state how the section progression appropriately introduces, defines, and emphasizes the core research object or core research method. For method-centered sections, state how the method is introduced, defined, and given supported advantage.

For opening reports, default macro progression:

```text
选题背景及意义
-> 国内外发展现状与趋势
-> 研究内容与预期目标
-> 研究方法、技术路线与可行性
```

User approval is required before writing section-level structure into the target document.

### Gate 4：章节内段落推进链

For the active section, split paragraph units. For each paragraph, state short title, paragraph function, paragraph progression, and bridge to the next paragraph. Keep background, status, gap, research content, and method workflow separated.

User approval is required before writing paragraph-level structure into the target document.

### Gate 5：引文先行的段落关键词链

Work paragraph by paragraph.

1. Read the target paragraph's current wording, current `【段落主线】`, and current `【桥接句】`; treat the mainline and bridge as initial, not final.
2. Review local notes for the active paragraph and confirmed core reference pool before searching again. If local notes are missing or too thin, tell the user and provide candidate note entries or passages to add.
3. Extract Chinese keyword relations as `中文 A -> 中文 B（关系）`.
4. Search the confirmed core reference pool for original quotations, using local notes only as discovery aids.
5. Critique the initial `【段落主线】` and `【桥接句】` against the common logic-flow found in the original quotations: missing concepts, premature definitions, weak transitions, overstrong relations, repeated relations, misplaced emphasis, or a bridge that does not create enough pressure for the next paragraph.
6. Propose an optimized `【段落主线】` and optimized `【桥接句】` based on the reference logic-flow before proposing final quote-chains.
7. For each relation, require at least three different core-pool references per relation: at least one quotation from Abstract/Introduction and at least two from Conclusion/Discussion/Summary/Outlook/Perspectives when available.
8. Reject pure second-hand citation sentences; if a sentence only repeats another source, trace one level deeper and use the primary source instead. Mark acceptable review synthesis as `review_synthesis`.
9. Prefer 20-40 word complete argumentative quotation units.
10. Reject weak, topic-only, phrase-only, or paraphrase-only evidence.
11. Compare the draft wording with the authoritative original wording.
12. Build candidate quote-first keyword chains with evidence status.
13. Wait for user review before write-in.

Do not reduce chain count merely for concision during corpus-expansion passes. Preserve the user's chain granularity and increase original quotation diversity.

Default paragraph-review output order:

```text
本地笔记回顾
-> 初版段落主线批判
-> 初版桥接句批判
-> 参考文献常见 logic-flow
-> 优化版段落主线
-> 优化版桥接句
-> 关键词链候选（中文关键词 + 原文引文 only）
-> 等待用户审阅
```

### Gate 6：正文草拟、审阅与写入

Use when the user asks to write `【正文】`, continue `P1/P2/...`, or convert accepted keyword chains into formal prose.

1. Re-read the active paragraph's `【作用】`, `【段落主线】`, `【关键词链】`, and `【桥接句】`.
2. Re-read adjacent paragraphs only for continuity; do not import their claims into the active paragraph.
3. Use Chinese corpus articles for terminology, sentence rhythm, and discipline style only; do not treat Chinese corpus wording as evidence unless it is in the reference list and cited.
3a. Before drafting, check whether the available Chinese corpus supports the active paragraph's key Chinese terminology and style. If central terms are missing, stop and tell the user what corpus should be added instead of drafting from memory.
4. Check keyword-chain status before drafting: prefer `ready_strong`; if any relation is only `ready_min`, state the missing evidence slot and do not treat it as final unless the user explicitly accepts that limitation.
5. Enforce `【专业术语规范】`: choose Chinese/English terms and symbols only from the reference corpus, accepted keyword chains, or verified original evidence; do not invent or normalize terms from memory.
6. Draft one `【正文】` paragraph from accepted keyword-chain relations.
7. Make each sentence map to one keyword relation or bridge function.
8. Add bracket citations like `[4,17]`; do not include original quotations in `【正文】`.
9. Do not add a citation merely to avoid an unused reference. Any newly used reference must support an accepted keyword-chain relation.
10. Avoid generic filler transitions such as `在将...之后，需要...` when the next sentence can state the claim directly.
11. Avoid project-only framing such as `对本课题而言` for field-general claims.
12. Output `语料充分性检查`, `证据状态检查`, `正文草稿`, and `逐句对照` for user review first. Never write into the target document in the same turn unless the user has explicitly approved write-in after seeing the draft.
13. After approval, update only the active paragraph's `【正文】` field.

Reference order helper:

```text
scripts/reorder_refs.py
```

Use this helper only after the user approves citation renumbering for a Markdown draft. It expands bracket citation groups/ranges, applies first-use numbering through OLD labels, and sorts Markdown reference blocks such as `<a id="ref1"></a>[1]`.

## 4. 各 Gate 审查要点

Use these checks inside each Gate. Do not wait for a final omnibus review.

### Gate 1 审查要点

- 核心参考文献池是否足够权威
- 文献角色是否清楚
- 核心关键词是否明确
- 核心【研究对象】是否明确
- 核心【研究方法】是否明确

### Gate 2 审查要点

- 证据是否可追踪到原文、full-text、Zotero full text 或 publisher page
- 本地笔记是否只作为证据发现线索
- 是否误把译文、解读、本地改写当作原文证据

### Gate 3 审查要点

- 章节推进链是否恰当【引出】【定义】【强调】研究对象或研究方法
- 各章节是否有核心关键词
- 重要概念是否按章节推进完成：引入 -> 定义 -> 强调
- 核心方法是否完成：引入 -> 定义 -> 优越性说明
- 若多段之间出现整体作用错位，回到章节推进链检查段落组是否仍服务章节出口压力

### Gate 4 审查要点

- 各段【段落主线】是否服务章节核心词
- 段落功能是否重复
- 背景、现状、缺口、方法、研究内容是否混写
- 桥接句是否制造下一段必要性
- 相邻段落是否形成“上一段未解决的问题 -> 下一段处理的对象”
- 段落【作用】是否互相区分，避免两个段落承担同一功能
- 【桥接句】是否具体指向下一段关键词，而不是泛泛过渡

### Gate 5 审查要点

- 每条关键词链是否 `ready_strong`；`ready_min` 只能临时使用并标明缺口
- 是否有 3+ 核心文献原文证据：>=1 Abstract/Introduction，>=2 Conclusion/Discussion/Summary/Outlook/Perspectives
- 引文是否为完整观点单元
- 引用是否证明关系，而不是只提到主题
- 重复关系是否合并、移动、收束，或说明保留理由
- 关键词链是否承接上一段出口并服务本段【作用】
- 关键词链末端是否自然生成下一段入口，避免概念跳跃

### Gate 6 审查要点

- `【正文】` 是否逐句对应关键词链或桥接功能
- 正文使用的关键词链是否达到 `ready_strong`；若为 `ready_min`，是否清楚标出缺口并经用户接受
- 中文语料是否只用于术语和行文风格校准
- `【专业术语规范】` 是否严格来自参考语料、已接受关键词链或已核验证据
- 中文术语、英文术语、符号写法是否与参考语料保持一致
- 是否避免翻译腔、空泛过渡和不必要的“本课题”限定
- 是否使用 `[1,2]` 形式参考标注且不出现原文引文
- 是否避免为了消除空引而硬塞参考文献；新增引用必须对应已接受关键词链
- 是否先给用户审阅草稿，获批后才写入
- 正文首句是否承接上一段末句或桥接句
- 正文末句是否为下一段制造必要性，而不是提前替下一段展开

## 5. 模板

Use these templates only when they match the current Gate. Do not reintroduce Chinese explanatory claims into quote-first keyword chains.

### 核心参考文献池

##### 本地参考文献说明

```md
【核心参考文献池】
- 主综述：
- 方法综述：
- 实验/现象证据：
- 基础理论：
- 近期进展：

【本地线索】
- 笔记：
- PDF / full-text：
- 需要补核验：
```

##### 本地文献笔记

```md
Abstract & Content & Introduction

【原文】
...

【译文】
...

【解读】
...
```

### 章节推进链

```md
Section N：章节名

Paragraph M：段落标题

【作用】：一句话...

Paragraph M+1：段落标题

【作用】：一句话...

...
```

### 段落推进链

```md
Paragraph N：短标题

【作用】：一句话...

【段落主线】：关键词 A -> 关键词 B -> 关键词 C -> 下一段入口。

【桥接句】：...
```

### 引文先行关键词链

```md

Paragraph N：短标题

【作用】：...

【段落主线】：...

【关键词链】：
- 中文关键词 A -> 中文关键词 B（关系类型）：
  [[1("complete original quotation, preferably 20-40 words")]](#ref1)
  [[2("complete original quotation from a different core-pool reference, preferably 20-40 words")]](#ref2)。

- 中文关键词 C -> 中文关键词 D（关系类型）：
  [[3("complete original quotation, preferably 20-40 words")]](#ref3)
  [[4("complete original quotation from a different core-pool reference, preferably 20-40 words")]](#ref4)。

【桥接句】：...
```

### 参考文献条目

```md
<a id="ref1"></a>[1] Author A, Author B, and Author C, *Journal Name* **Volume**, page-or-article-number (Year).  
[Paper Title](https://doi.org/xxxxx).
```

### 正文草稿

正文草稿不得包含原文引文；原文引文只保留在 `【关键词链】` 中。

```md
Paragraph N：短标题

【正文草稿】：
...

【逐句对照】：
- S1：关键词关系：[4,17]
- S2：关键词关系：[4,18]
- S3：桥接功能：[ref]

【衔接检查】：
- 上承：
- 本段收束：
- 下启：

【用语校准】：
- 中文语料借鉴：
- 避免的表达：

【写入状态】：
等待用户审阅；未获明确“写入/可以写入/同意”前，不修改目标文档。
```





