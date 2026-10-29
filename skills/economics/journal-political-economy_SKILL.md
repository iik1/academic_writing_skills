---
skill_id: jpe-writing-style
skill_type: journal-specific
journal: Journal of Political Economy
issn: 0022-3808
publisher: University of Chicago Press
abs_rating: 4*
field: Economics
base_skill: econ-field-writing-style
created: 2026-04-12
articles_reviewed:
  - "Acemoglu & Loebbing (2026). Automation and Polarization. JPE 134(3): 1017–1072."
guidelines_accessed: false
guidelines_note: >
  All attempts to access JPE author guidelines at journals.uchicago.edu returned 403 Forbidden.
  No cached or archived version was accessible. All deltas below are classified PRACTICE ONLY
  unless independently confirmed as journal policy. No ENFORCED or GUIDELINE ONLY classifications
  are possible from this run.
---

# Journal of Political Economy — Writing Style Deltas

> This file records **only deviations** from the `econ-field-writing-style` baseline.
> Items not listed here should be treated as FIELD DEFAULT — follow the baseline.

---

## 1. Document Structure

### 1.1 Section Heading Hierarchy

**Classification: PRACTICE ONLY**

JPE uses a specific two-level heading system for the main article body:

- **Main sections**: Roman numerals — `I. Introduction`, `II. Model`, `III. Characterization of Equilibrium`, etc.
- **Subsections**: Capital letters — `A. Environment`, `B. Competitive Equilibrium`, `C. Assumptions and Motivation`
- **Appendix subsections**: Letter + number — `A1`, `A2`, `A2.1`, `A2.2`

The FIELD_SKILL baseline is agnostic on specific numbering style. JPE practice enforces Roman numeral primaries and capital-letter secondaries. Do not use Arabic numeral section numbering (e.g., `1.`, `1.1`) in JPE submissions.

### 1.2 Related Literature Placement

**Classification: PRACTICE ONLY**

The FIELD_SKILL baseline notes that standalone "Related Literature" sections are *more common in theory papers*. In JPE practice (confirmed in a theory/quantitative hybrid paper), the literature review is **fully integrated into the Introduction** as a sequence of paragraphs, with no standalone section. This is a tightening of the field norm for theory papers.

- Literature paragraphs appear after the main contribution summary and before the roadmap, occupying approximately 3 paragraphs (1–1.5 pages) within the Introduction.
- Do not create a separate "Related Literature" section.

### 1.3 Data Availability Statement

**Classification: PRACTICE ONLY** *(likely ENFORCED; could not confirm from guidelines)*

JPE requires a standalone **"Data Availability"** section, appearing as a titled section immediately **before** the References section. This is a discrete structural element, not a footnote or acknowledgment. It likely reflects journal data transparency policy aligned with AEA standards.

- Position: after Conclusion, before References
- Format: titled section ("Data Availability"), short prose or itemized statement
- Example: describes data sources, access, and any restrictions on replication materials

### 1.4 Online Appendix Structure

**Classification: PRACTICE ONLY**

JPE splits supplementary material into:

- **Appendix A**: Included in the **main published document** (proofs, derivations, extended tables)
- **Appendix B**: Designated as **"available online"** — referenced in the main text as `appendix B (available online)` but not included in the print/primary PDF

Authors should structure supplementary material with this explicit split. Online appendix is referenced in text parenthetically, not as a footnote.

---

## 2. Front Matter and Editorial Conventions

### 2.1 Named Editor Attribution

**Classification: PRACTICE ONLY**

JPE includes an editor attribution in the **first-page acknowledgment footnote** (the starred footnote), in the following form:

> "This paper was edited by [Full Name]."

This appears as a terminal sentence in the acknowledgment footnote. It is an editorial addition made at publication; authors do not write this themselves. Awareness of this convention is relevant for formatting the acknowledgment footnote — leave space for it and do not close the footnote in a way that precludes this addition.

