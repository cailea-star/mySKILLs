---
name: introduction-writing
description: Build, diagnose, restructure, evidence-map, and draft academic or technical introductions, especially proposal/opening-report introductions, using an authoritative reference pool, section/paragraph progression chains, keyword-relation networks, and verifiable citation evidence. Use when the user asks to write or revise an introduction, 开题报告, research background, literature-status section, paragraph logic, keyword chain, paragraph-by-paragraph reference additions, citation plan, or reference-grounded draft.
---

# Introduction Writing

This skill turns a research topic, existing draft, local literature notes, and authoritative references into a coherent introduction or opening-report structure.

The practical model is:

```text
Introduction / 开题报告前置部分 =
core reference pool
+ section progression chain
+ paragraph progression chain
+ paragraph function and keyword-relation network
+ critical comparison with standard reviews
+ verifiable citation evidence
+ approval-gated write-in
```

Core principle:

```text
References constrain the field logic.
Keywords form paragraphs.
Keyword relations form paragraph logic.
Paragraph functions form sections.
Section progression forms the document.
Citations verify each claim.
```

In working scaffolds, use `【关键词链】` for paragraph-level keyword work. It is not a keyword list; it is a concept-relation chain. Each item should state a relation such as background, definition, causal, evidence, limitation, method, validation, transition, or application:

```text
Concept A -> Concept B（relation type）：claim sentence + verifiable evidence.
```

## When To Use

Use this skill when the user wants to:

- Write, revise, or diagnose an introduction.
- Build or refine a 开题报告 / proposal background.
- Structure sections such as 选题背景及意义, 国内外发展现状与趋势, 研究内容与预期目标, 研究方法与可行性.
- Turn literature notes into paragraph logic.
- Search paragraph-level or keyword-level references.
- Compare a draft against authoritative review logic.
- Add verifiable citation evidence to claims.
- Develop a paragraph one step at a time with user approval.

## Source Policy

For nuclear physics, unless the user changes it, use this default authoritative pool:

```text
RMP / PPNP / ARNPS / PR / NRP / PRL / PLB
```

Always preserve the user's preferred abbreviations. If an abbreviation is ambiguous, state the assumed meaning or ask briefly.

Use this priority order for evidence discovery:

1. Existing project files and local reference notes.
2. Local notes for the active field, method, or paragraph keywords, especially Abstract, Contents, Introduction, and project-specific 解读 / 可直接用于开题报告 sections.
3. Specific key chapters inside local notes if the paragraph is method-heavy or evidence-heavy.
4. Original papers, local full-text extracts, Zotero full text, or publisher pages cited by the local notes.
5. External authoritative search when local evidence is missing, too indirect, outdated, contradicted, or when the user asks for a stronger reference pool.

When using external/current information, verify rather than relying on memory.

Citation evidence rule:
- Treat local `.md` reading notes as discovery aids, not as final original evidence, unless the user explicitly asks to cite notes.
- For verifiable citation labels, use original evidence clauses or short sentences checked against original article text, trusted local full-text extracts, Zotero full text, or publisher pages.
- A citation label must verify the claim relation, not merely repeat a topic word. Before accepting a citation, ask what relation it proves: definition, cause, decomposition, limitation, evidence, method, validation, or application.
- Prefer syntactically complete clauses/sentences that show why the claim is true. Avoid evidence labels that only name the field, observable, method, or paper title.
- Avoid weak keyword-only labels such as `("Q-value")`, `("Fine structure")`, or `("Shape coexistence in nuclei")`, unless the claim is only naming or defining that term.
- Keep in-text citation labels concise but meaningful, usually a complete clause or sentence fragment of about 15-25 words; if the user explicitly asks for fuller verification and source/copyright rules allow, 20-40 word evidence sentences can be used, especially in the evidence map.
- If only a paraphrase is available, mark it as paraphrase instead of formatting it as a direct quote.
- Use the smallest complete evidence unit that verifies the claim, and do not overquote.

## Mandatory Reference Re-Read

Before any new paragraph-chain proposal, keyword-chain proposal, paragraph rewrite, citation mapping, or document modification:

