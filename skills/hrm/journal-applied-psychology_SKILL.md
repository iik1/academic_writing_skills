---
name: journal-applied-psychology-writing-style
description: >
  Journal-specific writing conventions for Journal of Applied Psychology
  (ABS 4*, HRM). Use alongside hrm-field-writing-style when available,
  which provides the field baseline. This skill records journal-specific
  requirements. Trigger on phrases like "write for Journal of Applied Psychology",
  "submit to Journal of Applied Psychology", "match Journal of Applied Psychology style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Applied Psychology

## Journal Profile
- **ABS 2024 Rating:** 4*
- **Field:** HRM
- **Publisher:** American Psychological Association (APA)
- **Scope:** Original investigations contributing new knowledge to applied psychology (excluding clinical, applied experimental, and human factors)
- **Guidelines URL:** https://www.apa.org/pubs/journals/apl
- **Field baseline:** hrm-field-writing-style (NOT YET AVAILABLE - deltas cannot be assessed)
- **Articles spot-checked:** 0 (access restricted; analysis based on comprehensive author guidelines only)

---

## Hard Constraints (Author Guidelines)

> These are enforced requirements from the journal's manuscript preparation instructions and author agreement checklist.

### Structure

**ENFORCED** - Manuscripts must be categorized into one of five types, each with specific methodological reporting requirements:

1. **Primary Quantitative Studies** - Standard empirical research
2. **Meta-Analytic Research** - Requires PRISMA flowchart
3. **Qualitative and Mixed-Methods Studies** - Must specify qualitative approach used
4. **Machine Learning Studies** - Requires detailed algorithm documentation
5. **Simulation and Computational Modeling Studies** - Must share all code

All manuscripts must include a **"Transparency and Openness" subsection** within the Method section explaining compliance with TOP (Transparency and Openness Promotion) guidelines.

### Length

No specific word or page limits stated in guidelines.

### Abstract

Format and word limit not specified in the guidelines reviewed. Follow APA 7th edition standards (structured abstracts with Introduction, Method, Results, Discussion/Conclusions).

### Citations

**ENFORCED** - APA Style (7th edition as of 2026, though guidelines reference 6th edition).

Must cite:
- Statistical software packages with version numbers
- All measurement scales with either sample items OR full content (if copyright obtained)
- All adapted/translated measures with modification details

### Headings

**ENFORCED** - Must follow APA Style heading conventions (5-level heading system).

### Tables and Figures

**ENFORCED** - Extensive requirements:

- Means, SDs, correlations, and reliability coefficients for ALL measured variables (including controls and sociodemographic characteristics)
- Full and observed scale range, scale anchors, number of items for all measures
- Sample size for each analysis
- How dichotomous/categorical variables were coded
- Standard errors, confidence intervals, and/or test statistics with p-values
- Text must be checked against tables for consistent statistical reporting (manual or via statcheck.io)

For moderation plots:
- Use relative language ("higher" vs. "lower"), not absolute ("high" vs. "low")
- Report raw values for levels selected
- Scale appropriately to represent effects

### Formatting

**ENFORCED** - Double-space all copy.

### Transparency and Reproducibility Requirements

**ENFORCED** - This journal has among the most stringent transparency requirements in management/HRM:

#### Data and Code Sharing
- Must retain raw data minimum 5 years post-publication
- Must comply with APA Ethics Code Standard 8.14a (sharing data for verification)
- For machine learning: provide code when possible
- For simulation/modeling: share all code and data

#### Methodological Reporting - Primary Quantitative Studies

Must report:
- Sampling plan including recruitment, power analysis, inclusion/exclusion criteria, cases excluded
- Final sample size for each analysis + response rate
- Missing data treatment at scale and item levels
- For experiments: sample size per condition; within-subjects: correlations between conditions
- For multilevel: sample size at each level + descriptive statistics at each level
- Year data were collected
- For longitudinal/ESM: rationale for time intervals
- Manipulation checks and how failed manipulations were handled

#### Inclusive Reporting

**ENFORCED** - Special requirements exceeding typical HRM journals:

- Do NOT use race and ethnicity interchangeably
- Report percentage in each unique racial/ethnic group (not "percent non-White")
- Use research-question-relevant group as reference (NOT default to White)
- Provide interpretation of race/ethnicity within research context/nation
- Report sociodemographic info (age, sex, race/ethnicity, tenure) AND research context (country, industry, occupation, job, tasks)
- Must follow JARS-REC (Journal Article Reporting Standards for Race, Ethnicity, and Culture)

#### Statistical Reporting

**ENFORCED** - Must report:

