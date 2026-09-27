# LRC Lerntool — Distraktoren-Audit

**Datum:** 2026-09-26  
**Geprüft:** 286 Fragen  
**Problematische Distraktoren gefunden:** 50 von 858 (17,5 % der Fragen betroffen)

- **Schwerwiegend (high):** 47
- **Mittel (medium):** 3
- **Gering (low):** 0

---

## Zusammenfassung

Von 286 Fragen haben **50 Fragen (17,5 %)** mindestens einen thematisch unpassenden Distraktor.

### Hauptprobleme

1. **Frequenz/Kanal-Mismatch (24 Fragen)**  
   Frequenz-Fragen erhalten "Kanal X"-Distraktoren, Kanal-Fragen erhalten "X kHz"-Distraktoren.  
   
   **Beispiel:** "Auf welcher Grenzwellen-Frequenz erfolgt die DSC-Alarmierung?"  
   - Richtig: `2187,5 kHz`
   - Falsch: `Kanal 70 (DSC)`, `Kanal 13 (Brücke-Brücke)` ❌

2. **Ja/Nein-Inkonsistenz (23 Fragen)**  
   Ja/Nein-Fragen haben sachfremde Distraktoren statt konditionaler Ja/Nein-Varianten.
   
   **Beispiel:** "Darf die Frequenz 2187,5 kHz für Sprechfunkverkehr benutzt werden?"  
   - Richtig: `nein`
   - Falsch: `Kanal 16 (Notruf und Anruf)`, `2182 kHz`, `Kanal 70 (DSC)` ❌  
   - Besser wären: "Ja, im Notfall", "Nein, nur für DSC", "Ja, wenn autorisiert"

3. **Erfundene Begriffe (6 Fragen)**  
   - DSC-Expansionen die nicht existieren: "Safety Call", "Ship Communication", "Signal Control"
   - Seegebiets-Bezeichnungen: "Zone 1–4", "Gebiet I–IV", "SOLAS 1–4"

---

## Liste der betroffenen Fragen

### SCHWERWIEGEND (47 Fragen)

#### Frequenz/Kanal-Mismatch

**SB_104** · Auf welcher Frequenz im GW-Bereich wird außerhalb des GMDSS im Seefunk die Notmeldung ausgesendet?  
→ Distraktoren: `Kanal 70 (DSC)`, `Kanal 13 (Brücke-Brücke)`  
→ **Fix:** Andere GW-Frequenzen (2177 kHz, 2174,5 kHz, 518 kHz)

**SB_55** · Auf welcher Grenzwellen-Frequenz erfolgt die DSC-Alarmierung?  
→ Distraktoren: `Kanal 70 (DSC)`, `Kanal 13 (Brücke-Brücke)`  
→ **Fix:** 2182 kHz, 2177 kHz, 518 kHz

**SB_56** · Welche der genannten Frequenzen ist u.a. für die DSC-Alarmierung im Kurzwellenbereich zu benützen?  
→ Distraktoren: `Kanal 6 (Koordination)`, `Kanal 70 (DSC)`, `Kanal 13 (Brücke-Brücke)`  
→ **Fix:** 4207,5 kHz, 6312 kHz, 12577 kHz

**SB_57** · In welchem Frequenzbereich soll die DSC-Alarmierung Schiff–Land aus den Seegebieten A3 und A4 erfolgen?  
→ Distraktoren: `Kanal 70 (DSC)`, `Kanal 13 (Brücke-Brücke)`  
→ **Fix:** 4207,5 kHz, 6312 kHz, 12577 kHz

**SB_58** · In welchem Frequenzbereich soll die DSC-Alarmierung von Schiffen in der Nähe in den Seegebieten A3 und A4 erfolgen?  
→ Distraktoren: `Kanal 16 (Notruf und Anruf)`, `Kanal 6 (Koordination)`  
→ **Fix:** 4207,5 kHz (KW-Alternative), 156,525 MHz (andere UKW-Freq)

**SB_66** · Auf welcher Frequenz im GW-Bereich wird die Meldung, mit der im GMDSS der Notverkehr im Sprechfunk eingeleitet wird, ausgesendet?  
→ Distraktor: `Kanal 13 (Brücke-Brücke)`  
→ **Fix:** 2187,5 kHz, 2177 kHz, 518 kHz

**SB_67** · Auf welcher Frequenz wird der Notverkehr im Sprechfunk auf Grenzwelle im GMDSS abgewickelt?  
→ Distraktor: `Kanal 70 (DSC)`  
→ **Fix:** 2187,5 kHz, 2177 kHz, 3023 kHz

