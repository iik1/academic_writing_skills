---
name: marketing-science-writing-style
description: >
  Journal-specific writing conventions for Marketing Science
  (ABS 4*, MKT). Use alongside mkt-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Marketing Science",
  "submit to Marketing Science", "match Marketing Science style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Marketing Science

## Journal Profile
- **ABS 2024 Rating:** 4*
- **Field:** MKT
- **Publisher:** INFORMS (Institute for Operations Research and the Management Sciences)
- **Scope:** Premier journal for empirical and theoretical quantitative research in marketing; emphasizes mathematical modeling, econometric methods, and rigorous analytical contributions
- **Guidelines URL:** https://pubsonline.informs.org/page/mksc/submission-guidelines
- **Field baseline:** mkt-field-writing-style
- **Articles spot-checked:** 0 (direct article access blocked by paywalls; analysis based on INFORMS style guide PDF and submission guidelines)

**Note:** Marketing Science is one of four ABS 4* journals that define the MKT field baseline. Most conventions described in mkt-field-writing-style originate from or are exemplified by this journal.

---

## Hard Constraints (Author Guidelines)

### Structure
**ENFORCED:** Double-column final format (submission format: double-spaced, single-column, 11-12pt font, 1-inch margins). Sections numbered consecutively (1, 2, 2.1, etc.) in economics/operations research style. No deviation from FIELD_SKILL structural norms for quantitative empirical papers: Introduction → Literature/Background → Data → Model → Results → Discussion/Conclusion. Mathematical models presented with numbered equations.

### Length
**GUIDELINE ONLY:** No explicit word limit for regular articles. "Marketing Science: Frontiers" papers (special article type): authors encouraged to keep manuscripts to 6,000 words including references. In practice, emphasis is on contribution quality over length constraints.

### Abstract  
**ENFORCED:** Maximum 200 words. Unstructured (single paragraph). No citations. No mathematical notation or equations (INFORMS-wide prohibition to ensure web browser compatibility). Must communicate contribution clearly to general readers, not just specialists.

### Citations
**ENFORCED:** Author-year system following natbib conventions: (Author, Year) or Author (Year). References listed alphabetically by author surname. Follows INFORMS house style via informs2014.bst BibTeX style file or equivalent manual formatting. Three or more authors abbreviated to "first author et al." from first citation. No deviation from FIELD_SKILL.

### Headings
**ENFORCED:** Numbered sections (1, 1.1, 1.1.1) required for quantitative papers. LaTeX template uses `\section{}`, `\subsection{}`, `\subsubsection{}`. Follows INFORMS informs4.cls style with [mksc] journal option. No deviation from FIELD_SKILL quantitative paper norms.

### Tables and Figures
**ENFORCED:** Table captions above tables; figure captions below figures (per INFORMS style). Only three horizontal rules in tables: above column heads, between heads and body, below body. Straddle rules (partial horizontal rules) permitted where necessary. Significance indicated by asterisks (*** p < 0.01, ** p < 0.05, * p < 0.1). Vector formats (PDF, EPS) preferred for figures; minimum 300 dpi for photographs. Tables and figures may be rotated to landscape if necessary. No deviation from FIELD_SKILL.

### Mathematical Notation
**ENFORCED:** Variables set italic. Vectors set bold. Mathematical functions and operators set roman (e.g., max, lim, log). INFORMS provides macros for bold symbols (\BFalpha, \BFx, etc.). Displayed equations numbered consecutively through article (1, 2, 3...) or by section (1.1, 1.2, ...) if complexity requires. No deviation from FIELD_SKILL for quantitative papers.

### Explicit Prohibitions
**ENFORCED:** 
- Footnotes prohibited—use endnotes. Display endnotes before References section using `\THEEndNotes` command.
- No mathematical notation in abstract.
- No citations in abstract.
- Must remove author-identifying information for double-anonymous review (names, affiliations, acknowledgments, self-citations that reveal identity).
- Equations in display format may not break after operators (break before operators instead).

### Data and Code
**ENFORCED:** Upon acceptance, authors must submit data and estimation codes used in the paper. Primary objective: ensure replicability. Marketing Science maintains a strict replication policy. This is a journal-specific enforcement beyond general FIELD_SKILL norms.

---

## Observed Deltas from FIELD_SKILL

### Replication Policy
**FIELD BASELINE:** Field-level best practice encourages data/code sharing; not universally enforced across all MKT journals.