1. Re-read the relevant local project references for the active paragraph or section.
2. State briefly which references were consulted and what claims they support.
3. Do not present claims as authoritative unless they are supported by freshly checked local notes or newly verified sources.
4. For reference additions, produce the verified mapping required in Gate 8 before write-in.

This applies even if similar references were read earlier in the conversation.

## Approval And Write-In Rule

Before modifying the target document, get explicit user approval for the relevant structure, paragraph reference pool, or evidence map. Keep edits scoped to the approved section or paragraph, preserve useful existing structure, and avoid rewriting unrelated material.

## Main Workflow

### Gate 0: Title And Reference Pool

First establish:

```text
Title / working title:
Genre: research paper / thesis / opening report / proposal / review / presentation
Target document path, if any:
Authoritative reference pool:
Local reference-note directory:
```

If the user already has a draft or opening-report document, read that first. Do not assume the task starts from a blank page.

From the title, extract 2-5 core keywords. Use them to search or inspect the reference pool.

Recommend an initial set of references, grouped by role:

```text
Main review:
Method review:
Experimental or phenomenological evidence:
Foundational / original theory:
Recent important progress:
```

Ask the user to confirm the initial reference set before building the global structure, unless the user explicitly instructs you to proceed with an already accepted local reference set.

### Gate 1: Build Local Reference Notes

For user-confirmed references, create or use local notes. Standard note structure:

```text
## Abstract

### English
...

### 中文
...

### 解读
...

## Contents

| English | 中文 | 解读 |
| --- | --- | --- |
| ... | ... | ... |

## Introduction

### Paragraph 1: English
...

### Paragraph 1: 中文
...

### Paragraph 1: 解读
...
```

For long or method-specific references, add key-section notes only when needed:

```text
## Key Section: [section title]
English / paraphrase:
中文:
解读:
可用于开题报告:
```

Respect copyright. Prefer short quotes, compressed paraphrases, and interpretive summaries unless the source text is user-provided or openly reusable.

### Gate 2: Section Progression Chain

Before paragraph details, design 3-4 major sections or document units.

For opening reports, a common chain is:

```text
选题背景及意义
→ 国内外发展现状与趋势
→ 研究内容与预期目标
→ 研究方法、技术路线与可行性
```

For each section, produce:

```text
Section N: [name]
【作用】：...
【章节主线】：A -> B -> C -> D
出口压力：因此下一节必须说明...
```

Get user approval before moving to paragraph chains.

### Gate 3: Section-Level Paragraph Progression

Work one section at a time. For the active section, propose paragraph units before writing them.

Use this format:

```text
Section N: [name]

Paragraph X：短标题
【作用】：本段在本节和全文中的功能。
【段落主线】：关键词/概念 A -> B -> C -> D。
【桥接句】：本段如何自然引向下一段。
```

After presenting a section skeleton, remind the user:

```text
是否需要我重新阅读核心参考文献池，对这个章节骨架做一次优化和批判？
```

If the user agrees, re-read the relevant core references and compare the proposed chain with the standard review logic.

### Gate 4: Paragraph Keyword Chain

After the section paragraph chain is accepted, work paragraph by paragraph.

For each paragraph, use the Paragraph scaffold template below.

Keyword rules:

- Keywords should be semantic units, not decorative terms.
- Each keyword relation should state a real relation: background, definition, causal, evidence, contrast, limitation, transition, method, validation, or application.
- A paragraph may have network-like internal relations, but it must have one dominant paragraph logic.
- Avoid turning a paragraph into a literature list.
- Use the heading `【关键词链】`, not `【内部关键词】`, unless the user explicitly asks for the older wording.
- Treat the keyword chain as a concept-relation chain. Each bullet should contain `A -> B（relation type）：claim`, so the later prose can be written by following the claim sequence.

Apply the Approval And Write-In Rule before writing the paragraph block into the document.

### Gate 5: Critical Comparison With Standard Reviews

After a section or a paragraph group is drafted as structure, compare it with the logic of authoritative reviews.

Check:

```text
- Is the concept order standard?
- Are method categories in the accepted field order?
- Are background, status, gap, research content, and method sections clearly separated?
- Are any claims too broad for the selected references?
- Are important terms missing or nonstandard?
- Are there repeated paragraphs or repeated claims?
- Does each paragraph create a reason for the next paragraph?
```

