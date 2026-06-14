---
name: introduction-writing
description: Build and revise academic or technical introductions and opening reports with quote-first keyword chains, confirmed core reference pools, verified original quotations, section/paragraph progression, approval-gated write-in, and prose drafting. Use when working on 开题报告, research background, introduction structure, literature evidence, keyword chains, quote-based evidence mapping, paragraph-by-paragraph reference support, or formal prose from verified quotations.
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
- Support each keyword chain with original quotations from at least two different references in the confirmed core reference pool.
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

- Each keyword relation must have original quotations from at least two different references in the confirmed core reference pool.
- Each quotation must prove a relation: definition, cause, decomposition, limitation, evidence, method, validation, transition, or application.
- Each quotation must be a complete viewpoint-bearing clause or sentence, not a noun phrase, title fragment, topic label, or isolated term.
- Reject weak evidence such as `("Q-value")`, `("Fine structure")`, `("important probe")`, or `("Shape coexistence in nuclei")` unless the relation is only naming.
- Mark paraphrase as paraphrase. Do not format paraphrase as direct quote.
- Use the smallest complete quotation set that supplies enough original wording for later prose. Do not overquote.

Mandatory re-read before any new chain, review, prose, or write-in:

1. Re-read the active paragraph or section.
2. Re-read the confirmed core reference pool, using local notes only to locate original evidence.
3. State briefly which core references were consulted and which keyword relations their original quotations support.
4. Do not mark a relation `ready` unless it has strong original quotations from at least two different core-pool references.

Evidence status:

```text
ready = 2+ strong original quotations from different core-pool references
needs_core_second_source = only one core-pool reference verified
supplemented_not_ready = one core-pool reference plus non-core support
paraphrase_only = no verified original quotation
weak_quote = quotation incomplete or topic-only
conflict_check = core references frame the relation differently
```

## 3. 七步工作流

### Gate 1：题目与核心参考文献池

Establish the working title, genre, target document, research object, and active section/paragraph. Extract 2-5 core keywords from the title and draft. Confirm the active core reference pool before building structure or quote-chains.

Output:

```text
title / genre / target document
active section or paragraph
core keywords
confirmed core reference pool by role
```

### Gate 2：本地文献笔记建立与使用

Inspect local notes, PDFs, full-text extracts, and reference lists for the confirmed core pool. Use the active project's existing note style when it is already clear. When creating or normalizing notes, prefer the minimal three-part structure `原文 / 译文 / 解读`; keep metadata such as source, DOI, arXiv, page, section, or evidence status only as brief traceability lines, not as extra analytical sections.

Build or update local notes only when needed to locate original evidence. In each note, make the evidence status explicit: original full-text extraction, normalized full-text extraction, compressed paraphrase, focused reading note, or interpretation. Local notes remain discovery aids unless the relevant passage is explicitly verified against original article text, trusted full-text extraction, Zotero full text, or a publisher page.

Output:

```text
local note paths
available 原文 / 译文 / 解读 blocks
original evidence source paths or URLs
candidate sections for quotation extraction
```

### Gate 3：章节推进链

Design section-level progression before paragraph detail. For each section, state function, main conceptual progression, and exit pressure: why the next section is required.

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

1. Read the target paragraph's current wording.
2. Extract Chinese keyword relations as `中文 A -> 中文 B（关系）`.
3. For each relation, search the confirmed core reference pool for original quotations.
4. Require at least two different core-pool references per relation.
5. Prefer 20-40 word complete argumentative quotation units.
6. Reject weak, topic-only, phrase-only, or paraphrase-only evidence.
7. Compare the draft wording with the authoritative original wording.
8. Build candidate quote-first keyword chains with evidence status.
9. Wait for user review before write-in.

Do not reduce chain count merely for concision during corpus-expansion passes. Preserve the user's chain granularity and increase original quotation diversity.

### Gate 6：与权威综述逻辑对照

Compare the accepted section, paragraph, or quote-chain against standard review logic.

Check:

- concept order standardness
- missing standard terms or categories
- overbroad or overstrong relations
- repeated relations across adjacent paragraphs
- method/status/background boundary confusion
- relation conflicts across core references
- whether each paragraph creates a reason for the next paragraph

For nuclear-physics method/status sections, default comparison pattern:

```text
general formalism
-> empirical/systematic methods
-> microscopic mechanism
-> fine structure / diagnostic observables
-> deformation / coupled-channel or modern trend
```

Report suggested changes and wait for user approval before write-in.

### Gate 7：正文化前审查

Before drafting formal prose, audit the accepted structure and quote-chains.

Require:

- each keyword chain is `ready`
- each `ready` chain has 2+ core-pool original quotations
- quotations are complete viewpoint-bearing units
- no Chinese secondary claim is treated as evidence
- no local note paraphrase is treated as original quotation
- terminology is consistent across paragraphs
- citations and quote sources are traceable
- paragraph roles and bridge logic remain distinct

If any check fails, return a problem list instead of drafting prose.

## 4. 审阅后写入与正文化

There is no separate write-in Gate. Every Gate may write only after user approval.

Write-in rules:

- Get explicit user approval before modifying the target document.
- Write only the current Gate's approved content.
- Preserve useful existing structure unless the user approves replacement.
- Never write single-source, weak-quote, paraphrase-only, or unreviewed quote-chains as final chains.
- For quote-chain write-in, require `ready` status.

Draft formal prose only after Gate 7 passes or the user explicitly asks for a direct draft.

Prose rules:

- Draft from accepted quotation sets, not from Chinese secondary explanations.
- Follow accepted section and paragraph progression.
- Preserve paragraph function.
- Use quotation-supported relations as sentence logic.
- Keep transitions visible but not mechanical.
- Avoid encyclopedia-style background and chronological literature lists unless the paragraph function requires them.
- Convert verification-style quotation evidence to conventional citation style only when the user asks.

## 5. 检查与失败模式

Diagnosis checklist:

- Does every section and paragraph have a distinct role?
- Does each paragraph make the next paragraph necessary?
- Are background, status, gap, research content, and method workflow separated?
- Does each quote-first keyword chain have 2+ different core-pool original quotations?
- Does each quotation contain a predicate and independently express the relation?
- Are local notes used only as discovery aids?
- Are all quotation sources traceable to original text, trusted full-text extraction, Zotero full text, or publisher pages?
- Are terminology and symbols consistent, e.g. `Qα/Q_α`, `Tα/T_α`, `Schrödinger/Schrodinger`, `formation amplitude/formation probability`, `耦合道方法/通道耦合`?
- Are repeated relations merged, redistributed, or justified?
- Is the final research objective specific and reachable?

Failure modes:

- Writing Chinese explanatory claims inside quote-first keyword chains.
- Using keyword-only quotation labels as evidence.
- Treating local reading-note paraphrase as original quotation.
- Accepting one core-pool source as final evidence for a chain.
- Using one core-pool source plus non-core support as `ready`.
- Reducing chain count when the user requested corpus expansion.
- Writing prose before quote-chains pass review.
- Citing papers because they mention a topic rather than prove the relation.
- Overquoting beyond the smallest complete argumentative unit.
- Placing sentence-level citations after punctuation when the user wants citation before punctuation.

## 6. 模板

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
