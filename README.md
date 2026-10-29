# academic_writing_skills

**200+ writing skills for Claude Code: 10 field baselines + 190+ journal-specific skills**

A library of Claude Code skills for writing academic journal articles. Each skill encodes the writing conventions, structural expectations, citation norms, and rhetorical style of a specific outlet. The library covers 197 journals across 15 fields from the ABS 2024 Academic Journal Guide, plus NHH's bonus list.

---

## How It Works: Two-Layer Design

Every journal skill builds on a **field baseline**. There are two layers:

1. **Field skill** (one per discipline): sets the default voice, argument structure, quantitative norms, and citation style for the field. Apply this when you want field-appropriate writing without targeting a specific outlet.
2. **Journal skill** (one per outlet): inherits the field baseline and adds outlet-specific conventions: typical article length, section structure, preferred empirical approaches, editorial emphases, tone calibration, and so on.

You can use either layer alone. For the best result when targeting a submission, use the journal skill (it already incorporates the field conventions).

---

## Field Baselines

10 field baselines in `skills/fields/`:

| Skill file | Field |
|---|---|
| `econ-field-writing-style` | Economics |
| `finance-field-writing-style` | Finance |
| `account-field-writing-style` | Accounting |
| `strat-field-writing-style` | Strategy |
| `mgmt-field-writing-style` | Management |
| `mkt-field-writing-style` | Marketing |
| `opsandtech-field-writing-style` | Operations and Technology Management |
| `orandmansci-field-writing-style` | Operational Research and Management Science |
| `sector-field-writing-style` | Sector journals (tourism, transport, hospitality, energy) |
| `soc-sci-field-writing-style` | Social Sciences |

---

## Journal Coverage by Field

### Economics (`skills/economics/`) -- 41 journals

AEJ: Applied Economics, AEJ: Economic Policy, AEJ: Macroeconomics, AEJ: Microeconomics, American Economic Review, Cambridge Journal of Economics, Ecological Economics, Econometrica, Economic Journal, Economic Theory, European Economic Review, Experimental Economics, Games and Economic Behavior, Health Economics, JEBO, JEEM, Journal of Development Economics, Journal of Econometrics, Journal of Economic Literature, Journal of Economic Perspectives, Journal of Economic Theory, Journal of European Economic Association, Journal of Health Economics, Journal of Human Resources, Journal of International Economics, Journal of Labor Economics, Journal of Law and Economics, Journal of Monetary Economics, Journal of Political Economy, Journal of Public Economics, Journal of Urban Economics, Oxford Bulletin of Economics and Statistics, Quarterly Journal of Economics, RAND Journal of Economics, Review of Economic Dynamics, Review of Economic Studies, Review of Economics and Statistics, Scandinavian Journal of Economics, Energy Economics, Journal of Environmental Management, Journal of Productivity Analysis

### Finance (`skills/finance/`) -- 26 journals

Annual Review of Financial Economics, Corporate Governance: An International Review, European Financial Management, European Journal of Finance, Finance and Stochastics, Financial Management, IJFE, Insurance: Mathematics and Economics, JFQA, Journal of Banking and Finance, Journal of Corporate Finance, Journal of Empirical Finance, Journal of Financial Econometrics, Journal of Financial Economics, Journal of Financial Intermediation, Journal of Financial Markets, Journal of Financial Services Research, Journal of Financial Stability, Journal of Futures Markets, Journal of International Money and Finance, Journal of Money Credit and Banking, Journal of Finance, Mathematical Finance, Quantitative Finance, Review of Financial Studies, Review of Finance

### Accounting (`skills/accounting/`) -- 23 journals

AAAJ, Abacus, Accounting and Business Research, Accounting Forum, Accounting Horizons, Accounting Organizations and Society, Accounting Review, Auditing: A Journal of Practice and Theory, Behavioral Research in Accounting, British Accounting Review, Contemporary Accounting Research, Critical Perspectives on Accounting, European Accounting Review, Financial Accountability and Management, International Journal of Accounting, Journal of Accounting and Economics, Journal of Accounting and Public Policy, Journal of Accounting Research, Journal of American Taxation Association, Journal of Business Finance and Accounting, Journal of Financial Reporting, Management Accounting Research, Review of Accounting Studies

### Strategy (`skills/strategy/`) -- 5 journals

Global Strategy Journal, Long Range Planning, Strategic Management Journal, Strategic Organization, Strategy Science

### Management (`skills/mgmt/`) -- 8 journals

Academy of Management Annals, Academy of Management Journal, Academy of Management Learning and Education, Academy of Management Review, Administrative Science Quarterly, Journal of Management, Organization Science, Research Policy

### Marketing (`skills/marketing/`) -- 6 journals

Journal of the Academy of Marketing Science, Journal of Consumer Psychology, Journal of Consumer Research, Journal of Marketing, Journal of Marketing Research, Marketing Science

### Operations and Technology Management (`skills/ops-tech/`) -- 13 journals

Computers in Industry, IEEE Transactions on Engineering Management, IJOPM, IJPE, IJPR, Journal of Business Logistics, Journal of Operations Management, Journal of Purchasing and Supply Management, Journal of Supply Chain Management, MSOM, Production and Operations Management, Production Planning and Control, Supply Chain Management: An International Journal

### Operational Research and Management Science (`skills/or-mansci/`) -- 16 journals

Annals of Operations Research, Computers and Operations Research, Decision Sciences, EJOR, INFORMS Journal on Computing, International Journal of Forecasting, Journal of the Operational Research Society, Management Science, Mathematical Programming, Mathematics of Operations Research, Naval Research Logistics, Omega, Operations Research, Reliability Engineering and System Safety, SIAM Journal on Optimization, Transportation Science

