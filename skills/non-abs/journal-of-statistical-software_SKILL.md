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
These conventions apply regardless of field or journal. Apply them in addition to everything above; only deviate where this journal's own guidelines explicitly require otherwise. One exception within this section: in a funding proposal, Layer 6 overrides the paper-mode trimming of ambition language.

*Merged from academic-humanizer v0.3.3 (MIT License, AIScientists-Dev), which builds on humanizer by blader (MIT); full license text in THIRD_PARTY_NOTICES.md of the academic_writing_skills repository.*

### Core principle and scope

Improve the clarity and voice of AI-assisted *academic* writing while keeping the precise, evidence-bound voice that scholarship requires and matching the author's own style. Preserve every number, result, and citation. This is not a tool for evading AI-use disclosure.

**Scope.** Editing or reviewing academic prose: paper sections, abstracts, rebuttals, related work, and **funding proposals** (NSF Project Summary/Description, NIH Specific Aims, ERC, NFR, fellowship and foundation proposals; see Layer 6). **Not** for blogs, marketing, or personal essays, and **never** inject opinion, humor, or first-person "personality" into a manuscript. For technical writing, neutral and precise *is* the human voice. One caveat for proposals: their register is different from a paper's, since they are sold on vision and feasibility, so the ambition language a paper would trim is appropriate there; apply Layer 6, not the paper layers' stricter trimming, to vision statements.

**Core principle.** Academic writing already has a correct human voice: neutral, precise, third-person plural ("we"), every claim tied to its evidence. The job is to (1) strip the AI *tells* without casualizing, and (2) enforce the discipline a general humanizer misses: **every claim earns its number, figure, or citation, and no verb is stronger than its evidence.**

### Process

1. **Read** the manuscript and any author writing sample; note the document type (paper vs. funding proposal) and the target venue or funding agency. For proposals, also apply Layer 6 and preserve appropriate vision.
2. **Audit** (do not edit yet): list each detected pattern with its location and proposed fix, and each empirical claim's evidence status.
3. **Rewrite**: same structure and content, all claims and citations preserved, tells removed, over-claims matched to evidence, legitimate hedging kept.
4. **Report**: cleaned text plus a short change log (patterns removed, claims softened or given evidence pointers, voice notes). Cover everything the original covered: if it had five paragraphs, so does the rewrite. See Output below.

### Layer 1: General AI tells

Scan for and fix these general patterns, subject to the academic exceptions in Layer 3. Connectives, vague quantities, formulaic openers, emphasis openers, hedging, and novelty claims are covered in Layer 2.

