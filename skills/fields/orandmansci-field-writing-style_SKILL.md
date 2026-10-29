---
name: orandmansci-field-writing-style
description: >
  Normative academic writing conventions for the OR&MANSCI field,
  derived exclusively from ABS 4* and ABS 4 journals. Use this skill
  as a baseline prior when writing for any journal in the OR&MANSCI field.
  Trigger on phrases like "write for a OR&MANSCI journal", "what does
  OR&MANSCI writing look like", "field norms for OR&MANSCI", or when a
  journal-specific skill references this baseline. Superseded by
  journal-specific skills where they conflict.
---

# Field Writing Style: OR&MANSCI

## Scope and Intended Use

This baseline captures the shared writing conventions of ABS 4* and ABS 4 journals in the Operations Research and Management Science (OR&MANSCI) field. It covers macro structure, voice, argumentation, methods conventions, citation norms, and hedging patterns as observed across the field's leading outlets.

It does NOT cover journal-specific formatting requirements, word or page limits, submission checklists, publisher templates, or statistical reporting rules mandated by individual journals. Journal-specific skills take precedence when they conflict with this baseline.

The OR&MANSCI field spans a spectrum from purely theoretical/mathematical contributions to empirically grounded computational and applied work. Some conventions differ modestly across this spectrum; where they do, the range is noted.

---

## Typical Article Structure

Leading journals in this field expect a clear, standardised structure. The near-universal section set, in canonical order, is:

1. **Abstract** — brief statement of problem, approach, and main finding
2. **Introduction** — motivation, gap identification, contributions, paper roadmap
3. **Model / Preliminaries / Framework** — formal problem setup and notation
4. **Main Analysis** — theorems, algorithms, or empirical methodology (may be split across multiple numbered sections organised by topic)
5. **Results / Experiments / Numerical Study** — formal results, proofs (or proof sketches), computational validation
6. **Conclusion** — synthesis, limitations, future directions
7. **References**
8. **Appendix / Online Supplement** — full proofs, robustness checks, additional experiments

**Related Work** is almost always present but its placement varies: it appears either as a dedicated subsection of the Introduction (more common in Management Science-style papers) or as a standalone section immediately after the Introduction (more common in theoretically focused papers). A separate, free-standing Discussion section is rare; interpretive discussion is typically woven into the Results sections or folded into the Conclusion.

Appendices are near-universal in ABS 4*/4 work and serve a distinct function: complete proofs and extensive robustness tables are routinely moved there to maintain readability in the main body. Reviewers in this field expect main-body theorem statements and empirical findings to be self-contained, with the appendix providing the full evidentiary detail.

---

## Voice, Person, and Register

At the ABS 4*/4 level, reviewers expect consistent use of **first-person plural** ("we"). The authorial "we" appears throughout — in problem framing, contribution claims, algorithmic descriptions, and interpretation of results. Impersonal or third-person constructions are reserved for definitional passages ("let X denote…") or when describing prior work ("prior work shows…").

**Active voice dominates.** Passive constructions appear selectively: in formal theorem statements, when describing procedures that logically require objectivity ("samples are drawn from…"), and when attributing results to prior literature. The overall register is formal, precise, and technically dense.

The field's formality is high and consistent across sections. Colloquial language, rhetorical questions addressed to the reader, and motivational narrative flourishes are generally absent after the opening paragraphs of the Introduction.

---

## Sentence and Paragraph Style

Sentences are typically medium to long, with technical and mathematical content integrated directly into prose. Short emphatic sentences are rare and tend to appear only to foreground a key result. Paragraphs are moderately dense: each makes a single logical move but typically sustains that move for several sentences before transitioning.

Mathematical notation is woven into running text throughout the paper — this is a field-wide norm, not a feature of any single subgenre. Readers are expected to process formal notation fluently. Unnecessary paraphrase of mathematical content into plain language is avoided; instead, authors offer brief intuitive "sketch" remarks immediately following formal statements, particularly for major theorems.

---

## Argumentation and Rhetorical Moves

The Introduction follows a structure consistent with the CARS (Create A Research Space) model, executed with field-specific precision:

1. **Establish the territory**: The opening situates the problem in a practically or theoretically significant domain. This is typically brief — one to three paragraphs — and often cites foundational or recent high-profile work to anchor the relevance claim.

2. **Identify the gap**: The authors identify a specific limitation of existing work — a missing assumption, an unanalysed regime, an open question, or a condition under which prior methods fail. The gap is stated precisely, often in technical terms, not in vague "little is known" language. Prior work is acknowledged respectfully and its achievements credited before its limits are noted.

3. **Occupy the niche (state contributions)**: Contributions are stated explicitly and usually collected in a dedicated paragraph or subsection. At the ABS 4*/4 level, reviewers expect contributions to be stated as enumerated claims, each claim asserting something specific and verifiable (a theorem, a bound, an algorithm with a guarantee, an empirical finding). Vague or broadly framed contribution statements are atypical.

4. **Paper roadmap**: The Introduction closes with a brief roadmap — one paragraph or a short list — that maps sections to contributions.

Papers do not open with rhetorical grand claims about the importance of OR generally; they move quickly to the specific problem. The gap is typically framed as a gap in formal analysis or theoretical understanding, not merely as a gap in the applied literature.

At the paper's close, the Conclusion reconnects findings to the gap stated in the Introduction, provides a clear summary of what was established, acknowledges limitations of the framework or model, and typically closes with explicit pointers to future research directions.

---

## Methods Conventions

Leading journals in this field expect **high procedural and formal detail**. The methods section (or model section) is expected to be fully self-contained: all notation introduced here should be consistent with what appears in proofs and results.