### 2.2 Electronically Published Date

**Classification: PRACTICE ONLY**

First page includes "Electronically published [month day, year]" before the print issue date. Editorial addition; not author-written. Standard for UChicago Press online-first workflow.

---

## 3. Mathematical and Formal Content (Theory Papers)

### 3.1 Formal Result Environments

**Classification: PRACTICE ONLY**

JPE uses a specific named-environment convention for formal theoretical results, with **small caps** labels and **descriptive names**:

| Environment | Format |
|---|---|
| Proposition | `PROPOSITION X (Descriptive Name).` |
| Assumption | `ASSUMPTION X (Name).` |
| Condition | `CONDITION X (Name).` |
| Lemma | `LEMMA X.` |
| Example | `EXAMPLE X.` |

Key features:
- Label is in **small caps** (typeset as `\textsc{Proposition}` or equivalent)
- Descriptive name in parentheses immediately follows the number (for Propositions and Assumptions)
- Proof environment follows, concluding with QED mark
- These environments are numbered sequentially within their type across the full paper (not per-section)

The FIELD_SKILL baseline does not specify formatting for formal environments. JPE practice sets a distinct standard. For theory papers submitted to JPE, adopt this convention.

---

## 4. Figures and Tables

### 4.1 Figure Caption Format

**Classification: PRACTICE ONLY**

JPE figure captions use an em dash separator:

> `FIG. X.—[Caption text in complete sentence(s).]`

- Abbreviation: `FIG.` (not `Figure`)
- Period after number, then em dash (`—`), then caption text
- Caption text is a complete sentence with terminal period
- Notes (if any) appear below the caption in smaller type

### 4.2 Table Caption Format

**Classification: PRACTICE ONLY**

JPE table captions use a two-line format:

```
TABLE X
[ALL CAPS DESCRIPTIVE TITLE]
```

- `TABLE X` on its own line (no period)
- Descriptive title in ALL CAPS on the next line
- Notes section below the table body, introduced with `Note.—` or `Notes.—`

---

## 5. Abstract

### 5.1 Length and Structure

**Classification: PRACTICE ONLY**

JPE abstracts are **unstructured single paragraphs**, approximately **100 words**. The FIELD_SKILL baseline does not specify a word count, but field norms trend toward 100–150 words. JPE practice is at the shorter end (~100 words). No structured abstract (no bold labels for Background/Methods/Results). No JEL codes are embedded in the abstract itself (JEL codes appear as a separate field below the abstract on the first page).

---

## 6. FIELD DEFAULT — No Deviation Observed

The following FIELD_SKILL baseline conventions were confirmed in JPE practice with no deviation. Follow the baseline:

| Dimension | Baseline convention confirmed |
|---|---|
| Voice and person | First-person plural "we" throughout |
| Citation format | Author-year parenthetical; no footnote citations for literature |
| Citation density | High in introduction; moderate in body |
| Hedging | Low; results stated directly |
| Active voice | Consistently active |
| Introduction structure | Hook → question → approach → results → contributions → roadmap |
| Conclusion length | Shorter than introduction (~1.5–2 pages) |
| Conclusion function | Summarizes, does not introduce new results |
| Tense in methods | Mixed (past for own work, present for model) |
| Robustness | Reported as standard, typically in dedicated subsection |

---

## 7. Acquisition Notes

- **Guidelines status**: Inaccessible (403 Forbidden on all UChicago journal URLs, EZProxy authentication wall). All classifications above are PRACTICE ONLY.
- **Articles reviewed**: 1 full article (Acemoglu & Loebbing 2026, theory/quantitative hybrid, 56 pp. including Appendix A). Convergence rule not triggered — multiple deltas found.
- **Recommended follow-up**: Access JPE submission guidelines directly from within NHH network or via journal office. Priority items to confirm as ENFORCED: Data Availability section (§1.3), formal result environment formatting (§3.1).

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
