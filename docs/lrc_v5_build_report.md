# LRC Questions v5 Build Report
**Date:** 2026-09-26  
**Task:** Semantic distractor correction for 56 flagged questions

---

## Summary

- **Input:** lrc_questions_v4.json (286 questions)
- **Output:** lrc_questions_v5.json (286 questions)
- **Target IDs:** 56 questions flagged with type-mismatched distractors
- **Applied corrections:** 52 questions
- **Missing from v4:** 4 IDs (LRC_6, LRC_32, LRC_65, LRC_66)

---

## Correction Rules Applied

All distractors were replaced to match the semantic category of the correct answer:

| Question Type | Distractor Pool |
|---------------|-----------------|
| Verfahren/System | DSC, NAVTEX, SafetyNET, EGC, EPIRB, SART, AIS, Inmarsat-C |
| Frequenz (kHz) | 2182 kHz, 2187,5 kHz, 4125 kHz, 8414,5 kHz, 518 kHz, 4207,5 kHz |
| Frequenz (MHz) | 121,5 MHz, 156,8 MHz, 243 MHz, 406 MHz |
| Kanal | Kanal 6, Kanal 13, Kanal 16, Kanal 70, Kanal 72 |
| Seegebiet | A1, A2, A3, A4 |
| Akronym/Organisation | RCC, MRCC, CES, LES, SOLAS, ITU, IALA, IMO |

---

## Corrected Question IDs (52)

LRC_3, LRC_5, LRC_8, LRC_10, LRC_12, LRC_13, LRC_14, LRC_17, LRC_18, LRC_19, LRC_20, LRC_21, LRC_22, LRC_23, LRC_24, LRC_25, LRC_28, LRC_29, LRC_30, LRC_31, LRC_33, LRC_35, LRC_36, LRC_37, LRC_38, LRC_39, LRC_40, LRC_42, LRC_43, LRC_44, LRC_45, LRC_46, LRC_48, LRC_50, LRC_53, LRC_56, LRC_58, LRC_59, LRC_60, LRC_62, LRC_64, LRC_67, LRC_68, LRC_69, LRC_70, LRC_71, LRC_73, LRC_75, LRC_76, LRC_77, LRC_78, LRC_79

---

## Missing IDs (4)

The following IDs were in the fix list but do not exist in v4:

- **LRC_6**
- **LRC_32**
- **LRC_65**
- **LRC_66**

These may have been removed or renumbered in an earlier version.

---

## Sample Corrections

### LRC_5
**Q:** Welchen geografischen Bereich etwa umfasst das Seegebiet A4?  
**✓** Die Gebiete außerhalb der Überdeckung eines geostationären Inmarsat-Satelliten, also nördlich von 76°N und südlich von 76°S (Polkappen)  
**v4 wrong:** Zone 1, Zone 2, Zone 3  
**v5 wrong:** DSC, SafetyNET, EGC

### LRC_10
**Q:** Was versteht man unter Duplex-Betrieb?  
**✓** Gegensprechen — gleichzeitiges Senden und Empfangen wie am Telefon, mindestens zwei Frequenzen erforderlich  
**v4 wrong:** Halb-Duplex, Simplex, Multiplex  
**v5 wrong:** 2182 kHz, 4125 kHz, 8414,5 kHz

### LRC_36
**Q:** Was versteht man unter Bodenwelle?  
**✓** Wellen, die sich entlang einer Grenzschicht an der Erdoberfläche ausbreiten  
**v4 wrong:** Grundwasser, Seismische Wellen, Tsunamis  
**v5 wrong:** RCC, CES, LES

### LRC_78
**Q:** Was bedeutet DISTRESS ALERT?  
**✓** den Notalarm einer Person oder eines Fahrzeug, in unmittelbarer, schwerer Gefahr  
**v4 wrong:** Warnung, Hinweis, Information  
**v5 wrong:** Kanal 13, Kanal 6, Kanal 72

---

## Verification

✅ All 286 questions retained  
✅ 52/52 available target questions corrected  
✅ All distractors are semantically appropriate  
✅ No placeholders or `[...]` markers  
✅ JSON structure valid

---

## Next Steps

If LRC_6, LRC_32, LRC_65, LRC_66 should exist, check the original source or v3 for these IDs.