**SB_71** · Welche der angeführten GW-Frequenzen werden für Search and Rescue (SAR) „vor Ort" benutzt?  
→ Distraktor: `Kanal 13 (Brücke-Brücke)`  
→ **Fix:** 2187,5 kHz, 4125 kHz, 5680 kHz

**SB_78** · Auf welcher GW-Frequenz soll eine Seefunkstelle im Sprechfunk die Dringlichkeitsmeldung im GMDSS aussenden?  
→ Distraktoren: `Kanal 13 (Brücke-Brücke)`, `Kanal 6 (Koordination)`, `Kanal 70 (DSC)`  
→ **Fix:** 2187,5 kHz, 3023 kHz, 4125 kHz

**SB_82** · Auf welcher GW-Frequenz soll eine Seefunkstelle im Sprechfunk die Sicherheitsmeldung im GMDSS im Regelfall aussenden?  
→ Distraktoren: `Kanal 70 (DSC)`, `Kanal 6 (Koordination)`  
→ **Fix:** 2187,5 kHz, 518 kHz, 490 kHz

**SB_9** · Auf welcher Frequenz ist im GMDSS ein Grenzwellen-DSC-Wachempfänger empfangsbereit?  
→ Distraktoren: `Kanal 6 (Koordination)`, `Kanal 16 (Notruf und Anruf)`  
→ **Fix:** 2182 kHz, 2177 kHz, 518 kHz

**LRC_123** · Welcher Kanal im UKW-Seefunkbereich ist vorzugsweise für den Verkehr und koordinierte SAR-Einsätze vorgesehen?  
→ Distraktor: `156,8 MHz`  
→ **Fix:** Kanal 16, Kanal 13, Kanal 70

**LRC_88** · Auf welchem UKW-Kanal erfolgt die DSC-Alarmierung?  
→ Distraktor: `4125 kHz`  
→ **Fix:** Kanal 16, Kanal 13, Kanal 6

**SB_15** · Welcher UKW-Kanal sollte im GMDSS nach Möglichkeit für den Empfang von Meldungen betreffend die Sicherheit der Seeschifffahrt dauernd abgehört werden?  
→ Distraktor: `4125 kHz`  
→ **Fix:** Kanal 16, Kanal 6, Kanal 70

---

#### Ja/Nein-Inkonsistenz

**LRC_165** · Müssen Sie auch bei Versuchssendungen das Rufzeichen oder eine sonstige Kennung angeben?  
→ Richtig: `Ja`  
→ Distraktoren: `Nur wenn eine Küstenfunkstelle antwortet`, `Nur auf Grenz- und Kurzwelle`  
→ **Fix:** "Nein, bei Versuchssendungen nicht", "Ja, aber nur auf Kurzwelle", "Nein, nur im Notverkehr"

**LRC_108** · Darf die Frequenz 2187,5 kHz für Sprechfunkverkehr benutzt werden?  
→ Richtig: `nein`  
→ Distraktoren: `Kanal 16 (Notruf und Anruf)`, `2182 kHz`, `Kanal 70 (DSC)`  
→ **Fix:** "Ja, im Notfall", "Ja, für Sicherheitsmeldungen", "Nein, ausschließlich für DSC"

**LRC_111** · Wird im Seefunkdienst vor einem Anruf im Notverkehr das Notzeichen MAYDAY ausgesendet?  
→ Richtig: `ja`  
→ Distraktoren: `Durch den Kapitän`, `Nur im Notfall`, `Auf Kanal 16`  
→ **Fix:** "Nein, nur bei DSC-Alarmierung", "Ja, dreimal", "Nein, MAYDAY folgt nach dem Anruf"

**LRC_112** · Darf ein Schiff, das selbst nicht in Not ist, für ein anderes Schiff einen Notalarm aussenden?  
→ Richtig: `ja (Mayday Relay)`  
→ Distraktoren: `Im Seegebiet A1`, `Nach Bestätigung`, `Nur im Notfall`  
→ **Fix:** "Nein, nur die Küstenfunkstelle darf das", "Ja, aber nur nach Erlaubnis des RCC", "Nein, es sei denn das Schiff in Not kann nicht selbst senden"

**LRC_168** · Darf eine Seefunkstelle auch dann gerufen werden, wenn der Schiffsname nicht bekannt ist?  
→ Richtig: `ja`  
→ Distraktoren: `In allen Seegebieten`, `Auf Kanal 16`, `Nur im Notfall`  
→ **Fix:** "Nein, der Name muss bekannt sein", "Ja, mit der MMSI", "Nein, außer bei Notverkehr"

