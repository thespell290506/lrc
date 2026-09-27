# LRC/SRC Lerntool

Maritime radio certification learning tool for LRC (Long Range Certificate) and SRC (Short Range Certificate) German-language examinations.

## Overview

Self-contained single HTML file with embedded 286 multiple-choice questions covering:
- **LRC:** 188 questions
- **SB (Seebetriebsfunk):** 98 questions

Built for gift to instructor — quality standard: expert-level review without finding errors.

## Usage

Open `lrc_lerntool.html` in any modern web browser. No server, no dependencies, no internet connection required.

**Features:**
- Randomized answer order per question
- Wrong answer tracking
- Review mode for missed questions
- Progress tracking
- Clean, accessible interface

## Files

- **`lrc_lerntool.html`** — Production version (v4, 98 KB, 286 questions)
- **`data/questions.json`** — Latest question data (v5, 92 KB)
- **`data/cards_all.json`** — Source flashcards (295 cards from PDF extraction)
- **`docs/`** — Build reports, completion notes, audit findings
- **`versions/`** — Stable backups

## Data Format

Questions embedded in HTML as:
```javascript
const QUESTIONS = [
  {
    id: "LRC_1",
    q: "Question text",
    correct: "Correct answer",
    wrong: ["Distractor 1", "Distractor 2", "Distractor 3"]
  },
  // ...
]
```

**HARD RULE:** Variable name must be `QUESTIONS` (uppercase). Render code shuffles `[q.correct, ...q.wrong]`.

## Quality Standards

1. Correct answer must be documented in official learning materials
2. Distractors should be plausible invented terms (not random nonsense)
3. No duplicate distractors within a question
4. No distractor equals or contains the correct answer
5. Yes/No questions need Yes/No distractors with wrong reasoning
6. No placeholder phrases

## Validation

Before any build:
```bash
# Syntax check
node --check lrc_lerntool.html

# Data validation
python3 scripts/validate.py

# Verify specific corrected IDs present in output
grep -n "LRC_5" lrc_lerntool.html
```

## Known Issues

- **9 missing questions:** SB_12, SB_26, SB_28, SB_48, SB_62, SB_72, SB_74, SB_76, SB_100 (not in source PDF)
- **v5 data has wrong distractor assignments** — use v4 HTML as source of truth

## Development Notes

See `docs/` for:
- Build process documentation
- Distractor audit findings
- Lessons learned from failed builds

## License

Educational use. Questions derived from official LRC/SRC examination materials.

---

**Status:** Production-ready v4 (2026-09-26)  
**Questions:** 286 / 295 from source  
**Quality:** Expert-reviewed
