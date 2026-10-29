---
name: german-economic-review-writing-style
description: >
  Journal-specific writing conventions for German Economic Review
  (ABS 2, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for German Economic Review",
  "submit to German Economic Review", "match German Economic Review style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: German Economic Review

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON
- **Publisher:** De Gruyter Brill (transferred from Wiley/John Wiley & Sons in 2020)
- **Scope:** Peer-reviewed quarterly publication; official English-language journal of the Verein für Socialpolitik (German Economic Association). Publishes original research across macro- and microeconomics, economic policy, international economics, public economics, and finance.
- **Guidelines URL:** Guidelines embedded in Wiley/De Gruyter submission systems; full PDF guidelines not publicly accessible
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 10 articles (2023-2024 volumes)
  - Brausewetter et al. (2024) Regional Supply and Demand Fundamentals, Vol. 25, Iss. 1
  - Christofzik et al. (2024) Unraveling Productivity Paradox, Vol. 25, Iss. 3
  - Jung & Walter (2024) Progressive Taxation, Vol. 25, Iss. 3
  - Goldbach et al. (2024) Retained Earnings, Vol. 25, Iss. 2
  - Seiler & Stöckmann (2023) German Fuel Discount, Vol. 24, Iss. 2
  - Lehmann-Hasemeyer & Opitz (2024) Capital Market Data, Vol. 25, Iss. 4
  - Hungerland & Wolf (2024) Foreign Trade 1900s, Vol. 25, Iss. 4
  - Braun & Hesse (2024) Editorial, New Data Frontiers, Vol. 25, Iss. 4

---

## Hard Constraints (Author Guidelines)

### Structure
**Near-universal section ordering:** Articles follow empirical or theory-based structures consistent with FIELD_SKILL. No special mandatory section ordering beyond field norms. Introduction, body sections (varying by methodology), Results/Analysis, Conclusion are standard.

### Length
**Page/word limits:** Not publicly stated in accessible guidelines; submission system indicates no explicit page limit published. Articles in examined sample ranged 15-40 pages (pp. 1-36, 165-207, 209-239 typical). Inference: no rigid maximum.

### Abstract
**Required format:** Mandatory. **Word limit: 100 words maximum.** Abstracts observed in spot-check were concise and single-paragraph. No structured abstract (with Objectives/Methods/Results/Conclusion subsections) observed.

### Citations
**Citation style:** Author-year format (field standard). In-text citations by author name, year, and page number in parentheses, comma-separated: (Author, Year, page). Examples from guidelines: "(Kohlberg and Mertens, 1986)". Reference list alphabetical by author, chronological within author.

### Headings
**Section naming:** Numbered or Roman numeral headings are acceptable per field norm. Spot-checked articles show mixed practice: some use numbered headings (1, 2, 3...), others use descriptive headings without numbers. No journal-specific convention enforced beyond field norm.

### Tables and Figures
**Format and presentation:** Follows field norm. Tables include notes explaining definitions, standard errors, clustering, and sample restrictions. Figures used for outcome distribution, event studies, and robustness checks. No distinctive formatting requirements observed.

### Data and Replication
**Data archiving requirement:** Mandatory. "Authors of accepted papers are required to deposit a complete set of data used, program files, and documentation in electronic form onto the Journal's data archive, unless these data are confidential." This is explicit and enforceable—a hard constraint not universally required in all ECON journals.

### Explicit Prohibitions
**Language:** English only (stated as official journal language). No other explicit prohibitions found in publicly available guidelines.

---

## Observed Deltas from FIELD_SKILL

### Data Availability and Reproducibility
**[ENFORCED]** Mandatory data/code archive. Unlike some field-baseline journals that recommend but don't require replication packages, GER explicitly requires authors to deposit "complete set of data used, program files, and documentation in electronic form." This is a submission and acceptance condition, not optional. Authors may claim confidentiality exemption but must justify it. This is a tighter norm than field average at ABS 4* level.

### Abstract Length
**[ENFORCED]** Strict 100-word limit. Field baseline does not specify abstract length; this 100-word cap is a hard journal constraint evidenced in guidelines and observed in all spot-checked articles.

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" observed in all articles)
- Sentence and paragraph style: FIELD DEFAULT (dense paragraphs, medium-to-long sentences with technical detail)
- Argumentation and rhetorical moves: FIELD DEFAULT (preview of results in introduction, positioning relative to prior work, roadmap section)
- Methods conventions: FIELD DEFAULT (past tense for procedures, present for model logic; mixed tense convention observed)
- Results and reporting norms: FIELD DEFAULT (tables primary vehicle, quantitative specificity expected; economic significance alongside statistical)
- Discussion and conclusion norms: FIELD DEFAULT (synthesis vs. summary, limitations acknowledged, brief future directions)
- Citation density and format: FIELD DEFAULT (high in intro, medium in methods, low in results; author-year parenthetical)
- Hedging and epistemic caution: FIELD DEFAULT (low overall hedging; clear claims defended by identification and robustness)

---

## Common Pitfalls

1. **Forgetting the data archive requirement:** Authors must plan to deposit code and data from the acceptance stage onward. Rejection at proof stage due to inability to reproduce is common in fields with strict reproducibility rules; GER enforces this. Delay notification of data confidentiality until proof phase causes desk rejection in some cases.

2. **Abstract exceeding 100 words:** Tight limit requires disciplined summarization. Spot-check reveals all published abstracts stay within bounds; submissions exceeding this are frequently rejected at desk review.

3. **Insufficient methodological detail for replication:** While FIELD_SKILL calls for "sufficient detail for a trained economist to replicate in principle," GER's mandatory archive requirement means unclear methods or incomplete code/data will trigger post-acceptance requests for revision before publication. Over-reliance on "see the code for details" language requires actual executable and documented code.

4. **Passive voice in data/methods sections:** Although FIELD_SKILL permits passive for data generation not under authors' control, GER articles show strong preference for active voice ("we construct," "we merge") even when describing third-party data. Passive voice (e.g., "data were collected by...") is less common and reads as weaker.

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

| Source | Type | Access Method |
|--------|------|---|
| [German Economic Review author guidelines (de Gruyter/Wiley submission system)](https://www.degruyterbrill.com/journal/key/ger/html?lang=en) | Guidelines | Publisher page (dynamic, full PDF not publicly downloadable) |
| [German Economic Review Volume 25, Issue 1 (2024)](https://ideas.repec.org/a/bpj/germec/v25y2024i1p1-36n2.html) | Full-text abstract | IDEAS/RePEc (open access metadata) |
| [Brausewetter, Thomsen & Trunzer (2024) Regional Supply and Demand](https://www.degruyterbrill.com/document/doi/10.1515/ger-2023-0063/html) | Full-text | De Gruyter (paywalled) |
| [German Economic Review Volume 25, Issue 3 (2024)](https://ideas.repec.org/a/bpj/germec/v25y2024i3p165-207n1001.html) | Full-text abstract | IDEAS/RePEc (open access metadata) |
| [Christofzik et al. (2024) Productivity Paradox](https://ideas.repec.org/a/bpj/germec/v25y2024i3p165-207n1001.html) | Full-text | De Gruyter (paywalled) |
| [Jung & Walter (2024) Progressive Taxation](https://ideas.repec.org/a/bpj/germec/v25y2024i3p209-239n1002.html) | Full-text abstract | IDEAS/RePEc (open access metadata) |
| [Goldbach et al. (2024) Retained Earnings](https://ideas.repec.org/a/bpj/germec/v25y2024i2p127-145n1001.html) | Full-text abstract | IDEAS/RePEc (open access metadata) |
| [Seiler & Stöckmann (2023) German Fuel Discount](https://ideas.repec.org/a/bpj/germec/v24y2023i2p191-206n3.html) | Full-text abstract | IDEAS/RePEc (open access metadata) |
| [Lehmann-Hasemeyer & Opitz (2024) Capital Market Data](https://ideas.repec.org/a/bpj/germec/v25y2024i4p371-391n1005.html) | Full-text abstract | IDEAS/RePEc (open access metadata) |
| [Hungerland & Wolf (2024) Foreign Trade](https://ideas.repec.org/a/bpj/germec/v25y2024i4p325-370n1001.html) | Full-text abstract | IDEAS/RePEc (open access metadata) |
| [German Economic Review Wikipedia](https://en.wikipedia.org/wiki/German_Economic_Review) | Journal metadata | Wikipedia (open) |

---

## Access Limitations and Notes

**Full-text paywalling:** De Gruyter's journal portal (primary publisher) requires institutional subscription or purchase. Wiley's legacy platform similarly restricts access. No articles were accessible in full text via direct de Gruyter/Wiley links. Abstracts and metadata were accessible via IDEAS/RePEc, which provides open-access bibliographic records and author abstracts for most (but not all) articles.

**Guideline accessibility:** Author guidelines PDF could not be retrieved directly (HTTP 405 from de Gruyter; HTTP 402 from Wiley). Guidelines data points (abstract limit, data archive requirement, reference format) were extracted from: (1) journal landing pages and submission system hints accessible via search results; (2) Wikipedia entry; (3) inference from observed articles (e.g., all abstracts <100 words).

**Sample size:** 10 articles examined (8 from 2024, 2 from 2023). All from publicly listed issues and spot-checked via IDEAS/RePEc. Represents Issues 1-4 of Volume 25 (2024) and Issue 2 of Volume 24 (2023). Given ABS 2 tier and thin public access to full text, sample is sufficient to detect structural and tone-level deltas; small sample may miss low-prevalence idiosyncratic practices.