1. **No participial result clauses.** Findings should not carry an "-ing" tail asserting an interpretation the sentence has not earned ("...rose by 12 points, highlighting the importance of enforcement"; "...underscoring the need for validation"; "...demonstrating that norms shifted"). State the finding. If the implication is worth stating, state it as its own sentence.
2. **Limit rule-of-three constructions.** An occasional triple is fine ("clear, concise, and compelling"); a triad in every paragraph is a tell, and so is a triple added as padding. Vary the structure.
3. **Replace importance-inflation words with the actual magnitude.** Avoid "crucial," "critical," "pivotal," "vital," "paramount," "invaluable," "essential" as importance markers, inflated significance ("marking a pivotal moment"), and "dramatically" as an intensifier. Avoid "vast," "myriad," "plethora." State the size of the effect instead of asserting its importance. For "significantly," see 2.1.
4. **Avoid the 2023-era word list.** "Delve," "explore" (as metaphor), "unpack," "navigate," "landscape," "realm," "tapestry," "testament," "journey," "harness," "leverage," "unlock," "foster," "bolster," "garner," "showcase," "boast," "underscore," "pivotal," "seamless," "holistic," "multifaceted," "nuanced," "intricate," "interplay." Also avoid "robust" outside its statistical sense and "comprehensive" as self-description.
5. **No promotional or figurative language.** Avoid "rich," "vibrant," "groundbreaking," and similar praise or imagery for any subject. Describe it plainly. (For praise of your own contribution, see 2.4.)
6. **No empty balance.** Avoid "while challenges remain," "a double-edged sword," "strikes a balance," "it is not without limitations," "both approaches have merits": these simulate judgment without making one. Do not open more than one or two sentences per section with a concessive "While X, Y" construction.
7. **No vague attributions.** Avoid "experts argue" and similar attributions with no citation attached. Cite the source or cut the attribution.
8. **No anthropomorphised prose.** Avoid "the data tell a story," "the analysis paints a picture," "this paper seeks to," "the results speak to."
9. **No padding verb phrases or copula avoidance.** Replace "serves to," "serves as," "acts as," "stands as," "functions as," "is able to," "in order to," "due to the fact that," "utilize," "prior to," "commence" with their one-word equivalents ("serves as" -> "is").
10. **No wrap-up restatement.** A conclusion should add the implication or end. It should not repeat what was just said via "Taken together, these results suggest...," "In sum," or "In conclusion" followed by a restated summary.
11. **No elegant variation.** Do not cycle synonyms for one referent. Pick one term and keep it.
12. **Vary rhythm.** Avoid clustering sentence lengths in a narrow band, making every paragraph roughly equal, or opening every section the same way. Split overlong, clause-stacked sentences (2.11).
13. **No chatbot leakage.** Avoid "Certainly," "Here's," "Let's examine," "we can see that," "as mentioned above": residue from copy-pasted chat output.
14. **No em dashes.** Remove em dashes (the long dash, U+2014) entirely. Recast with a period, comma, colon, or parentheses, or split into separate sentences, whichever the sentence actually calls for.
15. **No antithesis padding or negative parallelisms.** Avoid the "X, not Y" contrast construction as a rhetorical flourish ("a correlation, not a coincidence"; "a policy shift, not a technical adjustment") and "not just X, but Y" unless the contrast is doing real argumentative work and stated once.
16. **No fillers.** Cut "basically," "essentially," "simply," "just," "really," "very," "quite," "actually" unless the sentence fails without them.
17. **No flourish labels.** Do not bold or set off rhetorical labels like "The Bottom Line:," "Key Insight:," "Takeaway:," "Bottom line," "The upshot." State the point in the sentence itself. Structural run-in labels in a funding proposal (6.4) are not flourish labels.
18. **No topic-announcing openers.** Avoid "This section discusses...," "This paper will discuss...," "Let's turn to...," "We now turn our attention to...." Open with the content itself.

**Before:** *Additionally, an enduring testament to the method's value is its ability to delve into intricate dependencies, showcasing a seamless integration that underscores its pivotal role.*
**After:** *The method also captures higher-order dependencies, which the baselines miss (Table 2).*

### Layer 2: Academic AI tells (remove or fix)

#### 2.1 Over-claiming verbs
Empirical work *shows* and *provides evidence*; it does not *prove* or *demonstrate* universal truths.
**Watch:** demonstrate, prove, establish, confirm, guarantee. Use "significantly" only for a stated statistical test, with the test and its result; never as an intensifier.
**Before:** *We prove that our method significantly outperforms all prior approaches.*
**After:** *Our method improves held-out accuracy by 4--7 points over the strongest prior approach (Table 3); the gain is significant at p < 0.01 by a paired test.*

#### 2.2 Significance hype
**Watch:** paves the way for, a crucial/pivotal step toward, has the potential to revolutionize, opens new avenues, sheds light on, of paramount importance, bridges the gap.
**Before:** *This work paves the way for a new paradigm and sheds light on a problem of paramount importance.*
**After:** *This work addresses one failure mode of prior methods: error accumulation under long-horizon rollout (Section 4).*

#### 2.3 Empty intensifiers and vague quantities
**Watch:** extensive/comprehensive/thorough experiments, a wide range of, a range of, a number of, several key, numerous, various, "numerous studies" without citations attached. Give the count or the citation.
**Before:** *We conduct extensive experiments on a wide range of datasets.*
**After:** *We evaluate on three datasets (ImageNet, CIFAR-100, and iNaturalist).*