For method/status sections, extract the standard progression from review papers. Example pattern:

```text
General formalism
→ empirical/systematic methods
→ microscopic mechanism
→ fine structure / diagnostic observables
→ deformation / coupled-channel or modern trend
```

Report suggested changes before editing.

### Gate 6: Document Write-In

When editing an existing document, apply the Approval And Write-In Rule. Do not remove user-added material unless explicitly asked or clearly replaced by an approved version.

For Markdown opening-report drafts, keep the working scaffold visible if the user is still developing structure:

```text
【作用】
【段落主线】
【关键词链】
【桥接句】
```

When the user later requests formal prose, convert the scaffold into polished paragraphs.

### Gate 7: Paragraph-Level Reference Planning

After paragraph function and keyword chains are accepted, search references paragraph by paragraph.

Use the user's preferred policy. Default:

```text
1. Read the accepted paragraph function, paragraph line, and keyword chain.
2. Use local notes and project files to locate candidate references and cited originals; follow the Citation evidence rule for final citation labels.
3. Search the external authoritative pool when local/original evidence is missing, too indirect, outdated, contradicted, or insufficiently authoritative.
4. Recommend a 3-4 paper reference pool before write-in unless the user requests a different density.
5. Apply the Approval And Write-In Rule.
```

Use this output format:

```text
Paragraph N：
核心命题：
需要支撑的关键词：
候选参考文献池（3-4 篇）：
本地线索：
需要外部补充的文献类型：
拟引用位置：
写入状态：等待用户确认
```

Reference roles:

```text
Main review: supports the paragraph's broad framing.
Topic support: supports a specific mechanism, observable, or method category.
Experimental/method evidence: supports data interpretation or computational route.
Foundational/original theory: supports formalism or historical source.
```

### Gate 8: Keyword-Level Evidence Mapping

For high-stakes or closely argued paragraphs, map evidence to each keyword-chain relation.

After the user accepts the paragraph reference pool, first produce a compact verification map:
```text
已核对文献：
- Reference -> supported keyword/claim -> original/full-text quote source or source type -> evidence clause/sentence -> planned citation position.
```

Use this format:

```text
【关键词链】：
- A -> B（关系类型）：claim sentence[[1("complete evidence clause or short sentence")]](#ref1)。
- C -> D（关系类型）：claim sentence[[2("complete evidence clause")]](#ref2)[[3("complete evidence clause")]](#ref3)。
```

Evidence rules:

- Follow the Citation evidence rule.
- Map citations to keyword relations, not just to broad topics.
- Place each citation where it supports the claim.
- Each mapped quote should make the claim relation verifiable, such as cause, definition, mechanism, limitation, evidence, method, validation, or application.
- Reject or flag weak evidence that merely repeats a topic word, paper title, observable name, method name, or broad field label without supporting the relation in the claim.
- Record whether the evidence came from publisher abstract/page, local full-text extraction, Zotero full text, or an original PDF when that distinction matters for verification.

### Gate 9: Pre-Prose Audit / 正文化前审查

Before converting a scaffold into formal prose, audit the accepted section or whole draft. Report suggested changes before editing unless the user explicitly asks for direct revision.

Check:

```text
- Repetition: Are paragraph roles distinct, or do adjacent paragraphs restate the same claim?
- Citation density: Does each paragraph keep a readable balance, usually 2-4 core references in prose even if the scaffold contains denser verification?
- Weak citations: Are any citation labels keyword-only, title-only, or only topic-matching rather than relation-supporting?
- Terminology: Are symbols, translated terms, and method names used consistently across paragraphs?
- Old fields: Are stale scaffold fields such as 【内部关键词】, unapproved 【一句话】, obsolete paragraph numbers, or removed concepts still present?
- Section boundaries: Are background, method status, research content, and concrete calculation workflow kept separate?
- Bridge logic: Does each paragraph create a real need for the next paragraph?
```

For nuclear-physics introductions, also check common terminology drift such as `Qα/Q_α`, `Tα/T_α`, `Schrödinger/Schrodinger`, `formation amplitude/formation probability`, and `耦合道方法/通道耦合`.

