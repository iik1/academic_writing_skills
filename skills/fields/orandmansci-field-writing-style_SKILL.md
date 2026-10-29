---
name: orandmansci-field-writing-style
description: >
  Normative academic writing conventions for the OR&MANSCI field,
  derived exclusively from ABS 4* and ABS 4 journals. Use this skill
  as a baseline prior when writing for any journal in the OR&MANSCI field.
  Trigger on phrases like "write for a OR&MANSCI journal", "what does
  OR&MANSCI writing look like", "field norms for OR&MANSCI", or when a
  journal-specific skill references this baseline. Superseded by
  journal-specific skills where they conflict.
---

# Field Writing Style: OR&MANSCI

## Scope and Intended Use

This baseline captures the shared writing conventions of ABS 4* and ABS 4 journals in the Operations Research and Management Science (OR&MANSCI) field. It covers macro structure, voice, argumentation, methods conventions, citation norms, and hedging patterns as observed across the field's leading outlets.

It does NOT cover journal-specific formatting requirements, word or page limits, submission checklists, publisher templates, or statistical reporting rules mandated by individual journals. Journal-specific skills take precedence when they conflict with this baseline.

The OR&MANSCI field spans a spectrum from purely theoretical/mathematical contributions to empirically grounded computational and applied work. Some conventions differ modestly across this spectrum; where they do, the range is noted.

---

## Typical Article Structure

Leading journals in this field expect a clear, standardised structure. The near-universal section set, in canonical order, is:

1. **Abstract** — brief statement of problem, approach, and main finding
2. **Introduction** — motivation, gap identification, contributions, paper roadmap
3. **Model / Preliminaries / Framework** — formal problem setup and notation
4. **Main Analysis** — theorems, algorithms, or empirical methodology (may be split across multiple numbered sections organised by topic)
5. **Results / Experiments / Numerical Study** — formal results, proofs (or proof sketches), computational validation
6. **Conclusion** — synthesis, limitations, future directions
7. **References**
8. **Appendix / Online Supplement** — full proofs, robustness checks, additional experiments

**Related Work** is almost always present but its placement varies: it appears either as a dedicated subsection of the Introduction (more common in Management Science-style papers) or as a standalone section immediately after the Introduction (more common in theoretically focused papers). A separate, free-standing Discussion section is rare; interpretive discussion is typically woven into the Results sections or folded into the Conclusion.

Appendices are near-universal in ABS 4*/4 work and serve a distinct function: complete proofs and extensive robustness tables are routinely moved there to maintain readability in the main body. Reviewers in this field expect main-body theorem statements and empirical findings to be self-contained, with the appendix providing the full evidentiary detail.

---

## Voice, Person, and Register

At the ABS 4*/4 level, reviewers expect consistent use of **first-person plural** ("we"). The authorial "we" appears throughout — in problem framing, contribution claims, algorithmic descriptions, and interpretation of results. Impersonal or third-person constructions are reserved for definitional passages ("let X denote…") or when describing prior work ("prior work shows…").

**Active voice dominates.** Passive constructions appear selectively: in formal theorem statements, when describing procedures that logically require objectivity ("samples are drawn from…"), and when attributing results to prior literature. The overall register is formal, precise, and technically dense.

The field's formality is high and consistent across sections. Colloquial language, rhetorical questions addressed to the reader, and motivational narrative flourishes are generally absent after the opening paragraphs of the Introduction.

---

## Sentence and Paragraph Style

Sentences are typically medium to long, with technical and mathematical content integrated directly into prose. Short emphatic sentences are rare and tend to appear only to foreground a key result. Paragraphs are moderately dense: each makes a single logical move but typically sustains that move for several sentences before transitioning.

Mathematical notation is woven into running text throughout the paper — this is a field-wide norm, not a feature of any single subgenre. Readers are expected to process formal notation fluently. Unnecessary paraphrase of mathematical content into plain language is avoided; instead, authors offer brief intuitive "sketch" remarks immediately following formal statements, particularly for major theorems.