#### 2.4 Novelty padding and self-praise
Never characterize your own contribution as "novel," "innovative," "unique," "cutting-edge," "state-of-the-art," or "groundbreaking," and drop "to the best of our knowledge" and "for the first time." Say what the work addresses that prior work does not, and let the reader judge novelty. This holds in funding proposals too: Layer 6 keeps vision language, not self-labels.
**Before:** *We propose a novel framework and, to the best of our knowledge, are the first to study this.*
**After:** *We study online calibration under delayed labels, which prior calibration work (offline) does not address.*

#### 2.5 Formulaic and throat-clearing openers
**Watch:** "In recent years, X has attracted increasing attention"; "In recent years, there has been growing interest in..."; "With the rapid development of..."; "With the advent of..."; "In today's rapidly evolving..."; "Despite recent advances,...". Delete and start with the claim.
**Before:** *In recent years, tabular deep learning has attracted increasing attention.*
**After:** *Tabular deep learning has a structural limitation: most models discard feature-type metadata and must relearn it from data.*

#### 2.6 Connective overuse
Do not start a sentence with "Moreover," "Furthermore," "Additionally," "In particular," "Ultimately," "Overall," "In essence," "Indeed," or "That said," whether or not the previous sentence did. Transitions belong inside the argument, not bolted onto it; let logic carry.
**Before:** *Moreover, the method is fast. Furthermore, it is simple. Additionally, it scales.*
**After:** *The method is fast and simple, and it scales to one million rows (Section 5).*

#### 2.7 Contribution-list cliches
Each contribution names a *specific* result, not a restatement of the abstract.
**Before:** *Our contributions are: (1) a novel method; (2) extensive experiments; (3) strong results.*
**After:** *We (1) introduce a metadata-aware encoder that reaches 0.91 AUROC vs 0.86 for the strongest baseline; (2) show it stays within 2 points under 20% label noise where the baseline drops 9; (3) release the benchmark.*

#### 2.8 Citation dumping
Cite the one or two works that matter and say why, not a bracketed list.
**Before:** *Many methods exist [3, 7, 9, 12, 15].*
**After:** *The closest prior method is TabNet [7], which encodes all features jointly; we instead condition on feature-type metadata.*

#### 2.9 Hedging: cut empty hedges, keep evidence-tied ones
Cut hedges that carry no specific, defensible qualification: "somewhat," "relatively," "fairly," "quite," "arguably," "to some extent," "in some sense," "it could be argued," "seems to," "may potentially." Quantify or cut. Keep evidence-tied hedging, which is correct and required: "suggests," "is consistent with," "we hypothesize that," "may indicate," "appears to" when the claim is genuinely uncertain. Hedge only where the uncertainty is real, and specify its source. Never upgrade a calibrated verb.
**Before:** *Performance is somewhat better and relatively robust.*
**After:** *Accuracy is 3 points higher and varies by less than 1 point across five seeds.*
*Wrong fix:* turning *"the results suggest X"* into *"the results prove X"*: this manufactures over-claiming. Keep the calibrated verb.

#### 2.10 Boilerplate emphasis and interpretive openers
**Watch:** "It is worth noting that", "It should be emphasized that", "Notably,", "Importantly,", "Interestingly,", "Surprisingly,", "Strikingly,". If it matters, the sentence shows it; if the fact is surprising, the reader will notice.
**Before:** *It is worth noting that, importantly, the gain holds across scenarios.*
**After:** *The gain holds across all three scenarios (Table 4).*

#### 2.11 Overlong, clause-stacked sentences
AI favors long sentences that chain three or four clauses with commas and "which", "that", "while", "with". Split them: one idea per sentence, and cut subordinate clauses that carry no weight. **Watch:** sentences past ~30 words, or with 3+ subordinate clauses.
**Before:** *Existing methods, though promising, are largely empirical, with unclear principles underpinning their behavior, which limits their reliability and further progress.*
**After:** *Existing methods stay empirical. Their principles are unclear, which limits reliability and progress.*