- Full model testing results (e.g., for 3-way interaction, report ΔR² over all 2-way interactions and main effects)
- For mediation: a, b, c paths + indirect and total effects
- If unstandardized: include intercepts/constants
- Effect sizes with confidence intervals preferred (r, R², ΔR², Cohen's f², d, η², odds ratios)
- For multilevel: aggregation models, centering decisions (justified), ICCs, variance components
- Estimation procedures for advanced methods (df corrections, bootstrapping, Bayesian intervals)
- Skew and kurtosis when appropriate
- Do NOT convert continuous to binary/categorical without sufficient rationale

#### Meta-Analysis Specific

**ENFORCED**:
- PRISMA flowchart required
- Inter-coder agreement/reliability, qualifications, training, resolution methods
- If psychometric corrections applied: method, artifact distributions, order of corrections, justification
- Primary study information in appendix or online (OSF preferred)
- Publication bias check reported
- Use confidence/credibility intervals, not NHST, for interpretation

#### Qualitative/Mixed-Methods Specific

**ENFORCED**:
- Specify approach (grounded theory, phenomenological, thematic analysis, etc.)
- Data collection procedures, recruitment, protocols, time in field
- Unit of analysis specified
- Coding taxonomy development, number of coders, training, agreement (%, kappa)
- Direct quotations/observations/raw data examples
- Follow APA JARS qualitative and mixed-methods guidelines

#### Machine Learning Specific

**ENFORCED**:
- Data preprocessing/feature engineering described
- Missing data and outlier handling
- Variable distributions
- Class imbalance methods (if applicable)
- Algorithm nature, model selection, parameters, cross-validation
- Neural networks: layer architecture, nodes per layer
- Model tuning: parameters tuned, value ranges, selection method
- Validation: internal and external, multiple metrics
- LLM use: model, prompts, generation/evaluation process
- Cite software and provide code when possible

### Explicit Prohibitions

**ENFORCED**:

- Do NOT simply state "Brislin (1970, 1984, 1986) recommendations were followed" for translation—must describe process in detail
- Do NOT use absolute language for moderation plots ("high" vs. "low")
- Do NOT convert continuous data to binary/categorical without rationale
- Do NOT default to White participants as reference group
- Do NOT use race and ethnicity interchangeably
- Do NOT report "percent non-White"
- Masked review required—do NOT include author-identifying information in manuscript

### Submission Requirements

**ENFORCED**:

- Cover letter must contain all author names and contact info
- Must disclose multiple uses of same dataset
- Must obtain institutional approval for human subjects research
- Must obtain copyright permission for adapted materials
- Copyright transfers to APA upon acceptance
- Checklist must appear on first page of manuscript

---

## Observed Deltas from FIELD_SKILL

**NOT APPLICABLE** - The HRM field baseline (hrm-field-writing-style) has not yet been generated. Delta analysis cannot be performed. Once the field baseline is available, this section should be populated by comparing journal-specific requirements against field norms.

---

## Provisional Observations (Pending Field Baseline)

The following patterns may represent journal-specific emphasis, but cannot be confirmed as deltas without field baseline:

### Transparency Requirements
This journal appears to have exceptionally detailed transparency and reproducibility requirements, including mandatory "Transparency and Openness" subsection, specific data retention timelines, and code-sharing expectations. Classification pending field baseline.

### Inclusive Reporting Standards
Extensive race/ethnicity reporting requirements via JARS-REC may exceed typical HRM journal standards. Classification pending field baseline.

### Methodological Pluralism
Explicit separate checklists for five research paradigms (quantitative, meta-analytic, qualitative/mixed, machine learning, simulation) suggests unusual breadth. Classification pending field baseline.

### Statistical Detail
Extremely granular statistical reporting requirements (e.g., mandatory skew/kurtosis, ICC reporting, full model hierarchies) may exceed field norms. Classification pending field baseline.

---

## Common Pitfalls

Based on the extensive checklists, authors commonly fail to:

1. **Include the "Transparency and Openness" subsection in Method** - This is a unique requirement easily overlooked

2. **Report inclusive demographics properly** - Using "percent non-White," conflating race/ethnicity, or defaulting to White reference groups are explicitly prohibited

3. **Provide sufficient translation detail** - Cannot simply cite Brislin; must describe translator qualifications, process, disagreements

4. **Check tables against text** - Inconsistent statistical reporting between tables and narrative is common enough the journal recommends statcheck.io

5. **Report full model hierarchies** - Authors often report only final models, not the full sequence (main effects → 2-way → 3-way)

6. **Use absolute language in moderation plots** - Must use "higher/lower" not "high/low"

7. **Disclose multiple uses of same dataset** - Related manuscripts using overlapping data must be disclosed in cover letter

8. **Include the author agreement checklist on page 1** - Failure results in desk rejection

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
| https://www.apa.org/pubs/journals/features/apl-manuscript-checklist.pdf | Manuscript preparation instructions (6 pages) | Direct fetch (PDF) |
| https://www.apa.org/pubs/journals/features/apl-submission-checklist.pdf | Author agreement checklist | Direct fetch (PDF) |
| https://www.apa.org/pubs/journals/apl | Journal home page | Web search |
| APA JARS Guidelines (quantitative) | Referenced standard | http://dx.doi.org/10.1037/amp0000191 |
| APA JARS Guidelines (qualitative/mixed) | Referenced standard | http://dx.doi.org/10.1037/amp0000151 |
| APA JARS-REC | Referenced standard | https://apastyle.apa.org/jars/race-ethnicity-culture |

**Note:** Article spot-checking (Phase 2) was not completed due to paywall/access restrictions. This skill is based entirely on comprehensive author guidelines, which provide exceptional detail (6-page methodological checklist). Once field baseline is available and article access obtained, this skill should be updated with observed deltas and practice patterns.