**MARKETING SCIENCE DEVIATION:** Data and code submission required upon acceptance. Non-negotiable replication standard.

**CLASSIFICATION:** ENFORCED

---

### Generative AI Policy
**FIELD BASELINE:** Not addressed in FIELD_SKILL (emerging issue).

**MARKETING SCIENCE POSITION:** Authors welcome to use generative AI tools in manuscript preparation. Authors remain responsible for accuracy of all facts and references. Disclosure not explicitly required, but responsibility is non-delegable.

**CLASSIFICATION:** GUIDELINE ONLY (permissive stance; enforcement unclear)

---

### Frontiers Article Type
**FIELD BASELINE:** Not addressed (journal-specific article category).

**MARKETING SCIENCE ADDITION:** "Marketing Science: Frontiers" papers are shorter, more accessible articles targeting 6,000 words including references. Intended for rapid dissemination of high-impact findings. Traditional journal articles have no explicit word cap.

**CLASSIFICATION:** PRACTICE ONLY (special article track)

---

### LaTeX Template
**FIELD BASELINE:** LaTeX common in MKT quantitative work but not universal.

**MARKETING SCIENCE EMPHASIS:** Official INFORMS template provided: `informs4.cls` with `\documentclass[mksc]{informs4}` option. BibTeX style file `informs2014.bst` provided. Authors may use preferred software but must provide compiled PDF. LaTeX strongly encouraged for papers with heavy mathematical content.

**CLASSIFICATION:** GUIDELINE ONLY (preferred but not required)

---

### Keywords
**FIELD BASELINE:** Not specified in FIELD_SKILL.

**MARKETING SCIENCE REQUIREMENT:** 3–6 keywords required, describing theoretical and methodological orientation. Appear beneath abstract.

**CLASSIFICATION:** ENFORCED

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" throughout)
- Statistical reporting: FIELD DEFAULT (regression tables with SE in parentheses, *** /** /* significance stars, coefficient magnitudes interpreted substantively)
- Citation density: FIELD DEFAULT (introduction and literature review citation-dense; methods sparse; results minimal; discussion moderate)
- Structural organization for quantitative papers: FIELD DEFAULT (Data → Model → Results structure standard)
- Equation presentation: FIELD DEFAULT (numbered, aligned, formal notation)
- Hypothesis vs. identification framing: FIELD DEFAULT (empirical identification problem framed; causal quantities and threats addressed)
- Length of sections: FIELD DEFAULT (no journal-specific deviation)
- Use of appendices: FIELD DEFAULT (proofs, robustness checks, additional specifications in appendices standard)

---

## Common Pitfalls

1. **Including footnotes instead of endnotes:** INFORMS prohibits footnotes across all journals. Convert all footnotes to endnotes and place before References using `\THEEndNotes` command. Failure to do so will result in desk reject or mandatory revision.

2. **Abstract exceeds 200 words or contains math/citations:** Abstract must be exactly one paragraph, ≤200 words, with no equations or citations. Web display requirements prohibit mathematical notation. Violating these constraints delays publication.

3. **Inadequate mathematical rigor for audience:** Marketing Science reviewers and readers expect formal model specifications with equation numbers, rigorous identification arguments, and structural interpretation. Papers that rely solely on reduced-form correlational evidence without addressing causality or mechanism are typically rejected. The journal is economics-facing; match that standard.

4. **Failing to submit replication materials upon acceptance:** Data and code are required for publication. Plan for this from the start. Proprietary data require clear disclosure of access procedures. Code must be documented and executable. Failure to comply delays or blocks publication.

5. **Misunderstanding double-anonymous review requirements:** Remove all identifying information—names, affiliations, acknowledgments, and self-citations that reveal identity (e.g., "In our prior work (Smith, 2023)..." should be "Prior work has shown (Smith, 2023)..."). Manuscripts that break anonymity are returned without review.

---

## Sources

| Source | Type | Access |
|--------|------|--------|
| https://mitsloan.mit.edu/sites/default/files/2025-08/Style-Instructions.pdf | INFORMS style guide (all journals) | WebFetch (PDF read successfully) |
| https://pubsonline.informs.org/page/mksc/submission-guidelines | Submission guidelines | WebSearch (content summarized) |
| https://pubsonline.informs.org/journal/mksc | Journal home | WebSearch |
| General web searches for Marketing Science requirements | Multiple | See search results above |

**Articles accessed:** None (paywall/access restrictions prevented full-text article review). Analysis based on official INFORMS style documentation and submission guidelines.