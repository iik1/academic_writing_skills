---
name: evolutionary-computation-writing-style
description: >
  Journal-specific writing conventions for Evolutionary Computation
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Evolutionary Computation",
  "submit to Evolutionary Computation", "match Evolutionary Computation style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Evolutionary Computation

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** MIT Press
- **Scope:** International forum for theoretical and practical work on computational systems inspired by nature, with particular emphasis on evolutionary models of computation (genetic algorithms, evolutionary strategies, evolutionary programming, genetic programming, classifier systems) and related paradigms (swarm intelligence, artificial immune systems).
- **Guidelines URL:** https://direct.mit.edu/evco/pages/submission-guidelines (accessed via search-engine cache/snippets; direct fetch returned HTTP 403)
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 0 full-text (all direct.mit.edu article pages returned HTTP 403); findings below rest on the publisher guidelines page and corroborating secondary sources (Wikipedia journal entry, journal call-for-papers page, search-engine-indexed abstract snippets for ~6 articles/titles). No full-text or complete-abstract spot-check was possible within the accessible source chain.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No single mandated section template beyond standard IMRaD-style organization implied by field norms. The journal explicitly organizes accepted content into three overlapping categories authors should position their paper within: **Applications**, **Experimental Results**, and **Theory**. Authors are expected to make clear which category (or combination) their contribution falls into, which is a journal-specific framing not present in FIELD_SKILL.

### Length
Papers should be **8,000–12,000 words**, with a hard maximum of **35 pages** in the journal's LaTeX style, including references. This is a specific numeric constraint FIELD_SKILL does not specify.

### Abstract
No structured/sectioned abstract format found; standard single-paragraph abstract. No explicit word limit found for the abstract itself (distinct from the body length limit).

### Citations
No journal-specific citation style deviation found beyond field norms.

### Headings
No journal-specific heading convention found beyond field norms.

### Tables and Figures
Authors may submit a **Supplementary Material file** (data, additional visualizations, etc.) made available online after acceptance, with **no size limit**. This is a distinctive journal-specific allowance not covered by FIELD_SKILL's appendix/online-supplement guidance.

### Explicit Prohibitions
**Strong, distinctive, and specific prohibition**: the journal explicitly and strongly discourages papers proposing a "novel" algorithm based on a metaphor to a natural system (particularly where the natural system exhibits no actual optimization property), and discourages hybrids of such metaphor-based algorithms. Any genuinely novel algorithm must be described **in purely computational terms**, without reference to the source metaphor's vocabulary (e.g., "elephants," "seals," "hunting"). This is a well-known, actively enforced editorial policy specific to this journal (and the broader "metaphor-based metaheuristics" backlash in the field) and has no counterpart in FIELD_SKILL.

Submissions must describe **mature, original work** not published or under review elsewhere — standard but worth stating as it is explicit in the guidelines.

Submission requires **LaTeX** preparation, submitted as PDF via Editorial Manager — a format mandate FIELD_SKILL does not specify.

---

## Observed Deltas from FIELD_SKILL
> Only dimensions where this journal deviates. Omit any with no delta.

### Voice and Register
Follows FIELD_SKILL norm. No evidence of deviation found in accessible sources.

### Statistical Reporting
Follows FIELD_SKILL norm. No evidence of deviation found.

### Citation Density
Follows FIELD_SKILL norm. No evidence of deviation found.

### Structural Deviations
The Applications / Experimental Results / Theory self-categorization (see Structure above) is the one journal-specific structural signal found; it is ENFORCED (stated in guidelines) but could not be confirmed against article text since full text was inaccessible.

### Other Journal-Specific Patterns
The anti-metaphor-algorithm prohibition (see Explicit Prohibitions) is the single most distinctive, well-documented journal-specific norm identified — ENFORCED, stated explicitly in guidelines and consistent with the journal's public editorial stance and the field's broader "metaphor-based metaheuristics" critique literature. Authors drafting for this journal should avoid naming or framing new methods around a biological/natural analogy and should instead present mechanisms in abstract algorithmic/mathematical terms.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Argumentation (CARS model, Introduction structure): FIELD DEFAULT
- Methods conventions (tense, procedural detail): FIELD DEFAULT
- Results and reporting norms: FIELD DEFAULT
- Discussion/Conclusion norms: FIELD DEFAULT
- Citation and literature engagement: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT

---

## Common Pitfalls
- Naming a new method after a natural/biological metaphor (e.g., an animal-behavior-inspired algorithm name) without purely computational justification — explicitly discouraged and a known desk-reject trigger at this journal.
- Exceeding the 35-page / 8,000–12,000 word envelope without checking against the journal's LaTeX style file.
- Failing to signal which of the three content categories (Applications, Experimental Results, Theory) the paper belongs to.

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
| https://direct.mit.edu/evco/pages/submission-guidelines | Guidelines | Search-engine-indexed snippet/summary (direct fetch returned HTTP 403) |
| https://en.wikipedia.org/wiki/Evolutionary_Computation_(journal) | Background/scope | Full fetch successful |
| https://direct.mit.edu/evco/pages/evolutionary_computation_call_for_papers | Guidelines (call for papers) | Search-engine-indexed snippet only |
| https://direct.mit.edu/evco/article/31/2/81/115462 ("Evolutionary Algorithms for Parameter Optimization—Thirty Years Later", 2023) | Abstract/title | Title/citation only via search snippet; full fetch returned HTTP 403 |
| PPSN 2024 Extended Versions special issue (multiple 2024/2025 titles, e.g. "Adaptive Sampled Walk...", "Adapting MOEA/D to CMA-ES...", "Runtime Analysis of Evolutionary Diversity Optimization...") | Titles only | Search-engine snippet, no abstracts accessible |
| Vol. 34 Issue 1 (Spring 2026) contributor names (Kneissl, Sudholt, Rook, Benjamins, Bossek, Trautmann) | Metadata only | Search-engine snippet |

**Access limitation note:** All `direct.mit.edu/evco/article/...` pages returned HTTP 403 Forbidden on direct fetch, blocking full-text and complete-abstract spot-checking. Findings in this skill rely on the publicly cached/indexed guidelines text and journal metadata rather than direct article reading. This is a materially thinner evidence base than the assignment's target of ~15 articles; treat the "Structural Deviations" and any unlisted dimensions as provisional pending future access.
