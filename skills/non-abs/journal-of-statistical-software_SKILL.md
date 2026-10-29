---
name: journal-of-statistical-software-writing-style
description: >
  Journal-specific writing conventions for Journal of Statistical Software (JSS)
  (ABS NHH, NON-ABS). Use alongside non-abs-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for JSS",
  "submit to Journal of Statistical Software", "match JSS style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Statistical Software

## Journal Profile
- **ABS 2024 Rating:** Not ABS-rated (NHH bonus tier). JSS does not appear on the ABS 2024 Academic Journal Guide; it is a statistics/computer-science venue, not a business/management journal.
- **Field:** NON-ABS (statistical computing and software)
- **Publisher:** Foundation for Open Access Statistics (FOAS). Older volumes (pre-~2016) were published by the American Statistical Association; the journal's own footer boilerplate reflects whichever publisher was current at publication.
- **Scope:** Publishes open-source statistical software paired with a reproducible scholarly article covering "design, implementation, documentation, application, evaluation, comparison, maintenance and distribution" of the software. Explicitly rejects methodological innovation alone (novel models/procedures must appear elsewhere first) and rejects software submissions lacking a documentation article.
- **Guidelines URL:** https://www.jstatsoft.org/authors ; https://www.jstatsoft.org/style ; https://www.jstatsoft.org/pages/view/mission
- **Field baseline:** non-abs-field-writing-style (NOT YET GENERATED - analysis proceeds without field comparison)
- **Articles spot-checked:** 6, of which 2 full-text:
  1. Gupta, Orlandi, Chang, Wang, Morucci, Dey, Howell, Sun, Ghosal, Roy, Rudin & Volfovsky, "dame-flame: A Python Package Providing Fast Interpretable Matching for Causal Inference," JSS 113(2), July 2025 — full text (PDF).
  2. Ho, Imai, King & Stuart, "MatchIt: Nonparametric Preprocessing for Parametric Causal Inference," JSS 42(8), May 2011 — full text (author-hosted mirror PDF).
  3. Untitled TrueSkill-through-time paper, JSS 112(6), March 2025 — partial: title, keywords, and citation-style visible; body text extraction failed (author names not verified, so not asserted here).
  4. Bates, Mächler, Bolker & Walker, "Fitting Linear Mixed-Effects Models Using lme4," JSS 67(1), 2015 — abstract, keywords, citation style from the landing page only, not full text.
  5. Hyndman & Khandakar, "Automatic Time Series Forecasting: The forecast Package for R," JSS 27(3), 2008 — abstract from the landing page only, not full text.
  6. Book Review 2, JSS 102, May 2022 — format/structure only (no abstract, single-flow narrative); page count could not be reliably extracted.

---

## Preliminary Note

JSS is an open-access, statistics/computer-science software journal, not a social-science or business journal. Its article form is closer to a hybrid of an academic paper and embedded software documentation than to any conventional empirical or theoretical paper structure. Because no NON-ABS field baseline exists yet, the observations below are absolute descriptions of JSS practice, not deltas from a baseline.

---

## Hard Constraints (Author Guidelines)

### Structure
**ENFORCED / PRACTICE (guideline + confirmed in both full-text articles, 2011 and 2025).** No Data/Methods/Results/Discussion skeleton is mandated or used. The recurring shape, confirmed in both full-text samples:
1. **Introduction** (numbered "1."), typically with subsections covering what the software does and its installation/software requirements, and often a roadmap paragraph previewing later sections ("In Section 2, we discuss...").
2. Theoretical/algorithmic background and, separately or combined, a **user's guide / worked examples** section with executable console-style code (`R>` or `>>>` prompts) interleaved directly with prose, walking through a real or toy dataset.
3. An explicit **comparison to existing software** — required by the mission statement ("a careful comparison with other open-source implementations"); in the dame-flame sample this is a standalone numbered subsection ending in a feature-comparison table against named competitor packages.
4. A **"Reference manual" / "API documentation" section** — a late, numbered major section (Section 4 in both samples) that abandons prose argument entirely and documents each class/function parameter-by-parameter, manual-page style: syntax, each argument with its type/default/options, and return values. This section is essentially reference documentation embedded in the paper and has no equivalent in ordinary academic writing.
5. A short **Conclusion(s)** section — common but not universal; the MatchIt sample moves directly from the reference manual to Acknowledgments with no separate conclusion.
6. Acknowledgments (funding **and** named individuals — unlike some field norms, thanking specific people by name is normal here, confirmed in both samples).
7. References, then a mechanical **Affiliation block** and journal footer (see below).

