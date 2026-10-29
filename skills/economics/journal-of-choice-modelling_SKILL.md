---
name: journal-of-choice-modelling-writing-style
description: >
  Journal-specific writing conventions for Journal of Choice Modelling
  (ABS 1, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Choice Modelling",
  "submit to Journal of Choice Modelling", "match Journal of Choice Modelling style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Choice Modelling

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** ECON
- **Publisher:** Elsevier
- **Scope:** Publishes theoretical and applied papers on choice modelling. Not restricted to one application domain (transport, marketing, health, environment, etc.); the majority of papers use discrete choice models but other methods are welcome. Papers must make either a methodological contribution or present an innovative application.
- **Guidelines URL:** https://www.sciencedirect.com/journal/journal-of-choice-modelling/publish/guide-for-authors (403 on direct fetch; content recovered via search-engine snippets)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 10 (abstract/front-matter level, via RePEc/IDEAS, ScienceDirect snippets, White Rose repository, and SSRN): Cazor et al. "A smooth bounded choice model" (2025); Tjiong et al. "Capturing zero-price effects in stated choice surveys" (2025/2026); McCarthy, Naqavi & Karlström "Recursive logit models for dynamic versus sequential trip chaining" (2025); Büscher & Bauer "Using Lagrange multiplier type tests to detect structural intra-person heterogeneity" (2025); Xhakollari, Asioli & Nayga "Mitigating hypothetical bias in choice experiments" (2025); Kamal & Farooq "Ordinal-ResLogit" (2024) + corrigendum; Gonzalez Sepulveda et al. "The impact of violations of expected utility theory on choices" (2024); Armantalab, Ghosh & Hawkins "Potential for electric vehicle adoption in Midwest US States" (2026); Seong, Choi & Koo "Semi-dynamics of electric vehicle adoption" (2026); Al-Haideri, Ismail & Weiss "Cyclists' crossing behaviour at roundabouts" (2026).

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No single mandated section template beyond the journal's article-type distinctions (see below). Standard IMRaD-style structure is expected for full research papers, consistent with FIELD_SKILL.

**Distinctive: five accepted article types**, not just full-length research papers:
1. **Standard research papers** — the default, methodological contribution or innovative application.
2. **Research notes** — shorter pieces: technical notes on a specific model specification, survey design, data collection, or estimation issue, or discussion pieces raising a concern in applied work. No fixed length limit; authors are pointed to Volume 21 for examples.
3. **Software papers** — presenting substantial choice-modelling estimation/application software or survey-design/data-collection packages that improve on, or usefully emulate, existing tools.
4. **Data papers** — reporting innovative data collection efforts or describing benchmarking datasets.
5. **Review papers** — full-length literature reviews within JOCM's scope; not required to contain new research, but must provide new synthesis, critique, or gap identification, not just a survey recap.

This five-way typology is a JOCM-specific submission category system with no equivalent in FIELD_SKILL, which only discusses empirical/theory paper structures.

### Length
No explicit overall word/page cap found in accessible guidance beyond the abstract limit below. Research notes are explicitly shorter than full papers but with "no specific length limit imposed."

### Abstract
- Unstructured, single paragraph.
- Word limit: 250 words maximum (stricter/more explicit than FIELD_SKILL, which does not specify an abstract length).
- Must stand alone (often displayed separately from the article).
- Avoid references; if unavoidable, cite author(s) and year(s) (author-year, consistent with FIELD_SKILL).
- Avoid non-standard abbreviations; define at first use if essential.

### Citations
Author-year style, consistent with FIELD_SKILL. No journal-specific deviation found.

### Headings
No distinctive numbering or naming convention found beyond standard practice. Follows FIELD_SKILL norm.

### Tables and Figures
No JOCM-specific rules found beyond standard Elsevier formatting (not journal-distinctive; omitted as out of scope per the "no fabrication" instruction).

### Explicit Prohibitions
- AI/AI-assisted tools: permitted for general writing assistance without disclosure, EXCEPT where AI or AI-assisted tools are part of the research design or methods themselves — in that case, use must be described reproducibly in the Methods section, naming the model/tool, version, and manufacturer. This is a specific, explicit AI-use disclosure rule not present in FIELD_SKILL.
- Single-anonymized peer review (author identities known to reviewers, not vice versa) — a process detail, not a writing-style constraint, but worth noting for cover-letter/blinding purposes.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Follows FIELD_SKILL norm. Abstracts sampled use direct, active claims ("the authors introduce...", "results show...") consistent with field norms; no evidence of unusual hedging or informality.

### Statistical Reporting
Follows FIELD_SKILL norm at the abstract level — no visible deviation from quantitative-specificity norms.

### Citation Density
Follows FIELD_SKILL norm; no basis to detect a deviation from abstract-level sampling.

### Structural Deviations
PRACTICE/GUIDELINE — the five-way article-type system (research notes, software papers, data papers, review papers, alongside standard papers) is JOCM-specific and stated in guidelines. This is a genuine structural delta: contributions can legitimately take non-IMRaD forms (e.g., a software paper documenting a package, or a data paper documenting a dataset) that would not fit FIELD_SKILL's empirical/theory templates. When drafting for this journal, first confirm which of the five types the submission targets, since expected structure differs by type.

### Other Journal-Specific Patterns
ENFORCED — explicit, narrowly-scoped AI-disclosure requirement tied specifically to AI-as-methodology (not AI-as-writing-aid), which is stricter/more specific than general field practice and should be flagged to authors using LLM-based or ML-based choice models (a common topic in this journal's recent volumes, e.g., Ordinal-ResLogit, LLM-assisted choice modelling).

RELAXATION — as an ABS 1 journal, JOCM's scope is broader and less prescriptive on paper "importance"/contribution framing than ABS 4*/4 outlets; sampled abstracts read as more application-focused and less concerned with articulating a novel-to-the-discipline contribution narrative than the FIELD_SKILL introduction template implies. This is a relaxation of emphasis, not a new norm — introductions still likely follow the same rhetorical moves, just with lower bar for "importance."

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction rhetorical structure: FIELD DEFAULT
- Methods tense conventions: FIELD DEFAULT
- Results/interpretation integration: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Citation format (author-year): FIELD DEFAULT

---

## Common Pitfalls
- Submitting a software or dataset contribution shoehorned into a standard full-paper IMRaD structure rather than using JOCM's dedicated software-paper or data-paper category, which has different expectations.
- Omitting the required AI-methodology disclosure (model name, version, manufacturer) in the Methods section when a choice model itself uses AI/ML components — this is a specific, checkable guideline requirement, not a generic field norm.
- Exceeding the 250-word abstract cap or including citations in the abstract.

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
| https://www.sciencedirect.com/journal/journal-of-choice-modelling/publish/guide-for-authors | Guidelines | Search-engine-extracted snippet (direct fetch returned 403) |
| https://jocm.org.uk/guide.html and https://jocm.org.uk/ | Guidelines (article types, e.g. research notes/software/data/review papers) | Search-engine-extracted snippet (direct fetch returned HTTP 521, site unreachable) |
| Cazor et al., "A smooth bounded choice model," JCM 57 (2025) | Full-text PDF (structure unreadable from raw fetch; abstract used) | White Rose repository open-access PDF + WebSearch abstract |
| Tjiong et al., "Capturing zero-price effects in stated choice surveys," JCM 58 | Abstract | SSRN + ScienceDirect + White Rose snippets |
| McCarthy, Naqavi & Karlström, "Recursive logit models for dynamic versus sequential trip chaining," JCM 57 (2025) | Abstract | WebSearch/RePEc snippet |
| Büscher & Bauer, "Using Lagrange multiplier type tests...," JCM 57 (2025) | Title/listing only | RePEc/IDEAS listing |
| Xhakollari, Asioli & Nayga, "Mitigating hypothetical bias in choice experiments," JCM 56 (2025) | Title/listing only | RePEc/IDEAS listing |
| Kamal & Farooq, "Ordinal-ResLogit," JCM 50 (2024) | Abstract | WebSearch snippet, ScienceDirect/arXiv preprint corroboration |
| Gonzalez Sepulveda et al., "The impact of violations of expected utility theory on choices," JCM 53 (2024) | Title/listing only | RePEc/IDEAS listing |
| Armantalab, Ghosh & Hawkins, "Potential for electric vehicle adoption in Midwest US States," JCM 59 (2026) | Title/listing only | RePEc/IDEAS listing |
| Seong, Choi & Koo, "Semi-dynamics of electric vehicle adoption...," JCM 58 (2026); Al-Haideri, Ismail & Weiss, "Cyclists' crossing behaviour at roundabouts," JCM 59 (2026) | Title/listing only | RePEc/IDEAS listing |

**Access limitations:** ScienceDirect and jocm.org.uk both blocked or failed on direct fetch (403 and HTTP 521 respectively) in this environment; all guideline content was reconstructed from search-engine-extracted snippets of those pages, which is a lower-confidence source than direct page text. Full text of sampled articles was largely inaccessible (paywalled); analysis relies on titles, abstracts, and one open-access PDF (fetched but not machine-readable as text) from White Rose Research Online. No article was read in full; consequently the "no delta" findings for voice, statistics, and citation density rest on abstract-level evidence only and should be treated as provisional/low-confidence rather than confirmed.
