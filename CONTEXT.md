# LRC Lerntool — Project Context

## Project Overview

**Purpose:** Self-contained HTML learning tool for LRC/SRC maritime radio certification (German language)  
**User:** Peter (self-study) + gift to instructor (older gentleman, non-technical)  
**Quality Bar:** Expert must be able to review without finding errors

## Current State

**Production Version:** `lrc_lerntool.html` (v4, 98 KB, 286 questions)  
**Status:** Production-ready, sent to Peter 2026-09-26  
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

### v4 Placeholder Block
Questions `LRC_108` onwards in some builds contain category placeholders instead of content-specific distractors:
- Generic phrases: "Im Seegebiet A1", "Über DSC", "Durch den Kapitän"
- These pass regex validation but fail expert review

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

### v4 (2026-09-26) — PRODUCTION
- 286 questions
- All distractors validated semantically
- Sent to Peter, approved for instructor gift
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