### Required Output Templates

Use these exact templates when the user asks for scaffolded writing, reference lists, or verifiable citations.

Paragraph scaffold:

```md
#### Paragraph N：段落标题

【作用】：本段在本节和全文中的功能。

【段落主线】：概念 A -> 概念 B -> 概念 C -> 研究问题/下一段入口。

【关键词链】：
- A -> B（关系类型）：解释句。
- B -> C（关系类型）：解释句。
- C -> D（证据/转化/局限/方法关系）：解释句。

【桥接句】：本段如何自然引向下一段。
```

Reference-list entry:

```md
<a id="ref1"></a>[1] Author A, Author B, and Author C, *Journal Name* **Volume**, page-or-article-number (Year).  
[Paper Title](https://doi.org/xxxxx).
```

For newly added references, verify and include a DOI link whenever one is available. If no DOI can be found, use the most authoritative stable publisher, arXiv, or journal URL and note that DOI was not found during verification if relevant.

Verifiable citation and placement:

```md
[[1("complete evidence clause or short sentence")]](#ref1)
重核尤其是超重核能否具有可观测寿命，取决于壳效应和形变壳隙能否提供足够的额外稳定性[[1("provide added stability and allow nuclei around these regions to have observable half-lives")]](#ref1)。
α 衰变链是研究未知超重核区域的重要观测入口[[1("identified through α-decay chain analysis")]](#ref1)。
```

Placement rules:

- For a single-sentence claim, put citations at the sentence end before the period.
- For multiple citations supporting the same sentence, place them consecutively before the period.
- For clauses supported by different references, place the citation immediately after the clause it supports.
- Keep the quoted evidence in the citation exactly long enough to verify the claim relation, not just the topic.
- Do not use ambiguous keyword-only quotes when a complete supporting clause is available.
- If the user asks for conventional final-paper citation style, convert this verification format into normal numeric citations later.

## Drafting Formal Prose

Only draft full prose after structure and citation plan are accepted, unless the user explicitly asks for a direct draft.

When drafting:

- Follow the accepted section chain.
- Follow the accepted paragraph chain.
- Preserve paragraph function.
- Use accepted keyword-chain relations as sentence logic.
- Keep paragraph transitions visible but not mechanical.
- Use citations where the evidence mapping says they belong.
- Avoid writing an encyclopedia-style background.
- Avoid chronological literature lists unless the paragraph function is historical.

## Diagnosis Checklist

Before finalizing or after major revisions, check:

```text
- Does every section have a distinct role?
- Does every paragraph have a distinct role?
- Does each paragraph make the next paragraph necessary?
- Are background, status, gap, goal, and method separated?
- Are repeated claims merged or redistributed?
- Are important keywords introduced before they are used?
- Are method categories ordered according to standard reviews?
- Are terms standard for the discipline?
- Do references support claims rather than merely matching keywords?
- Do citation labels contain complete evidence clauses/sentences when the claim is argumentative?
- Are newly added reference-list entries checked for DOI or another stable authoritative URL?
- Are citations placed before punctuation when they support one sentence?
- Is the final research objective specific and reachable?
```

## Compact Operating Formula

When in doubt, use this operating loop:

```text
Read local references
→ propose/compare/revise structure
→ get approval and write scaffold if requested
→ discover candidate references from notes and originals
→ verify complete evidence clauses or short sentences
→ recommend a 3-4 paper paragraph pool
→ get approval, map evidence, and write citation support
→ draft final prose only when requested
```

## Common Failure Modes To Avoid

Avoid:

- Starting from prose before the reference pool and paragraph chain are stable.
- Treating all keywords as equally important.
- Mixing research background with method review.
- Mixing research content with concrete calculation workflow.
- Citing papers only because they mention the topic.
- Using keyword-only citation labels for argumentative claims.
- Citing project `.md` reading-note prose as if it were original article text.
- Writing any scaffold, citation support, or prose before the required approval.
- Skipping the standard-review comparison step.
- Using long quotes in citation labels when a smaller complete evidence clause would verify the claim.
- Placing sentence-level citations after the period when the user wants citation before punctuation.

