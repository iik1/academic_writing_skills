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