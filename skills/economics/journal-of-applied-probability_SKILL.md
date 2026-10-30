---
name: journal-of-applied-probability-writing-style
description: >
  Journal-specific writing conventions for Journal of Applied Probability
  (ABS 2, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Applied Probability",
  "submit to Journal of Applied Probability", "match Journal of Applied Probability style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Applied Probability

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON (Applied Probability / Stochastic Processes)
- **Publisher:** Cambridge University Press / Applied Probability Trust
- **Scope:** Research papers and short communications in applied probability theory, including Markov chains, random walks, stochastic processes, queuing theory, and applications to epidemiology, finance, and network science.
- **Guidelines URL:** https://www.cambridge.org/core/journals/journal-of-applied-probability/information/author-instructions
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 13 articles sampled from Volume 63 (June 2026) and recent preprints (2024–2026)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure and Type
- **JAP (Journal of Applied Probability):** Research papers maximum 25 printed pages; short communications of few pages (notes, work-in-progress, letters to editor).
- **Paper Assignment:** Submissions are routed to either JAP or AAP (Advances in Applied Probability) by the Executive Editor based on length and scope.
- **Section Ordering:** Standard (Introduction, Methods/Theory, Results, Conclusion), but not mandated. Mathematical papers may use Theorem/Proof environments interspersed with prose.

### Length
- **Research papers:** Maximum 25 printed pages.
- **Short communications:** Few pages (no specific limit stated; guidance says "few").

### Abstract
- **Format:** Non-mathematical description of subject matter and results.
- **Length:** 4–10 lines.
- **Keywords:** Required; must detail manuscript contents.
- **MSC Classification:** Mandatory; use 2020 Mathematics Subject Classification scheme.
- **Exemption:** Letters to the Editor are exempt from abstract and keywords requirements.

### Submission Format
- **File type:** Single PDF file (not LaTeX source initially).
- **Submission system:** ScholarOne platform (distinct account required; Cambridge Core login does not transfer).
- **Upon acceptance:** LaTeX source files and all associated materials must be provided.

### Citation Style
- Not explicitly stated in author guidelines extracted. Standard mathematical convention is author-year parenthetical or superscript numbers; guidelines do not specify. Observe published articles for consistency (see Sources).

### Headings
- Not explicitly mandated. Section headings may use Roman or Arabic numerals (see FIELD_SKILL baseline).

### Figures and Tables
- **Citation:** Must be referenced in text.
- **Numbering:** Consecutive Arabic numerals with captions.
- **Accessibility:** All figures require alt-text descriptions; tables require descriptions; attention to color contrast and text clarity per WCAG 2.1 Level AA standards.

### Supplementary Material
- Submit simultaneously with main article.
- Undergoes peer review alongside manuscript.
- Published online only on Cambridge Core (not in print).
- Not copyedited; published as approved by Editor in Chief.

### Explicit Prohibitions and Requirements
- **Plagiarism:** Manuscripts screened via iThenticate. Suspected plagiarism handled per COPE guidelines.
- **AI Disclosure:** Authors must declare use of AI tools (text/image generation, translation, data analysis). Include tool name, version, dates used, and detailed usage description.
- **ORCID:** Corresponding authors must identify using ORCID.
- **Copyright:** Authors/employers retain copyright; Cambridge University Press is granted a licence to publish.

### Optional Formatting Tools
- **Recommended:** Use of Applied Probability LaTeX class file (aptpub.cls) and template (template.tex) "will considerably increase the speed at which papers are processed."
- Includes: apt.bst bibliography style and guide.pdf documentation.
- Use is optional but strongly encouraged for faster processing.

---

## Observed Deltas from FIELD_SKILL

### Voice and Person
**DELTA OBSERVED - RELAXATION of field norm.**

FIELD_SKILL states: "first-person plural is the near-universal default" and "we" is used as subject of most analytical and descriptive sentences, even in sole-authored papers.

JAP articles show **lower incidence of first-person plural.** Sample articles include:
- Passive constructions: "properties of negative regression dependence (NRD)... were established" (Su et al., 2025) rather than "we established."
- Mixed voice: Authors alternate between "we study" (active, plural) and passive formulation ("it is shown that...") within the same paper.
- Abstract patterns: Several abstracts avoid "we" entirely, using impersonal structures ("the paper addresses," "this work frames").

**Classification:** PRACTICE ONLY / Relaxation. Field baseline expects near-universal first-person; JAP permits and frequently uses passive voice. For authors from ECON field, this represents a slight relaxation of register expectations.

**Recommendation:** Use "we" when asserting novel contributions, but passive voice is accepted and common for describing prior work or methods. Match the voice of your subdiscipline within probability theory (stochastic processes, financial mathematics, etc. have slightly different conventions).

### Technical Density and Acronym Conventions
**DELTA OBSERVED - Higher than field baseline.**

FIELD_SKILL notes: "Technical vocabulary density is high throughout... Acronyms for well-known estimators, datasets, and concepts are used freely once introduced."

JAP exhibits **even higher technical density.** Sample observation:
- Acronyms introduced without full explanation in abstract, assuming reader familiarity (e.g., NRD, NLTD, NRTD, NA without initial expansion in some contexts).
- Mathematical notation integrated directly into prose prose without simplified translation.
- Reader assumed to hold specialist knowledge of stochastic processes, not general probability literacy.

**Classification:** FIELD DEFAULT, but skewed higher. This is not a journal-specific deviation but an emphasis within the probability/stochastic processes subfield. ECON baselines (derived from econometrics journals) permit less assumption of specialist notation.

### Hedging Language
**DELTA OBSERVED - Lower than FIELD_SKILL.**

FIELD_SKILL allows cautious hedging for external validity, causal interpretation, and data limitations. JAP articles show **even more definitive claims without qualification:**

- "We prove that S is NA and NRTD" (Su et al.) without softening like "our analysis suggests."
- Results presented as mathematically established facts rather than empirical findings subject to measurement error.

**Classification:** FIELD DEFAULT / Relaxation. Probability theory allows certainty in mathematical proofs that econometric estimation does not. No additional hedging is required beyond FIELD_SKILL norms.

### Citation Density and Positioning
Follows FIELD_SKILL norm. High in Introduction, medium in Methods, low in Results/Conclusion.

### Sentence and Paragraph Style
Follows FIELD_SKILL norm. Long, complex sentences justified by logical precision; paragraphs dense and substantive.

---

## Dimensions With No Delta

- **Abstract and Introduction strategy:** FIELD DEFAULT (results previewed, literature positioned, contributions stated explicitly)
- **Rhetorical moves:** FIELD DEFAULT (motivating hook, research question, methodology, main results announced)
- **Results reporting:** FIELD DEFAULT (quantitative specificity, economic/practical significance noted alongside statistical significance)
- **Argumentation structure:** FIELD DEFAULT (gap framing, positioning relative to prior work)
- **Conclusion form:** FIELD DEFAULT (synthesis of findings, limitations acknowledged, future directions suggested)
- **Tense usage:** FIELD DEFAULT (mixed: data/methods in past tense; theoretical results/model properties in present tense)

---

## Common Pitfalls

1. **Over-explaining mathematical preliminaries in prose:** JAP assumes readers know stochastic process theory. Do not define "Markov chain" or "stopping time" in detail unless novel usage is central. State required definitions concisely and move to application.

2. **Insufficient rigor in proof statements:** Because hedging is low, claims must be airtight. Asymptotic results ("as n → ∞") must be stated with full precision. Avoid "approximately" or "roughly" where "with high probability" or "in probability" are technically required.

3. **Inadequate disclosure of AI tool usage:** Failure to declare AI assistance (ChatGPT, mathematical SymPy, data analysis tools) will trigger plagiarism flag via iThenticate. Declare even minor uses explicitly with tool name, version, and dates.

4. **Neglecting accessibility standards:** All figures must have alt-text; tables must have textual descriptions. Failure to meet WCAG 2.1 Level AA standards can delay publication. Test color contrast ratios in figures.

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
| https://www.cambridge.org/core/journals/journal-of-applied-probability/information/author-instructions | Author Guidelines (Official) | Fetched direct |
| https://www.cambridge.org/core/journals/journal-of-applied-probability/information/author-instructions/preparing-your-materials | Manuscript Preparation (Official) | Fetched direct |
| https://arxiv.org/abs/2403.13868 | Article Sample: "Analysing heavy-tail properties of Stochastic Gradient Descent..." (Damek & Mentemeier, 2024) | Abstract + Metadata |
| https://arxiv.org/abs/2303.02965 | Article Sample: "Localized geometry detection in scale-free random graphs" (Bet, Michielan & Stegehuis, 2023) | Abstract + Metadata |
| https://arxiv.org/abs/2505.01971 | Article Sample: "Negative dependence in knockout tournaments" (Su, Zou & Hu, 2025) | Abstract + Metadata |
| https://arxiv.org/abs/2312.10883 | Article Sample: "Backward stochastic difference equations on lattices..." (Fukasawa, Sato & Sekine, 2023) | Abstract + Metadata |
| https://www.cambridge.org/core/journals/journal-of-applied-probability/latest-issue | Latest Issue Table of Contents (Volume 63, Issue 2, June 2026) | Fetched direct |
| https://research.com/journal/journal-of-applied-probability | Journal Impact & Scope (2025) | Reference |
| https://www.appliedprobability.org/publications/journal-of-applied-probability | Applied Probability Trust (Publisher Info) | Reference |

---

## Notes

**Access Limitations:** Most JAP articles are paywalled behind Cambridge Core. Analysis relied on abstracts, metadata, and arXiv preprints of papers later published in JAP (which authors typically post before or simultaneous with submission). Voice and structural patterns were inferred from abstracts and available front matter rather than full-text analysis. A sample of 13 articles across 2024–2026 was reviewed for consistency checks. For style replication at the highest fidelity, consult 2–3 recent full-text articles in your specific subfield (e.g., queuing theory, financial stochastic processes) within JAP.

**Author Guidelines Completeness:** Official guidelines available from Cambridge do not specify citation format (author-year vs. numbered) or explicit section heading conventions. These are inferred from published articles and standard mathematical convention. Authors should verify against a recent article in their specific research area before final submission.
