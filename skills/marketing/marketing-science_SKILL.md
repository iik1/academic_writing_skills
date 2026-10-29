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
| https://mitsloan.mit.edu/sites/default/files/2025-08/Style-Instructions.pdf | INFORMS style guide (all journals) | WebFetch (PDF read successfully) |
| https://pubsonline.informs.org/page/mksc/submission-guidelines | Submission guidelines | WebSearch (content summarized) |
| https://pubsonline.informs.org/journal/mksc | Journal home | WebSearch |
| General web searches for Marketing Science requirements | Multiple | See search results above |

**Articles accessed:** None (paywall/access restrictions prevented full-text article review). Analysis based on official INFORMS style documentation and submission guidelines.