---

## Argumentation and Rhetorical Moves

The Introduction follows a structure consistent with the CARS (Create A Research Space) model, executed with field-specific precision:

1. **Establish the territory**: The opening situates the problem in a practically or theoretically significant domain. This is typically brief — one to three paragraphs — and often cites foundational or recent high-profile work to anchor the relevance claim.

2. **Identify the gap**: The authors identify a specific limitation of existing work — a missing assumption, an unanalysed regime, an open question, or a condition under which prior methods fail. The gap is stated precisely, often in technical terms, not in vague "little is known" language. Prior work is acknowledged respectfully and its achievements credited before its limits are noted.

3. **Occupy the niche (state contributions)**: Contributions are stated explicitly and usually collected in a dedicated paragraph or subsection. At the ABS 4*/4 level, reviewers expect contributions to be stated as enumerated claims, each claim asserting something specific and verifiable (a theorem, a bound, an algorithm with a guarantee, an empirical finding). Vague or broadly framed contribution statements are atypical.

4. **Paper roadmap**: The Introduction closes with a brief roadmap — one paragraph or a short list — that maps sections to contributions.

Papers do not open with rhetorical grand claims about the importance of OR generally; they move quickly to the specific problem. The gap is typically framed as a gap in formal analysis or theoretical understanding, not merely as a gap in the applied literature.

At the paper's close, the Conclusion reconnects findings to the gap stated in the Introduction, provides a clear summary of what was established, acknowledges limitations of the framework or model, and typically closes with explicit pointers to future research directions.

---

## Methods Conventions

Leading journals in this field expect **high procedural and formal detail**. The methods section (or model section) is expected to be fully self-contained: all notation introduced here should be consistent with what appears in proofs and results.

Tense conventions follow a consistent pattern:
- **Present tense** for problem setup, model definitions, and algorithmic descriptions ("the algorithm selects…", "we define…")
- **Past tense** for reporting experimental execution and empirical estimation steps ("we estimated…", "we trained the model on…")
- **Present tense** for theorem statements and mathematical properties, regardless of when they were derived

The expected level of procedural detail is high. Algorithms are typically presented with pseudocode or formal step-by-step notation. Assumptions are stated explicitly and numbered. Conditions for results are stated with precision.

For theoretical papers, robustness is demonstrated through corollaries and extensions that relax assumptions, through numerical experiments that validate theoretical bounds, or through appendix sections comparing performance across parameter configurations. For empirical papers, robustness is demonstrated through alternative specifications, sensitivity analyses, or placebo/falsification exercises. Reviewers in ABS 4*/4 outlets expect robustness evidence to be substantive, not pro forma.

---

## Results and Reporting Norms

The boundary between reporting and interpretation differs by subgenre:

- In **theoretical papers**, results are formal theorem or proposition statements. Prose interpretation appears immediately after each major result as "remarks" or inline discussion, explaining what the bound implies or when the condition is relevant. Tables appear primarily in numerical experiment sections.
- In **empirical and computational papers**, tables are the primary vehicle for quantitative results. Prose accompanies tables to highlight key comparisons, explain statistical significance, and interpret direction of effects. Prose does not duplicate the table; it adds meaning.

Statistical narration in empirical papers is precise: specific statistics (e.g., ratio values, regret bounds, percentage improvements) are reported in prose rather than left to the reader to extract from tables. However, the narrative remains analytical — results are not merely read aloud but evaluated against the research question.

Null or mixed results are handled directly. When a method performs similarly to a benchmark or fails under a particular condition, this is reported and interpreted as informative about the model or algorithm's scope, not obscured.

---

## Discussion and Conclusion Norms

In OR&MANSCI, a separate free-standing Discussion section is the exception rather than the rule. Interpretation of findings is typically integrated into the Results sections themselves. The Conclusion section synthesises the paper's overall contribution, explicitly reconnects to the gap stated in the Introduction, and presents limitations.