### Content-Type Tiering
**ENFORCED (guidelines).** JSS publishes five distinct content types, not one uniform article format: full peer-reviewed **Articles** (comprehensive implementations, must include a non-trivial case study and comparison to alternatives); **Special Issues** (thematic, guest-edited, still peer-reviewed); **Code Snippets** (narrower-scope implementations using existing infrastructure, shorter and less comprehensive than a full article); **Software Reviews** (invited evaluations, including of closed-source software, held to a fairness/unbiasedness standard); **Book Reviews** (invited, overseen by a book editor, no abstract, no reference-manual section, narrative single-flow prose evaluating a book rather than presenting software).

### Length
**GUIDELINE ONLY.** No explicit page limit. Manuscripts over 30 pages "typically require much longer review times." "Careful writing exhibiting high readability" is stated as more important than length. Code Snippets are narrower and shorter by definition (mission statement); Book Reviews are markedly shorter still (a specific page count could not be reliably confirmed from the sample read).

### Abstract
**PRACTICE ONLY (no word limit stated in guidelines; range observed across 4 samples).** Single unstructured paragraph, no subheadings, no separate keyword-style fields. Observed length ranges from roughly 70 words (Hyndman & Khandakar 2008) to roughly 150 words (Bates et al. 2015; dame-flame ~130; MatchIt ~120). The package/software name is set in bold throughout, including inside the abstract. **Citations are permitted inside the abstract** when crediting a methodological source — the MatchIt abstract cites "Ho, Imai, King, and Stuart (2007)" twice — this is not universally prohibited the way it is in some other journals (e.g., Nature). Abstracts frequently close with a capability or availability statement (a GitHub/CRAN link, or a sentence naming what the software interoperates with) rather than a summary of findings.

### Keywords
**PRACTICE ONLY.** A single unlabeled `Keywords:` line (italicized), comma-separated, lowercase except proper nouns, always ending with the implementation language(s) (e.g., "..., Python." or "..., R."), terminated with a period. Observed counts: 4–5 terms. No explicit minimum or maximum stated in the guidelines.

### Citations
**ENFORCED (style guide) + PRACTICE (reference-list format confirmed in both full-text samples, 14 years apart).** Author-year via natbib: `\citet{}`/`\cite{}` render as "Author (Year)"; `\citep{}` renders as "(Author Year)"; page references use `\citet[p.~123]{}`. Never nest brackets-within-brackets like `(\cite{})`. The **reference list** itself lists every author as `Surname Initials`, comma-separated, with no ampersand or "and" before the final name (e.g., "Ho D, Imai K, King G, Stuart E (2007)."), confirmed identically in a 2011 paper and a 2025 paper. In-text handling of many-author works varies by paper: the dame-flame sample switches to "et al." after first mention for its own 5-author foundational citation, while the MatchIt sample spells out all four author names on every occurrence throughout a 27-page paper — this looks like an authors'-group stylistic choice rather than a house rule, so treat "et al. after first mention" as the safer default rather than a strict requirement.

### Headings
**ENFORCED via template.** Decimal numbering (`1.`, `1.1.`, `1.2.`) with a period after each number component; refer to subsections in prose as "Section x.y," never "Subsection." Titles use sentence-style capitalization ("What MatchIt does," not "What MatchIt Does"). `\section[]{}` with escaped markup is used when the natural section title contains formatting that would break a PDF bookmark.

### Code and Markup
**ENFORCED (style guide, confirmed in both full-text samples).** `\pkg{}` for package names (rendered bold, applied to *every* occurrence of the package name throughout the paper, not just first mention), `\proglang{}` for programming-language names, `\code{}` for inline code. Verbatim code uses the `{Code}`/`{CodeInput}`/`{CodeOutput}` environments; **no comments inside verbatim code blocks** — explanatory comments belong in the surrounding prose, not as `#`/`//` lines in the listing. Spaces around operators (`y = a + b * x`, not `y=a+b*x`). Executable examples are shown as REPL transcripts (`R>` or `>>>` prompts) with the literal printed output immediately following, interleaved directly into the narrative — the code-and-its-output *is* the evidence for a claim, not a table of statistical results.

