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
