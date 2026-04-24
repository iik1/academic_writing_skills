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