# LRC Lerntool — Project Context

## Project Overview

**Purpose:** Self-contained HTML learning tool for LRC/SRC maritime radio certification (German language)  
**User:** Peter (self-study) + gift to instructor (older gentleman, non-technical)  
**Quality Bar:** Expert must be able to review without finding errors

## Current State

**Production Version:** `lrc_lerntool_v7_20261001_1927.html` (v7, 100 KB, 286 questions)  
**Status:** Sent to Peter 2026-10-01, 10-question spot-check passed, awaiting full test  
**Repository:** https://github.com/thespell290506/lrc  

### Question Coverage
- **LRC:** 188 questions
- **SB (Seebetriebsfunk):** 98 questions
- **Missing:** 9 questions (no source data in PDF extraction)

## Technical Architecture

**Format:** Single self-contained HTML file  
**Data Structure:**
```javascript
const QUESTIONS = [  // MUST be uppercase
  {
    id: "LRC_1",
    q: "Question text",
    correct: "Correct answer",
    wrong: ["Distractor 1", "Distractor 2", "Distractor 3"]
  }
]
```

**Critical Rules:**
1. Variable name: `QUESTIONS` (uppercase) — renderer expects this exact name
2. Exactly 3 distractors per question
3. Never invent new format keys (`opts`, `ckey`) — breaks rendering

## Quality Standards (Peter's Requirements)

1. **Correct answer must be documented** in official learning materials
2. **Invented terms are acceptable** distractors if plausible ("Distress Safety Call" for DSC is good)
3. **Correct answer must not be too easy** to guess
4. **Yes/No questions need Yes/No distractors** with wrong reasoning (not "Channel 16" vs "yes")
5. **No placeholder phrases** in final output
6. **No distractor contains correct answer** as substring

## Known Issues & Traps

### v5 Data Corruption
`lrc_questions_v5.json` has wrong distractor assignments — corrections were applied by ID number instead of question type. **Do not use as source.**

### v3/v4 Pool-Phrase Contamination (Fixed in v7)
Versions v3 and v4 contained 262 generic distractor slots across 16 pool phrases:
- "Auf Kanal 16" ×31, "Über DSC" ×25, "Nach Bestätigung" ×24, "Nur im Notfall" ×22, "Durch den Kapitän" ×20, "Im Seegebiet A1" ×18, "4125 kHz" ×18, "Gemäß SOLAS" ×17, and 8 others
- These passed structural validation but failed expert scrutiny in actual use
- Status claims "all distractors validated" in commit `e4ed48d` and earlier CONTEXT.md were aspirational, not verified
- **Lesson (AGENTS.md §8.1):** Status lines written at session-end without consumer-level verification are unreliable

### Validation Traps (2026-09-26 Lessons)
1. **Self-checks must verify what consumers read**
   - Build script searched for lowercase `const questions =` 
   - HTML has uppercase `const QUESTIONS =`
   - Zero replacements, byte-identical output, reported as success
2. **Never send untested**
   - Minimum: `node --check` + JSON parse + grep for 2-3 corrected IDs
3. **No loops on known answers**
   - Check recent history before asking for recipient/subject

## Build Process

### Pre-send Checklist
```bash
# 1. Syntax validation
node --check lrc_lerntool.html

# 2. Verify QUESTIONS array parses
grep -A 5 "const QUESTIONS" lrc_lerntool.html | head -10

# 3. Spot-check corrected questions present
grep -c "LRC_5.*76°N" lrc_lerntool.html  # Should be 1

# 4. No placeholders leaked
grep -c "eine andere fachlich passende" lrc_lerntool.html  # Should be 0

# 5. Byte size changed from previous version
ls -l lrc_lerntool.html versions/lrc_lerntool_STABLE_*.html
```

## Distractor Strategies

### By Question Type
- **Frequency/channel:** Other maritime channels (2182, 2187.5, 518 kHz; channels 6, 13, 16, 70)
- **Sea areas:** A1/A2/A3/A4 alternatives
- **Certificates:** SRC/LRC/GOC/ROC variants
- **DSC procedures:** Other DSC call types
- **Modulation:** A3E/F3E/J3E/G1B
- **Yes/No:** Yes/No with wrong reasoning

### Good Distractor Examples
- "Distress Safety Call" (plausible invention, DSC context)
- "Nördlich 76°N und südlich 76°S" (wrong but specific, not vague)

### Bad Distractor Examples
- "Channel 16" as distractor for yes/no question (type mismatch)
- "Eine andere fachlich passende Antwort" (placeholder phrase)
- Any substring of correct answer

## Source Data

**Origin:** `flashcards/cards_all.json` (295 cards, PDF extraction)  
**Extraction Issues:**
- 4 questions had split text (LRC_7, LRC_8, SB_5, SB_6)
- Question text truncated, remainder in answer field
- Fixed by rejoining and using proper area codes

**Missing IDs:** SB_12, SB_26, SB_28, SB_48, SB_62, SB_72, SB_74, SB_76, SB_100

## Deployment

**Method:** Email via SMTP  
**Server:** host218.checkdomain.de:465 SSL  
**From:** ai@cp-i.at  
**To:** p.eisenkolb@i-invest.at  
**Credentials:** `.secrets/email.json` (field name: `pass`, not `password`)

**Why email:** Telegram rejects local HTML attachments by policy

## Version History

### v7 (2026-10-01) — PRODUCTION CANDIDATE
- 286 questions, all rebuilt from scratch
- Zero generic pool-phrase distractors (verified: "Auf Kanal 16", "Über DSC", etc. appear only as correct answers or in question text, never as distractors)
- Every distractor semantically plausible but factually wrong, domain-specific per question type
- Source: `data/rebuild_progress.json`
- Peter spot-check: 10 questions tested, "perfect"
- Full test pending 2026-10-02
- 100 KB

### v4 (2026-09-26) — SUPERSEDED
- 286 questions
- **Pool-phrase contamination discovered:** 262 generic distractor slots across 16 banned phrases
- Sent to Peter, initially approved — quality issues found in production use
- 98 KB

### v3 (2026-09-26)
- 146 questions
- Stable, backed up as baseline
- 92,229 bytes

### v5 (ABANDONED)
- Data corruption: wrong distractor assignments
- Do not use as source

### v6 (INCOMPLETE)
- Batched approach hit API credit limit
- 6 parallel Opus sub-agents spawned
- Zero usable output, full cost
- Peter feedback: "Du übertreibst es mit der token usage"

## Next Steps (if resuming development)

### High Priority
- Fix placeholder block (LRC_108+) if present in any builds
- Validate with rule-based script, not sub-agent fan-out

### Low Priority
- Extract 9 missing SB questions from PDF manually
- Build v6 deterministically (no LLM calls for distractor generation)

## Lessons Learned

1. **Status integrity:** Write completion immediately, not at session end
2. **Token efficiency:** Rule-based scripts over sub-agent parallelism for deterministic tasks
3. **Validation rigor:** Check actual consumer code paths, not assumed ones
4. **No untested sends:** Syntax + data + spot-checks mandatory
5. **Expert review required:** Automated validation catches format, not domain errors

---

**Last Updated:** 2026-09-27  
**Status:** Production-ready, repo established  
**Owner:** Peter Eisenkolb / The Spell
