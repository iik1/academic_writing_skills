---
name: accounting-review-writing-style
description: >
  Journal-specific writing conventions for The Accounting Review (TAR)
  (ABS 4*, ACCOUNT). Use alongside account-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for The Accounting
  Review", "submit to TAR", "match Accounting Review style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: The Accounting Review

## Journal Profile
- **ABS 2024 Rating:** 4*
- **Field:** ACCOUNT
- **Publisher:** American Accounting Association (AAA)
- **Scope:** High-quality empirical, experimental, and analytical research across all accounting disciplines (financial reporting, auditing, taxation, management accounting, accounting information systems). Dominant quantitative/archival/experimental tradition.
- **Guidelines URL:** https://aaahq.org/Research/Journals/Manuscript-Preparation-Guide
- **Field baseline:** account-field-writing-style
- **Articles spot-checked:** 0 (AAA publications portal returned 403; guidelines are the primary authoritative source)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Required manuscript order: AI disclosure statement → text beginning with "I. INTRODUCTION" → References → Numbered figures (captions only) → Numbered tables → Exhibits → Appendices. Title page submitted as a separate Word document. [ENFORCED]

### Length
55 pages maximum, inclusive of references, figures, tables, and appendices. [ENFORCED]

### Abstract
Unstructured paragraph, maximum 150 words. Appears at the start of the article file (without author names). Must convey topic, methods, and findings. [ENFORCED]

### Citations
Author–date, no comma: "(Berry 2003)" not "(Berry, 2003)". Two authors: "(Fehr and Schmidt 2003)". Three-to-five authors: all names listed with "and". Six or more: "First author et al." Journal titles not abbreviated in reference list. DOIs or online links required when available. [ENFORCED]

### Headings
Four levels, all explicitly formatted:
- **Level 1:** Centered, bold, ALL CAPS, Roman numeral (I. INTRODUCTION, II. HYPOTHESIS DEVELOPMENT, …)
- **Level 2:** Flush left, bold, Mixed Case
- **Level 3:** Flush left, bold, italic, Mixed Case
- **Level 4:** Paragraph indent, bold, lowercase

[ENFORCED]

### Tables and Figures
- Each table/figure must be directly mentioned in the text before it appears.
- No "Insert Table X here" callouts.
- Tables built with Word table editor or Excel only (not keyboard-formatted with tabs/spaces).
- Figures provided as separate files at final submission; preferred format EPS; must be interpretable in grayscale (600 dpi for line art, 264 dpi for halftones).
- Alt-text required for all tables, figures, exhibits, and graphics.

[ENFORCED]

### Equations
Numbered consecutively in parentheses flush with the right-hand margin. Mathematical notation must use MathML, MathJax, or MathType — not Wingdings or images. [ENFORCED]

### Explicit Prohibitions
- **Single authors must not use "we"** — this overrides the FIELD_SKILL norm that "we" is used regardless of author count. Single-authored papers must use "I" or impersonal constructions.
- No direct or indirect author self-identification in anonymous review copy.
- AI may not be listed as co-author or cited as a source.
- No links to author websites or cloud storage for supplemental materials — everything must be submitted at time of submission.
- People's likenesses require express permission.
- Footnotes must contain textual information only — no citations in footnotes.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Voice and Register

**Field norm:** "We" is the dominant convention regardless of author count.

**TAR rule:** Single-authored papers must use "I" (or impersonal constructions) — "we" is explicitly prohibited for single authors. Multi-author papers follow the field norm and use "we."

**Classification:** ENFORCED — stated in guidelines and historically practiced at AAA journals.

### Structural Deviations

**Field norm:** FIELD_SKILL does not specify an AI disclosure section or its placement.

**TAR rule:** A "Declaration of Generative AI and AI-Assisted Technologies in the Writing Process" is required immediately after the abstract and before the introduction — even if no AI was used (in which case authors state that no AI was used). The declaration specifies tools, extent of use, and reasons for use.

**Classification:** ENFORCED

**Field norm:** FIELD_SKILL specifies heading conventions for L1 (Roman numerals, ALL CAPS) but not L2–L4.

**TAR rule:** All four heading levels are specified (see Hard Constraints above). L2 is flush left/bold/mixed case; L3 adds italic; L4 is indented with lowercase bold.

**Classification:** ENFORCED

### Statistical Reporting

**Field norm:** FIELD_SKILL mentions that robustness checks and economic significance are expected; it does not specify experimental reporting requirements at this level of detail.

**TAR rule:** For experimental papers, three reporting requirements are mandatory: (1) standard deviation and cell sizes in all tables of means; (2) degrees of freedom reported alongside every test statistic; (3) complete ANOVA, MANOVA, and ANCOVA tables including all estimated terms and the error term.

**Classification:** ENFORCED

### Citation Density

Follows FIELD_SKILL norm.

### Other Journal-Specific Patterns

**Footnotes:** Footnotes must contain textual information only — citations must appear in-text, never in footnotes. This means the typical practice of footnoting tangential references (common in some sub-fields) is not permitted. [ENFORCED]

**Number style:** Spell out one through ten in text; use numerals for 11 and above. Use "percent" in text prose; use "%" in tables and figures. [ENFORCED]

---

## Dimensions With No Delta

- Voice register (formal, clinical, active): FIELD DEFAULT
- Introduction rhetorical structure (CARS model, enumerated results, explicit contribution): FIELD DEFAULT
- Methods tense (past throughout): FIELD DEFAULT
- Results organization by hypothesis in parallel with hypothesis development: FIELD DEFAULT
- Limitations paragraph in conclusion: FIELD DEFAULT
- Hedging calibrated to identification strength: FIELD DEFAULT
- Paraphrase over quotation: FIELD DEFAULT
- Causal language reserved for exogenous identification: FIELD DEFAULT
- Descriptive statistics table as near-universal element: FIELD DEFAULT

---

## Common Pitfalls

1. **Single-authored paper uses "we"** — Explicitly prohibited. Use "I" or impersonal constructions ("this paper examines…"). This is the most commonly overlooked TAR-specific constraint for sole-authored work.

2. **AI disclosure omitted** — Required even when no generative AI was used. The declaration must be placed between the abstract and the introduction; omitting it is a non-compliant submission.

3. **Citations in footnotes** — TAR footnotes are for textual elaboration only. References to prior literature must appear in-text. Relocating footnote citations to the body is required.

4. **Experimental papers missing complete ANOVA tables** — TAR requires all estimated terms including the error term. Reporting only the F-statistics of interest is insufficient; incomplete ANOVA tables are a common desk-reject trigger for experimental submissions.

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
| Source | Type | Access |
|--------|------|--------|
| https://aaahq.org/Research/Journals/Manuscript-Preparation-Guide | Guidelines (AAA-wide, authoritative for TAR) | Direct fetch |
| https://aaahq.org/Research/Journals/The-Accounting-Review | Journal submission page | Direct fetch |
| TAR full-text articles | Not accessed (AAA publications portal returned 403 for all attempts) | N/A |