Limitations are framed constructively: as boundary conditions of the model or analysis rather than as failures. Future research directions are stated explicitly and specifically — not as a generic call for more work but as identified open problems or extensions that the current framework does not yet handle.

Practice varies on whether Discussion and Conclusion are merged into one section or separated. Merged "Discussion and Conclusion" sections are common in shorter or more applied papers; longer theoretical papers sometimes keep them distinct, with Discussion synthesising across theoretical results before Conclusion closes the narrative.

---

## Citation and Literature Engagement

Citation density varies predictably by section:

- **Introduction and Related Work**: high density. The Introduction establishes scholarly territory through dense citation, with references clustered around foundational results, recent advances, and the specific gap being targeted. The Related Work subsection is systematically organised — typically by research stream rather than chronologically — and is expected to be comprehensive within the paper's scope.
- **Methods/Model sections**: moderate. Citations appear to acknowledge foundational frameworks, established algorithms, or established problem formulations that the paper builds on. Original derivations are not cited; assumptions and definitions are.
- **Results/Theorem sections**: low. Proof sections and theorem statements are largely self-referential; citations to external sources are minimal.
- **Appendix**: low to minimal.

**Direct quotation is essentially absent** from OR&MANSCI writing. All engagement with prior literature is through paraphrase, summarisation, and attribution. The field does not cite to quote; it cites to position.

Disagreement with prior work is handled diplomatically. Authors acknowledge what prior work achieves before identifying its limitations. Framing such as "while X establishes Y, it does not address Z" is normative. Adversarial framing or strong negative evaluation of prior work is rare at the ABS 4*/4 level.

---

## Hedging and Epistemic Caution

Overall epistemic caution in OR&MANSCI is **low to moderate**, but the form of caution differs substantially between subgenres:

- In **mathematical/theoretical papers**, verbal hedging (words like "might," "appears," "seems") is largely absent from claims about formal results. Uncertainty is expressed through the mathematical structure itself: probability statements, explicit assumption conditions, bounded-guarantee formulations, and scoped theorem premises. Claiming a result "under Assumption 3" is the field's idiomatic form of epistemic qualification.
- In **empirical and applied papers**, moderate hedging appears in claims about external validity and generalisation: phrases such as "in our experimental setting," "subject to the modelling assumptions," and "under the conditions studied" are common and expected. Claims are confident within the established scope, hedged at the boundary of that scope.

The phrase "to the best of our knowledge" is used specifically and sparingly — to flag the first formal treatment of a result or problem, not as a general disclaimer. Contribution claims are stated assertively; epistemic hedging does not extend to the core contribution statements.

---

## What This Baseline Does NOT Specify

The following are explicitly excluded from this baseline. They belong in journal-specific skills:

- Word limits, page limits, or column formatting requirements
- Required or prohibited section names
- Publisher-mandated formatting (referencing style, font, margins, template)
- Submission system requirements, cover letter conventions, or data availability statements
- Journal-specific statistical reporting standards (e.g., required disclosure of standard errors, specific hypothesis-testing conventions)
- Whether a separate "Data" section is expected
- Specific conventions around ethics statements or replication packages
- The balance between theory and computation expected by any specific journal
- Online supplement vs. appendix conventions specific to any journal

---

## Avoiding AI-Writing Patterns

These conventions apply regardless of field or journal. Apply them in addition to everything above; only deviate where this journal's own guidelines explicitly require otherwise.