### Tables and Figures
**ENFORCED (style guide).** Every figure/table requires `\label{}` and is invoked via `\ref{}`. Captions appear **below** the figure/table, sentence-case, ending in a period, with no additional formatting (`\emph`, `\bf`, `\it`) inside the caption. Footnote-style annotations belong in the caption, not embedded in the table body. Table headers use sentence-style capitalization.

### Math
**ENFORCED (style guide).** `$p$~value` (tilde, not a hyphen). Transpose symbol is `\top`. (Equation-numbering conventions were not reliably confirmed across the sample and are not asserted here.)

### Reproducibility and Submission
**ENFORCED.** Three mandatory attachments: the PDF manuscript in JSS style, the software source code, and replication materials (preferably a single commented standalone script) for every result in the manuscript. All figures/tables/output must be "fully and exactly reproducible on at least one platform"; pseudo-random-number generators must be seeded. Rough target: a technically competent reader should be able to install the software and run the replication material within about one hour on a regular PC. Code must carry a GPL-2/GPL-3 or GPL-compatible license; package-based submissions need formatted help files and should be on a standard repository (CRAN, Bioconductor, PyPI). Manuscripts must be LaTeX using JSS's own style files, compiled with pdfLaTeX, submitted as PDF only, 50 MB upload maximum.

### End-of-Article Affiliation Block and Footer
**ENFORCED via template (identical structure confirmed in a 2011 paper and a 2025 paper).** Immediately after the reference list, each author gets a block:
```
[Full Name]
[Department (optional)]
[University]
[Full postal address, including country]
E-mail: [address]
```
Older papers (e.g., 2011) also include `URL:`, `Telephone:`, and `Fax:` lines per author; the 2025 sample omits phone/fax and sometimes lists only a subset of co-authors rather than all of them. This is followed by a fixed journal footer giving the journal name and URL, the publisher and its URL, the volume/issue and publication month/year, the DOI, and the exact `Submitted:` / `Accepted:` dates. This mechanical closing block has no equivalent in ordinary field-baseline writing and should not be improvised or omitted.

### Explicit Prohibitions
- "Extensive simulation studies are discouraged" (direct quote from the author guidelines) — simulation should illustrate theory, not substitute for the required comparison/case-study content.
- Does not publish methodological innovation in computational statistics on its own; a novel model or procedure must be published elsewhere first, with the JSS submission documenting its software implementation.
- Does not accept supplementary-materials-only submissions to a methodology paper, or software with no accompanying documentation article.
- "Manuscripts rejected by JSS cannot be resubmitted."
- A revision not returned within six months of being requested is treated as withdrawn; a conditional acceptance not finalized within one year is treated as withdrawn.
- No small caps, italics, or periods in abbreviations.
- No comments inside verbatim code blocks.
- No additional formatting (`\emph`, `\bf`, `\it`) inside figure/table captions.

---

## Observed Deltas from FIELD_SKILL

> LIMITATION: FIELD_SKILL for NON-ABS not yet generated. Findings below are absolute observations of JSS practice, not deviations from a baseline.

### Manuscript Architecture
The largest and most consistent observation across the sample: JSS replaces the Data/Methods/Results/Discussion architecture entirely with Introduction → theory-and-worked-examples → mandatory comparison-to-existing-software → a **reference-manual section written as parameter-by-parameter documentation, not prose**. This reference-manual convention was independently confirmed in two full-text articles fourteen years apart (2011, 2025), by unrelated author groups, both explicitly labeling the section "Reference manual" / "API documentation."

### Voice and Register
Mixed by section, not uniform across the paper. Narrative sections (Introduction, worked examples, discussion of results) use first-person-plural "we" ("We offer the Python package...", "We conclude this is a reasonable ATE estimate..."). The reference-manual/API section shifts register entirely to direct second-person documentation voice addressing "the user" with imperative mood ("Use `matchit()` to implement...", "Users must begin by providing..."). A paper that stays in "we"-narrative voice throughout, or that never shifts into documentation voice for its parameter listing, is not matching observed JSS practice.

### Statistical/Evidential Reporting
Evidence for a claim is a runnable, reproducible code transcript plus its literal printed output (interleaved into prose as `R>`/`>>>` blocks), and/or a feature-comparison table against named alternative packages — not a table of regression coefficients, effect sizes, or significance tests reported as the paper's primary contribution. Simulation results, where present, illustrate the software rather than constitute the paper's evidentiary core (consistent with the "extensive simulation studies are discouraged" prohibition above).