### Layer 3: Preserve these (do NOT over-correct)

A general humanizer flattens legitimate scholarly constructs. Keep them.

- **Evidence-tied hedging is correct and required** (2.9). Keep the calibrated verb when the claim is genuinely uncertain.
- **Passive voice** is fine when the actor is irrelevant: *"Samples were normalized to total protein."*
- **First-person plural "we"** is standard; do not rewrite to avoid it.
- **Semicolons and an occasional triple** are fine in moderation (Layer 1, item 2). Em dashes are the exception: remove them entirely (Layer 1, item 14), recasting with commas, colons, parentheses, or separate sentences.
- **Formal definitions, named methods/metrics, technical terms, equations, and symbols** stay verbatim.
- **Never invent, drop, or alter a number, equation, or citation.** Same content; preserve every cite key.

### Layer 4: Claim-evidence discipline

For every empirical claim, check (a) is it backed by a number, figure, table, or citation in the text, and (b) does the verb match the strength of that evidence?

- **Unbacked claim -> add the evidence pointer or soften.**
  *Before:* *Our method is more robust.*  *After:* *Our method's accuracy drops by 2 points under distribution shift, versus 11 points for the baseline (Figure 3).*
- **Verb stronger than evidence -> downgrade.**
  *Before:* *This demonstrates that our method is universally superior.*
  *After:* *On these three datasets, our method matches or exceeds the strongest baseline (Table 2).*
- **Vague magnitude -> a number or RANGE, attributed.**
  *Before:* *a large improvement.*  *After:* *a 2--6% improvement in balanced accuracy over the strongest baseline.*
  Prefer ranges (e.g., "2--6%") over single averaged values unless the averaging method is stated, and attribute each number to its method, metric, and baseline. When comparing, lead with the comparison against the strongest competitor, not the trivial baseline.

### Layer 5: Voice and venue matching

If the author supplies prior papers, read a sample first and note sentence rhythm, connective habits, level and placement of hedging, how they open sections, notation, and recurring phrasings, then match them. Match the venue's register too: this skill's own voice and register guidance above defines it (in a field skill, "Voice, Person, and Register"; in a journal skill, the journal profile, hard constraints, and observed deltas), and that guidance wins over any generic register default. Absent a sample, default to clean, precise, venue-appropriate prose, not the casual, opinionated voice of a general-purpose humanizer.

### Layer 6: Funding-proposal mode (NSF, NIH)

Apply this layer only to funding proposals. The structure notes below cover NSF and NIH; the same discipline applies to other funders (e.g., ERC, NFR). In a paper, nothing in this layer relaxes the rules above.

A proposal is not a paper. It is sold on **vision plus feasibility**, not on finished results, and reviewers score it. The register shift matters: ambition language that the paper layers would trim ("long-term goal", "pioneer", "transformative", "establish a foundation") is *appropriate and expected* here, provided a credible plan and evidence back it. So in proposal mode, **do not flatten the vision**; enforce a different discipline instead: **claim <-> feasibility**.

#### 6.1 Know the structure; the score lives in the first pages
Reviewers form a score from the opening, then skim the rest to confirm it. Put most editing effort there.
- **NSF.** A one-page **Project Summary** with the three review-criteria heads spelled out: **Overview**, **Intellectual Merit**, **Broader Impacts**, each self-contained. The Project Description then opens with **long-term vision -> this proposal's goal -> the gap -> the specific thrusts/aims -> the payoff**, ideally within the first 1--2 pages, with one overview figure. Broader Impacts must be substantive and integrated, never an afterthought.
- **NIH (R01).** The **Specific Aims page is the whole proposal in one page**, and is the most-read, most-decisive page. Standard arc: (1) opening: the problem, what is known, the **gap / critical need**; (2) the **long-term goal** and the **central hypothesis** with its rationale; (3) "**The objective of this application is...**" plus how the hypothesis was formed; (4) **2--3 Aims**, each a one-line goal + a phrase on approach + the expected outcome; (5) a **payoff** paragraph: what changes if it succeeds. Then **Significance, Innovation, Approach** as separately scored sections.

