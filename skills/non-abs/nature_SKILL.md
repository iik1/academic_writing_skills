---
name: nature-writing-style
description: >
  Journal-specific writing conventions for Nature
  (ABS NHH, NON-ABS). Use alongside non-abs-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Nature",
  "submit to Nature", "match Nature style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Nature

## Journal Profile
- **ABS 2024 Rating:** NHH (Norwegian School of Economics bonus tier)
- **Field:** NON-ABS (multidisciplinary science)
- **Publisher:** Springer Nature
- **Scope:** Premier multidisciplinary science journal publishing breakthrough research across all fields of science and technology
- **Guidelines URL:** https://www.nature.com/nature/for-authors
- **Field baseline:** non-abs-field-writing-style (NOT YET GENERATED - analysis proceeds without field comparison)
- **Articles spot-checked:** 0 (full-text access blocked by authentication; analysis based on guidelines only)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure

**ENFORCED** - Required section order:
1. Abstract/Summary paragraph (unreferenced, ~150-200 words)
2. Introduction (referenced text expanding on background)
3. Results (divided by topical subheadings)
4. Discussion (succinct, may NOT contain subheadings)
5. Methods (typically <3,000 words, divided by topical subheadings)
6. References (must include article titles, one publication per number)
7. Acknowledgements (brief, no thanks to anonymous referees/editors)
8. Author contributions statement (required)
9. Competing interests statement (required for all content)

**Notable:** Methods section appears at END of manuscript, not before Results. Discussion must be succinct and cannot use subheadings.

### Length

**ENFORCED:**
- Main text: maximum 3,500 words (excludes abstract, methods, references, figure legends)
- Abstract: ideally no more than 200 words (some sources state ~150 words)
- Methods: typically less than 3,000 words
- Display items: maximum 6 (figures and tables combined)
- References: up to 50 as guideline (not strict limit)

### Abstract

**ENFORCED:**
- Format: Single unreferenced summary paragraph
- Length: Ideally ≤200 words
- Content restrictions: Avoid numbers, abbreviations, acronyms, or measurements unless essential
- Placement: Separate from main text, before Introduction

**Distinctive feature:** Abstract described as "summary paragraph" rather than structured abstract.

### Citations

**ENFORCED:**
- Style: Numbered references
- References section: Must list only one publication per number
- Must include the title of cited article or dataset
- Maximum ~50 references as guideline

### Headings

**ENFORCED:**
- Main sections use standard headings: Introduction, Results, Discussion, Methods
- Results and Methods: divided by topical subheadings
- Discussion: may NOT contain subheadings (must be succinct)

### Tables and Figures

**ENFORCED:**
- Maximum 6 display items total (figures + tables)
- Font: Sans-serif typeface, preferably Helvetica or Arial, consistent across all figures
- Multi-part figures: Label with lowercase boldface letters (a, b, c)
- Axis labels: Sentence case without periods
- Units: Include spaces between numbers and units
- Color: Use colorblind-accessible palettes; avoid red-green contrast
- Initial submission: Incorporate figures into single PDF or Word file with manuscript text
- Final submission: RGB color mode, 300+ dpi, vector formats preferred (.ai, .eps, .pdf, .svg)
- Figure legends: Present together with figures

### Submission Format

**ENFORCED:**
- Manuscript format: Single PDF or Microsoft Word file incorporating text and figures
- Line numbering: Required (automatic in Word uploads; manual for PDFs)
- Reporting summary: Required for life sciences manuscripts reporting original research

### Explicit Prohibitions

**ENFORCED:**
- Abstract: No citations, avoid numbers/abbreviations/acronyms unless essential
- Discussion: No subheadings allowed
- Acknowledgements: No thanks to anonymous referees or editors; no effusive comments
- Figures: No red-green color contrast (accessibility requirement)

---

## Observed Deltas from FIELD_SKILL

> LIMITATION: FIELD_SKILL for NON-ABS not yet generated. Cannot perform delta analysis.
> All findings below are absolute observations, not deviations from field baseline.

### Manuscript Architecture

**Observed (source: guidelines):**
- Methods section placement at END (after Discussion) rather than after Introduction
- Discussion must be succinct and may not contain subheadings (explicit prohibition)
- Results and Methods use topical subheadings; Discussion does not

**Classification:** ENFORCED (stated in guidelines, not yet verified in articles)

**Note:** This Methods-last structure may differ from standard NON-ABS field conventions but cannot be classified as delta without field baseline.

### Abstract Conventions

**Observed (source: guidelines):**
- Called "summary paragraph" not "abstract"
- Explicitly unreferenced
- Strict avoidance of numbers, abbreviations, acronyms, measurements unless essential
- Very brief: ideally ≤200 words

**Classification:** ENFORCED

**Note:** The term "summary paragraph" and prohibition on numbers/abbreviations may be Nature-specific but cannot confirm without field baseline.

### Post-Text Apparatus

**Observed (source: guidelines):**
- Author contributions statement: Required
- Competing interests statement: Required for all content
- Acknowledgements: Explicit prohibition on thanking referees/editors or effusive comments

**Classification:** ENFORCED

### Figure Accessibility Requirements

**Observed (source: guidelines):**
- Mandatory colorblind-accessible palettes
- Explicit prohibition on red-green contrast
- Specific font requirements (Helvetica/Arial)

**Classification:** ENFORCED

**Note:** Accessibility requirements may exceed typical field standards.

---

## Dimensions Not Assessed (Insufficient Data)

Due to inability to access full-text articles, the following dimensions were not analyzed:

- Voice and person (active vs. passive voice prevalence)
- Citation density patterns in Introduction
- Statistical reporting conventions (p-value reporting, confidence intervals, etc.)
- Actual adherence to guideline-stated structure
- Tone and register variations
- Subheading formatting practices within Results/Methods
- Figure caption length and style
- Supplementary materials organization

---

## Common Pitfalls

Based on guidelines analysis:

1. **Discussion subheadings:** Authors may try to organize Discussion with subheadings as done in Results/Methods - explicitly prohibited

2. **Abstract verbosity:** Exceeding 200-word limit or including citations, numbers, abbreviations unnecessarily

3. **Methods placement:** Positioning Methods section before Results (standard in many disciplines) rather than at end as Nature requires

4. **Display item limit:** Exceeding 6 figures+tables combined; authors may underestimate how restrictive this is

5. **Reference titles:** Omitting article titles in reference list (required by Nature, not universal practice)

6. **Acknowledgement tone:** Thanking anonymous reviewers or using effusive language (explicitly prohibited)

---

## Sources

| Source | Type | Access |
|--------|------|--------|
| https://www.nature.com/nature/for-authors | Guidelines landing | WebSearch successful |
| https://mts-nature.nature.com/cgi-bin/main.plex?form_type=display_auth_instructions | Author instructions | WebFetch successful |
| https://www.nature.com/nature/for-authors/formatting-guide | Formatting guide | 303 redirect - inaccessible |
| https://www.nature.com/nature/for-authors/initial-submission | Initial submission | 303 redirect - inaccessible |
| https://www.nature.com/articles/s41586-026-10265-5 | 2026 research article | 303 redirect - inaccessible |
| https://www.nature.com/articles/s41467-026-71269-3 | Nature Comm. article | 303 redirect - inaccessible |

**Access limitations:** All full-text article URLs returned 303 redirects, indicating authentication barriers incompatible with automated WebFetch. PDF guidelines could not be parsed (binary encoding). Analysis based solely on HTML-rendered guideline pages successfully accessed.

**Recommendation:** Manual verification of article-level practices required before relying on this skill for high-stakes submissions.