### Citation Placement
Citations are permitted, and observed, inside the abstract itself when the abstract needs to credit the methodological source paper the software implements — a pattern some other journals (e.g. Nature) explicitly forbid.

### Package/Software-Name Typography
The package name is set in bold (`\pkg{}`) at *every* occurrence throughout the running text, not just on first mention — confirmed identically in both full-text samples across a 14-year span. Programming-language names (`\proglang{}`) receive the same always-marked-up treatment.

---

## Dimensions Not Assessed (Insufficient Data)

- Equation-numbering conventions (whether all displayed equations are numbered or only cross-referenced ones) — sample too small and inconsistent to confirm a rule.
- Hedging and epistemic-register conventions outside the reference-manual section.
- Precise page-count norms for Code Snippets and Book Reviews (guidelines give no number; the one book review sampled could not be reliably measured from the extracted text).
- Whether the theory-section/user's-guide-section subsection numbers are always mirrored 1:1 (observed in the MatchIt sample — Sections 2.1–2.3 and 3.1–3.3 share identical subsection titles — but not in the dame-flame sample, so this looks like an optional authorial structuring choice, not a house rule).

---

## Common Pitfalls

1. **Submitting a paper with no accompanying software**, or a pure methodological/theoretical contribution — explicitly out of scope; the method must be published elsewhere first, with the JSS piece documenting its implementation.
2. **Writing a conventional empirical/theoretical paper structure** (Data/Methods/Results/Discussion) instead of the Introduction → theory/examples → comparison → reference-manual shape described above.
3. **Skipping or shortchanging the comparison-to-existing-software section** — the mission statement requires it explicitly, and reviewers check for it.
4. **Making simulation studies the paper's central evidence** rather than a supporting illustration — the guidelines explicitly discourage "extensive simulation studies."
5. **Missing or incomplete replication materials** — reviewers are instructed to verify reproducibility and to withhold acceptance until reproducibility problems are fully resolved.
6. **Wrong markup**: omitting `\pkg{}`/`\code{}`/`\proglang{}`, putting explanatory comments inside verbatim code blocks, or using small caps/italics/periods in abbreviations.
7. **Treating the reference-manual section as optional or as ordinary prose** — it is a required, distinctly-formatted documentation section, not a summary paragraph about the API.
8. **Resubmitting after rejection** — explicitly barred; a rejected manuscript cannot be resubmitted to JSS.
9. **Omitting the end-of-article affiliation block** or improvising its format instead of following the fixed name/department/university/address/email template.

---

## Avoiding AI-Writing Patterns

<!-- academic-humanizer:start v0.3.3 -->
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
<!-- academic-humanizer:end -->

---

## Sources

| Source | Type | Access |
|--------|------|--------|
| https://www.jstatsoft.org/authors | Guidelines | WebFetch, direct |
| https://www.jstatsoft.org/style | Style guide | WebFetch, direct |
| https://www.jstatsoft.org/pages/view/mission | Mission statement | WebFetch, direct |
| https://www.jstatsoft.org/article/download/v113i02/4716 | Full-text PDF (dame-flame, JSS 113(2), 2025) | Read (downloaded PDF) |
| https://imai.fas.harvard.edu/research/files/matchit.pdf | Full-text PDF (MatchIt, JSS 42(8), 2011; author-hosted mirror) | Read (downloaded PDF) |
| https://www.jstatsoft.org/article/download/v112i06/4680 | Partial (title/keywords/citation style only) | WebFetch (body extraction failed) |
| https://www.jstatsoft.org/article/view/v067i01 | Landing page (lme4 abstract/keywords) | WebFetch |
| https://www.jstatsoft.org/article/view/v027i03 | Landing page (forecast abstract) | WebFetch |
| https://www.jstatsoft.org/article/download/v102b02/4305 | Book review (structure only) | WebFetch (unreliable text extraction) |

*Access note: JSS is fully open access, so full-text access was not the limiting factor it is for paywalled journals in this library. The two full-text reads (2011 and 2025, unrelated author groups) independently converged on the same reference-manual/affiliation-block structure, which is the strongest evidence in this file.*