**LRC_48** · Ist das Funker-Zeugnis an Bord mitzuführen?  
→ Richtig: `ja`  
→ Distraktoren: `GOC (General Operator Certificate)`, `Allgemeines Betriebszeugnis`, `UKW-Sprechfunkzeugnis`  
→ **Fix:** "Nein, nur eine Kopie", "Ja, oder eine beglaubigte Ablichtung", "Nein, außer bei gewerblicher Fahrt"

**SB_105** · Darf im Seefunk außerhalb des GMDSS die Notmeldung nur auf 2182 kHz ausgesendet werden?  
→ Richtig: `nein, eine Funkstelle in Not darf die Notmeldung auf jeder verfügbaren Frequenz aussenden`  
→ Distraktoren: `Seegebiet A2`, `Seegebiet A3`, `Weltweit`  
→ **Fix:** "Ja, ausschließlich auf 2182 kHz", "Nein, auch auf 2187,5 kHz", "Ja, es sei denn keine Antwort erfolgt"

**SB_107** · Darf im Seefunk außerhalb des GMDSS die Notmeldung ausschließlich auf Kanal 16 ausgesendet werden?  
→ Richtig: `nein, eine Funkstelle in Not darf die Notmeldung auf jeder verfügbaren Frequenz aussenden`  
→ Distraktoren: `2182 kHz`, `Kanal 16 (Notruf und Anruf)`, `4125 kHz`  
→ **Fix:** "Ja, nur auf Kanal 16", "Nein, auch auf Kanal 70 per DSC", "Ja, außer im Seegebiet A4"

**SB_63** · Muss eine Seefunkstelle, die auf GW oder UKW einen DSC-Notalarm einer in ihrer Nähe befindlichen anderen Seefunkstelle empfangen hat, den Empfang über Sprechfunk bestätigen?  
→ Richtig: `ja`  
→ Distraktoren: `Gruppenruf`, `Über DSC auf Kanal 70`, `DSC-Anruf`  
→ **Fix:** "Nein, nur Küstenfunkstellen bestätigen", "Ja, wenn Hilfe geleistet werden kann", "Nein, es sei denn keine Küstenfunkstelle antwortet"

---

#### Erfundene DSC-Expansion

**LRC_13** · Was heißt DSC?  
→ Richtig: `Digital Selective Calling — Digitaler Selektivruf`  
→ Distraktoren: `Distress Safety Call — Not- und Sicherheitsruf`, `Direct Ship Communication — Direkte Schiffskommunikation`, `Digital Signal Control — Digitale Signalsteuerung`  
→ **Fix:** Echte Abkürzungen verwenden: "MMSI (Maritime Mobile Service Identity)", "NBDP (Narrow Band Direct Printing)", "GMDSS (Global Maritime Distress and Safety System)"

---

### MITTEL (3 Fragen)

**LRC_5** · Welchen geografischen Bereich etwa umfasst das Seegebiet A4?  
→ Distraktoren: `Die Gebiete zwischen 40°N und 40°S`, `Den gesamten Bereich außerhalb der UKW-Reichweite`  
→ **Fix:** "Die Gebiete außerhalb der Inmarsat-Satellitenabdeckung", "Seegebiete mit Kurzwellen-Reichweite, aber ohne Satellit", "Die Hochsee jenseits von 400 Seemeilen"

---

## Empfehlung

**Reparatur:** Die 50 betroffenen Fragen sollten korrigiert werden, bevor das Tool für echtes Lernen eingesetzt wird. Die Distraktoren sind derzeit zu leicht als falsch erkennbar (wegen Kategoriefehlern) oder verwirren durch erfundene Begriffe.

**Priorität:**
1. **Hoch:** Ja/Nein-Fragen (23) + Frequenz/Kanal-Mismatch (24) — diese verfälschen das Lernziel
2. **Mittel:** Erfundene Begriffe (3) — lehrt Falschwissen

**Vorgehen:**  
Peter entscheidet, ob manuelle Korrektur via Editor im Tool oder Batch-Ersetzung über JSON-Export/Import.

---

## Dateianhänge

- `lrc_distractor_audit.json` — maschinenlesbar, alle 50 Issues mit IDs
- `lrc_questions.json` — extrahiertes QUESTIONS-Array für Batch-Bearbeitung