#### 6.2 First-3-pages primacy (edit these hardest)
By the end of page 1 (NIH Aims) or pages ~2--3 (NSF), the reader must already hold: the **hook** (why it matters, concretely), the **gap** (what is missing and the cost of the gap), the **central idea** (your approach in one sentence), the **aims/thrusts** (crisp and parallel), and the **payoff**. If any is missing or buried, fix that before touching later sections. A reviewer unconvinced by page 3 does not recover on page 10.

#### 6.3 Proposal-specific weak moves to fix
- **Vague importance.** *Watch:* "this is an important/timely problem", "X has many applications".
  **Before:** *Understanding this problem is critically important.*
  **After:** *Without bounds on how measurement noise propagates to diagnosis, clinical models are tuned by trial and error, the inefficiency this proposal removes.*
- **Method-as-aim** (an aim naming a technique instead of a question or outcome).
  **Before:** *Aim 2: Apply transfer learning to the dataset.*
  **After:** *Aim 2: Determine whether fusing wearable and lab signals improves early detection, and for which patient subgroups it helps or hurts.*
- **Dominoed aims** (Aim 2/3 collapse if Aim 1 fails; reviewers flag this as fragile). *Fix:* phrase aims as **parallel and independently valuable**; where one depends on another, state the fallback.
- **Ambition without feasibility.** Every bold claim needs a footing: preliminary data, a prior result/publication, a classical theorem you build on, or a collaborator/letter. *Fix:* attach the evidence beside the claim ("our preliminary result in Fig. X shows...", "building on a classical minimax lower bound...").
- **Boilerplate Broader Impacts / training plan.** *Watch:* "we will mentor students and disseminate via talks and papers." *Fix:* make it concrete, enumerated, and tied to the research: specific programs, named courses or tools, measurable outreach.
- **Hedged central hypothesis.** The Aims-page hypothesis is a falsifiable commitment, not "we will explore whether possibly...". Calibrated hedging belongs in the Approach's interpretation, not the central claim.

#### 6.4 Preserve and deploy (funded-proposal craft)
These read as strength; keep or add them rather than editing them out.
- **Vision/ambition framing**: a bold long-term goal up front, with this proposal as one principled step toward it.
- **Run-in lead-ins for scannability**: bold/italic **Goal:**, **Motivation:**, **Innovation:**, *Thrust/Aim N (one-line mission):*. Reviewers skim; visible structure earns time.
- **A concrete running example or protagonist** to make an abstract method vivid and consistent across aims.
- **Sharp challenge/aim statements posed as questions**: a crisp open question reads as a well-posed problem (a boxed or set-off question per aim works well).
- **Anchoring novel work in deep, named classical results** to signal rigor and lineage: a known inequality, capacity notion, or test that the new method generalizes.
- **Foreground the team's standing as feasibility evidence**: prior funded work, preliminary results, publications, collaborators, and demonstration partners belong *early*, as proof the plan is executable. A real track record is evidence, not boasting; place it where it de-risks the aims. *(Use only the PI's own real, supplied record; never invent funding, results, partners, or letters.)*

#### 6.5 Claim <-> feasibility (the proposal analog of Layer 4)
For every aim and promised outcome, check: is the ambition matched by a credible means, such as preliminary data, a prior method, a classical foundation, a collaborator, or staged de-risking? If yes, keep the ambitious verb. If no, attach the missing evidence or scale the claim to what the plan supports. Never invent preliminary results, prior funding, partners, or letters; if the support does not exist, flag the gap for the author rather than papering over it.

### Output

Return the cleaned text plus a short change report: patterns removed (by type), claims softened or given evidence pointers, and any voice/venue notes. Confirm that no number, equation, or citation was altered.
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