1. **No participial result clauses.** Findings should not carry an "-ing" tail asserting an interpretation the sentence has not earned ("...rose by 12 points, highlighting the importance of enforcement"; "...underscoring the need for validation"; "...demonstrating that norms shifted"). State the finding. If the implication is worth stating, state it as its own sentence.
2. **No sentence-initial transition glue.** Do not stitch paragraphs together with "Moreover," "Furthermore," "Additionally," "Ultimately," "Overall," "In essence," "Indeed," or "That said" at the start of a sentence. Transitions belong inside the argument, not bolted onto it.
3. **Limit rule-of-three constructions.** One or two triads per paper is natural ("clear, concise, and compelling"); a triad per paragraph is a tell. Vary the structure.
4. **Replace importance-inflation words with the actual magnitude.** Avoid "crucial," "critical," "pivotal," "vital," "paramount," "invaluable," "essential" as importance markers, and "significantly" or "dramatically" as intensifiers (also statistically ambiguous). Avoid "vast," "myriad," "plethora." State the size of the effect instead of asserting its importance.
5. **Avoid the 2023-era word list.** "Delve," "explore" (as metaphor), "unpack," "navigate," "landscape," "realm," "tapestry," "journey," "harness," "leverage," "unlock," "foster," "bolster," "garner," "showcase," "boast," "seamless," "holistic," "multifaceted," "nuanced," "intricate," "interplay." Also avoid "robust" outside its statistical sense and "comprehensive" as self-description.
6. **No empty balance.** Avoid "while challenges remain," "a double-edged sword," "strikes a balance," "it is not without limitations," "both approaches have merits" — these simulate judgment without making one. Do not open more than one or two sentences per section with a concessive "While X, Y" construction.
7. **Quantify instead of gesturing.** Avoid "a number of," "various," "several key," "a range of," "numerous studies" without citations attached. Give the count or the citation.
8. **No anthropomorphised prose.** Avoid "the data tell a story," "the analysis paints a picture," "this paper seeks to," "the results speak to."
9. **No throat-clearing openers.** Avoid "In recent years, there has been growing interest in...," "With the advent of...," "In today's rapidly evolving...." Delete and start with the claim.
10. **No padding verb phrases.** Replace "serves to," "acts as," "stands as," "functions as," "is able to," "in order to," "due to the fact that," "utilize," "prior to," "commence" with their one-word equivalents.
11. **No wrap-up restatement.** A conclusion should add the implication or end — not repeat what was just said via "Taken together, these results suggest...," "In sum," or "In conclusion" followed by a restated summary.
12. **Vary rhythm.** Avoid clustering sentence lengths in a narrow band, making every paragraph roughly equal, or opening every section the same way.
13. **No interpretive adverb openers.** Avoid "Interestingly," "Surprisingly," "Notably," "Strikingly" — if the fact is surprising, the reader will notice.
14. **No chatbot leakage.** Avoid "Certainly," "Here's," "Let's examine," "we can see that," "as mentioned above" — residue from copy-pasted chat output.
15. **No em dashes.** Do not use em dashes (—) at all. Use a period, comma, colon, or parentheses instead, whichever the sentence actually calls for.
16. **No antithesis padding.** Avoid the "X, not Y" contrast construction as a rhetorical flourish ("a correlation, not a coincidence"; "a policy shift, not a technical adjustment") unless the contrast is doing real argumentative work and stated once.
17. **No hedges without content.** Avoid "somewhat," "arguably," "to some extent," "in some sense," "it could be argued," "seems to," "may potentially" when they are not carrying a specific, defensible qualification. Hedge only where the uncertainty is real and specify its source.
18. **No fillers.** Cut "basically," "essentially," "simply," "just," "really," "very," "quite," "actually" unless the sentence fails without them.
19. **No flourish labels.** Do not bold or set off rhetorical labels like "The Bottom Line:," "Key Insight:," "Takeaway:," "Bottom line," "The upshot" — state the point in the sentence itself.
20. **No self-praise.** Do not characterize the paper's own contribution as "novel," "innovative," "unique," "cutting-edge," "state-of-the-art," or "groundbreaking." Describe what it does; let the reader judge novelty.
21. **No topic-announcing openers.** Avoid "This section discusses...," "This paper will discuss...," "Let's turn to...," "We now turn our attention to...." Open with the content itself.

---

## Sources

| Journal | ABS Rating | Articles consulted |
|---------|------------|-------------------|
| Management Science | 4* | 4 |
| Operations Research | 4* | 2 |
| Mathematical Programming | 4 | 1 |
| European Journal of Operational Research | 4 | 2 |