Tense conventions follow a consistent pattern:
- **Present tense** for problem setup, model definitions, and algorithmic descriptions ("the algorithm selects…", "we define…")
- **Past tense** for reporting experimental execution and empirical estimation steps ("we estimated…", "we trained the model on…")
- **Present tense** for theorem statements and mathematical properties, regardless of when they were derived

The expected level of procedural detail is high. Algorithms are typically presented with pseudocode or formal step-by-step notation. Assumptions are stated explicitly and numbered. Conditions for results are stated with precision.

For theoretical papers, robustness is demonstrated through corollaries and extensions that relax assumptions, through numerical experiments that validate theoretical bounds, or through appendix sections comparing performance across parameter configurations. For empirical papers, robustness is demonstrated through alternative specifications, sensitivity analyses, or placebo/falsification exercises. Reviewers in ABS 4*/4 outlets expect robustness evidence to be substantive, not pro forma.

---

## Results and Reporting Norms

The boundary between reporting and interpretation differs by subgenre:

- In **theoretical papers**, results are formal theorem or proposition statements. Prose interpretation appears immediately after each major result as "remarks" or inline discussion, explaining what the bound implies or when the condition is relevant. Tables appear primarily in numerical experiment sections.
- In **empirical and computational papers**, tables are the primary vehicle for quantitative results. Prose accompanies tables to highlight key comparisons, explain statistical significance, and interpret direction of effects. Prose does not duplicate the table; it adds meaning.

Statistical narration in empirical papers is precise: specific statistics (e.g., ratio values, regret bounds, percentage improvements) are reported in prose rather than left to the reader to extract from tables. However, the narrative remains analytical — results are not merely read aloud but evaluated against the research question.

Null or mixed results are handled directly. When a method performs similarly to a benchmark or fails under a particular condition, this is reported and interpreted as informative about the model or algorithm's scope, not obscured.

---

## Discussion and Conclusion Norms

In OR&MANSCI, a separate free-standing Discussion section is the exception rather than the rule. Interpretation of findings is typically integrated into the Results sections themselves. The Conclusion section synthesises the paper's overall contribution, explicitly reconnects to the gap stated in the Introduction, and presents limitations.

Limitations are framed constructively: as boundary conditions of the model or analysis rather than as failures. Future research directions are stated explicitly and specifically — not as a generic call for more work but as identified open problems or extensions that the current framework does not yet handle.

Practice varies on whether Discussion and Conclusion are merged into one section or separated. Merged "Discussion and Conclusion" sections are common in shorter or more applied papers; longer theoretical papers sometimes keep them distinct, with Discussion synthesising across theoretical results before Conclusion closes the narrative.

---

## Citation and Literature Engagement

Citation density varies predictably by section:

- **Introduction and Related Work**: high density. The Introduction establishes scholarly territory through dense citation, with references clustered around foundational results, recent advances, and the specific gap being targeted. The Related Work subsection is systematically organised — typically by research stream rather than chronologically — and is expected to be comprehensive within the paper's scope.
- **Methods/Model sections**: moderate. Citations appear to acknowledge foundational frameworks, established algorithms, or established problem formulations that the paper builds on. Original derivations are not cited; assumptions and definitions are.
- **Results/Theorem sections**: low. Proof sections and theorem statements are largely self-referential; citations to external sources are minimal.
- **Appendix**: low to minimal.

**Direct quotation is essentially absent** from OR&MANSCI writing. All engagement with prior literature is through paraphrase, summarisation, and attribution. The field does not cite to quote; it cites to position.

Disagreement with prior work is handled diplomatically. Authors acknowledge what prior work achieves before identifying its limitations. Framing such as "while X establishes Y, it does not address Z" is normative. Adversarial framing or strong negative evaluation of prior work is rare at the ABS 4*/4 level.

---

## Hedging and Epistemic Caution

Overall epistemic caution in OR&MANSCI is **low to moderate**, but the form of caution differs substantially between subgenres:

- In **mathematical/theoretical papers**, verbal hedging (words like "might," "appears," "seems") is largely absent from claims about formal results. Uncertainty is expressed through the mathematical structure itself: probability statements, explicit assumption conditions, bounded-guarantee formulations, and scoped theorem premises. Claiming a result "under Assumption 3" is the field's idiomatic form of epistemic qualification.
- In **empirical and applied papers**, moderate hedging appears in claims about external validity and generalisation: phrases such as "in our experimental setting," "subject to the modelling assumptions," and "under the conditions studied" are common and expected. Claims are confident within the established scope, hedged at the boundary of that scope.

The phrase "to the best of our knowledge" is used specifically and sparingly — to flag the first formal treatment of a result or problem, not as a general disclaimer. Contribution claims are stated assertively; epistemic hedging does not extend to the core contribution statements.

---

## What This Baseline Does NOT Specify

The following are explicitly excluded from this baseline. They belong in journal-specific skills:

- Word limits, page limits, or column formatting requirements
- Required or prohibited section names
- Publisher-mandated formatting (referencing style, font, margins, template)
- Submission system requirements, cover letter conventions, or data availability statements
- Journal-specific statistical reporting standards (e.g., required disclosure of standard errors, specific hypothesis-testing conventions)
- Whether a separate "Data" section is expected
- Specific conventions around ethics statements or replication packages
- The balance between theory and computation expected by any specific journal
- Online supplement vs. appendix conventions specific to any journal

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

| Journal | ABS Rating | Articles consulted |
|---------|------------|-------------------|
| Management Science | 4* | 4 |
| Operations Research | 4* | 2 |
| Mathematical Programming | 4 | 1 |
| European Journal of Operational Research | 4 | 2 |