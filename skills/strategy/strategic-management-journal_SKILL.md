---
name: strategic-management-journal-writing-style
description: >
  Journal-specific writing conventions for Strategic Management Journal
  (ABS 4*, STRAT). Use alongside strat-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Strategic Management Journal",
  "submit to Strategic Management Journal", "match Strategic Management Journal style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Strategic Management Journal

## Journal Profile
- **ABS 2024 Rating:** 4*
- **Field:** STRAT
- **Publisher:** Wiley, in partnership with the Strategic Management Society
- **Scope:** Publishes high-quality research on questions relevant to strategic management, accepting diverse topics, framings, and methods including statistical inference, qualitative data, verbal theory, computational models, and mathematical models. Explicitly welcomes replications, non-results, and dataset articles.
- **Guidelines URL:** https://sms.onlinelibrary.wiley.com/hub/journal/10970266/homepage/forauthors.html (most recent: May 2025)
- **Field baseline:** strat-field-writing-style
- **Articles spot-checked:** 1 (Doshi, Bell, Mirzayev & Vanneste, 2025, DOI: 10.1002/smj.3677)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Required main document layout (in order): Abstract, body text, references, appendices, tables and figures. Tables and figures must NOT be embedded in the text — they are placed at the END of the manuscript, after references, with "INSERT TABLE X HERE" placement instructions in the body. Appendices follow references and precede tables and figures. If a single appendix, it is labeled "Appendix" without a number. Online-only appendices are labeled "online appendix" throughout and submitted as a separate file.

Title page must be a **separate file** from the main document. It contains: title, full author names/titles/email addresses/affiliations (with complete addresses), a running head (≤60 characters), and acknowledgements. Acknowledgements appear **only on the title page** at submission; upon acceptance they move to the main paper at the end of the text, immediately before the references.

### Length
- Research Article: strongly suggested limit of **40 pages**, including figures and tables. [ENFORCED by convention; stated as a strong suggestion]
- Short research articles (Commentary): no more than **20 pages** including title page, abstract, text, figures, tables, and references.
- Prospective, Special Issue Article, Editorial: 40 pages.

### Abstract
**Dual abstract required — this is a hard departure from FIELD_SKILL.** [ENFORCED]

Two separate one-paragraph abstracts, each of up to **125 words**:
1. **Research Summary** — precise summary of the entire paper (not just conclusions); must stand alone; no citations.
2. **Managerial Summary** — same scope requirements as the research summary, but written in **plain, non-academic language** aimed at business practitioners; no citations.

Additionally, **5 keywords** are required for indexing purposes. [ENFORCED]

The two abstracts appear under labeled bold headers ("Research Summary:" and "Managerial Summary:") within a single abstract block in the typeset version.

### Citations
APA style. Author-date in-text citations. Multiple citations in parentheses ordered alphabetically, separated by semicolons. Six or more authors: (first author et al., year) from first citation. Five or fewer: all names at first citation, et al. thereafter. Ampersands used in citations only within parentheses and in the reference list (not in running text). Unpublished/personal work may be cited in text but must not appear in the reference list. All references must correspond to in-text citations and vice versa.

Reference list in alphabetical order, single-spaced, at end of main document.

### Headings
Three levels. **Headings are not numbered** per the main document section, but the General APA guidelines table states "Please number sections" — published articles consistently use numbered sections with a vertical bar separator (e.g., "1 | INTRODUCTION", "2.1 | Strategic decisions", "2.3.1 | Large language models"). Follow the published practice of numbered headings. [PRACTICE ONLY for numbering convention; ENFORCED for formatting levels]

- **Level 1:** ALL CAPS, bold, center-aligned (e.g., INTRODUCTION, DISCUSSION)
- **Level 2:** Title case (main words capitalized), bold, left-aligned
- **Level 3:** Lowercase, italicized (e.g., *Independent variable*)

The General APA table lists up to 5 heading levels, all bold, with Level 5 running on with text after a full stop. In practice, a fourth level (italic, not numbered, flush left) is used for subsection labels within methods sections.

### Tables and Figures
Tables and figures placed at the END of the manuscript, after references. Body text contains only placement instructions: "INSERT TABLE 1 HERE". [ENFORCED]

Table label placed **above** the table in the format: TABLE 1  Name of table (bold number, space, name). Figure label placed **below** the figure in the format: FIGURE 1  Name of figure. [ENFORCED — specific format]

Tables must be in editable format (not images). Figures: high resolution (≥300 dpi), preferred formats .tiff and .png. Color appears online; black and white in print. All tables and figures must be numbered and include legends.

### Explicit Prohibitions
- **No p-value asterisks or significance cutoff levels** — SMJ explicitly bans papers that "report or refer to cutoff levels of statistical significance (p-values)." [ENFORCED — hard ban, see Statistical Reporting below]
- No citations in either abstract.
- No author names, affiliations, or acknowledgements in the main document (blind review).
- No Track Changes or comment bubbles in submission.
- Tables must not be submitted as images.
- Figures and tables must not be embedded in the body text.
- Personal websites and most departmental websites do not qualify as open data repositories.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where SMJ deviates from the field baseline.

### Statistical Reporting
**This is the most consequential delta from FIELD_SKILL.**