### Social Sciences (`skills/soc-sci/`) -- 36 journals

American Journal of Political Science, American Journal of Sociology, American Political Science Review, American Sociological Review, Annals of Statistics, Annual Review of Sociology, Antipode, British Journal of Sociology, Business Strategy and the Environment, Development and Change, Economy and Society, Environment and Planning D, Environmental Science and Technology, European Sociological Review, Industrial and Corporate Change, International Organization, International Studies Quarterly, Journal of Development Studies, Journal of European Social Policy, Journal of Politics, Journal of Social Policy, New Political Economy, Politics and Society, Progress in Human Geography, Psychological Science, Public Administration Review, Review of International Political Economy, Risk Analysis, Social Forces, Social Science and Medicine, Social Science Research, Socio-Economic Review, Sociological Review, Sociology, Sociology of Health and Illness, World Development

### Sector Journals (`skills/sector/`) -- 13 journals

Annals of Tourism Research, Energy Journal, Food Policy, International Journal of Contemporary Hospitality Management, International Journal of Hospitality Management, Journal of Service Research, Journal of Sustainable Tourism, Journal of Travel Research, Tourism Management, Transportation Research Part A, Transportation Research Part B, Transportation Research Part D, Transportation Research Part E

### Information Systems (`skills/information-systems/`) -- 3 journals

Information Systems Research, Journal of the Association for Information Systems, MIS Quarterly

### Entrepreneurship (`skills/entrepreneurship/`) -- 2 journals

Entrepreneurship Theory and Practice, Journal of Business Venturing

### Human Resource Management (`skills/hrm/`) -- 3 journals

Human Resource Management Journal, Journal of Applied Psychology, Personnel Psychology

### International Business (`skills/international-business/`) -- 1 journal

Journal of International Business Studies

### Non-ABS / Bonus List (`skills/non-abs/`) -- 4 journals

Applied Linguistics, Modern Language Journal, Nature, Science

---

---

## Repository Structure

```
academic_writing_skills/
├── README.md
├── LICENSE
├── skills/
│   ├── fields/                 10 field baselines
│   ├── economics/              41 journals
│   ├── finance/                26 journals
│   ├── accounting/             23 journals
│   ├── strategy/               5 journals
│   ├── mgmt/                   8 journals
│   ├── marketing/              6 journals
│   ├── ops-tech/               13 journals
│   ├── or-mansci/              16 journals
│   ├── soc-sci/                36 journals
│   ├── sector/                 13 journals
│   ├── information-systems/    3 journals
│   ├── entrepreneurship/       2 journals
│   ├── hrm/                    3 journals
│   ├── international-business/ 1 journal
│   └── non-abs/                4 journals
├── reports/                    QA reports, one per journal skill
└── tools/
    ├── dispatch_journal_agents.py
    ├── journal_agent_prompt.txt
    └── field_skill_generator_prompt.txt
```

---

## Installation

### Option A: Global (available in all projects)

```bash
git clone https://github.com/iik1/academic_writing_skills.git
cd academic_writing_skills

# Copy all standard journal skills
for f in skills/**/*_SKILL.md; do
  cp "$f" ~/.claude/skills/"$(basename "$f" _SKILL.md).md"
done

# All skills are now in field subdirectories -- no separate step needed
```

### Option B: Project-level (available in one project only)

```bash
mkdir -p .claude/skills
for f in skills/**/*_SKILL.md; do
  cp "$f" .claude/skills/"$(basename "$f" _SKILL.md).md"
done
```

### Selective installation

```bash
# Field baseline only
cp skills/fields/econ-field-writing-style ~/.claude/skills/econ-field-writing-style.md

# One journal
cp skills/economics/american-economic-review_SKILL.md ~/.claude/skills/american-economic-review.md
```

---

## Usage

Once installed, reference the skill by name in conversation with Claude Code:

```
Draft the introduction for this paper targeting the Journal of Finance.
```

```
Apply EJOR writing conventions to clean up this methods section.
```

```
Review this abstract against Management Science style.
```

For journal submissions, use the journal skill. It already encodes the field baseline, so you do not need to invoke both separately.

### Typical workflow

1. **Draft** using the field skill to get field-appropriate structure and voice.
2. **Revise** using the journal skill to apply journal-specific constraints (length limits, citation format, section norms).
3. **Check** by asking Claude to flag deviations from the journal's hard constraints before submission.

---

## Skill Quality

Each skill was developed by analyzing published articles and author guidelines. The skills encode voice and register, structural norms, quantitative reporting conventions, citation style, typical length, and editorial emphases.

Most journals are paywalled; the analysis for those skills relies on extended previews (abstracts plus whatever additional text was freely accessible) rather than full text. The author guidelines sections are reliable. The observed-pattern sections are reasonable but should be verified against full-text articles where possible.

Skills marked with `Articles spot-checked: 0` in their corresponding `reports/` file are based on author guidelines only.

---

## Adding a New Journal

1. Identify the field and locate the matching field baseline in `skills/fields/`.
2. Create a new file in the appropriate subdirectory: `skills/<field>/<journal-slug>_SKILL.md`.
3. Cover: voice and register, structure, quantitative norms, citation format, length norms, and distinctive editorial expectations.
4. Cross-reference the field baseline explicitly.
5. Add a corresponding QA report to `reports/`.
6. Update the journal list in this README.

---

## License

MIT. See `LICENSE`.