FIELD_SKILL states "practice varies across journals: some require exact p-values or confidence intervals without asterisks; others permit conventional significance markers." SMJ goes further: it **explicitly bans** all reporting that refers to cutoff levels of statistical significance (p-values with asterisks or stars). [ENFORCED]

What SMJ requires instead:
- Report **standard errors** and/or **exact p-values** (without asterisks), not significance markers.
- Preferred framing: confidence intervals, standard errors, probability of observing the result in the sample — assessed in relation to the research question, not against a cutoff.
- For accepted papers: **effect sizes must be explicitly discussed and interpreted** for all relevant estimated coefficients. This is a requirement at the acceptance stage, not just a preference.
- Authors must also address **material significance (magnitude)**, not only statistical significance.

SMJ also has an explicit editorial policy against **data snooping and p-hacking**: authors must not search for significant coefficients and then formulate hypotheses to match them.

This policy is confirmed in the spot-checked article: results are reported as correlation coefficients, proportions, and confidence intervals (jackknife 95% CIs) with no asterisks, no significance stars, and no reference to p < .05 thresholds.

### Abstract Format
FIELD_SKILL notes that a separate managerial summary is required "in many outlets" and is listed as a non-baseline element. At SMJ it is **mandatory and enforced**: both a Research Summary and a Managerial Summary are required, each ≤125 words, each standing alone, neither containing citations. The managerial summary must be in plain non-academic language. Confirmed in the spot-checked article, where both appear under labeled bold headers within the abstract block.

### Open Data and Transparency Requirements
Not covered in FIELD_SKILL. SMJ runs an explicit Open Data badge program in partnership with the Center for Open Science. Authors are asked at submission and acceptance whether they will share data in a qualifying public repository (OSF, Dataverse, FIVES, re3data-listed repositories). Participation is voluntary but strongly encouraged; data availability statements appear in published articles. The spot-checked article includes a "DATA AVAILABILITY STATEMENT" section immediately before the reference list. [PRACTICE ONLY for placement; GUIDELINE ONLY for the badge program itself]

### Endnotes vs. Footnotes
FIELD_SKILL does not specify. SMJ explicitly requires **footnotes** (shown at the bottom of the page), not endnotes. Confirmed in the spot-checked article, which uses numbered footnotes. [ENFORCED]

### Language Variety
FIELD_SKILL does not specify. SMJ requires **American English** throughout, including in tables and figures. [ENFORCED]

### Number and Punctuation Style
FIELD_SKILL does not specify. SMJ follows APA number and punctuation conventions with American formatting:
- Numbers 1–9 spelled out; 10 and above as numerals (with standard exceptions for measurement units, ratings, scales).
- No leading zero before a decimal fraction when the statistic cannot exceed 1 (e.g., p = .028, r = .45); leading zero required when it can exceed 1 (e.g., 0.23 cm).
- American decimal points (not commas); commas in numbers ≥1,000.
- En dashes for ranges (1996–2000); em dashes for parenthetical phrases.
- Serial comma required.
- Ampersands (&) restricted to parenthetical citations and reference list; not used in running text except in established proper names (R&D, Standard & Poor's).
- "Percent" spelled out in running text; % symbol in parenthetical text and figures.
[ENFORCED]

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT (first-person plural throughout)
- Active vs. passive voice: FIELD DEFAULT
- Register and formality: FIELD DEFAULT
- Introduction structure (CARS logic, gap-contribution framing): FIELD DEFAULT
- Contribution positioning: FIELD DEFAULT
- Literature engagement and paraphrase dominance: FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Hedging norms: FIELD DEFAULT
- Discussion and Conclusions structure (merged section): FIELD DEFAULT
- Managerial implications subsection: FIELD DEFAULT
- Limitations and future research subsection: FIELD DEFAULT
- Robustness checks: FIELD DEFAULT
- Qualitative/mixed methods transparency: FIELD DEFAULT

---

## Common Pitfalls

1. **Submitting with p-value asterisks or significance cutoff language** (e.g., "p < .05", "†p < .10"). SMJ will desk-reject or require major revision. Rephrase all significance statements as exact values with confidence intervals and effect size discussion.

2. **Omitting the Managerial Summary or conflating it with the Research Summary.** The two abstracts serve different audiences and must be written separately. The managerial summary must avoid academic jargon entirely and stay within 125 words.

3. **Embedding tables and figures in the body text.** At submission, all tables and figures must be at the end of the document, with placeholder text ("INSERT TABLE 1 HERE") in the body. Submitting them embedded is a formatting violation that can delay processing.

4. **Placing acknowledgements in the main document.** At submission, acknowledgements belong on the title page only. Including them in the body text compromises blind review.

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| https://www.strategicmanagement.net/wp-content/uploads/2023/07/SMJ-Author-Instructions-06-08-23-FINAL.pdf | Author Guidelines (June 2023) | Direct PDF fetch |
| https://sms.onlinelibrary.wiley.com/pb-assets/hub-assets/sms/AG/SMJ-Author-Instructions-May-2025-1748220403090.pdf | Author Guidelines (May 2025) | Web search confirmed; content consistent with 2023 version on all key constraints |
| Doshi, Bell, Mirzayev & Vanneste (2025). Generative artificial intelligence and evaluating strategic decisions. *Strategic Management Journal*, 46(3), 583–610. DOI: 10.1002/smj.3677 | Full-text article | UCL open-access PDF via discovery.ucl.ac.uk |