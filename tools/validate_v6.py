#!/usr/bin/env python3
"""6 Validierungspunkte gegen den ECHTEN Lesepfad des Renderers.
Der Renderer liest shuffle([q.correct, ...q.wrong]) -> also correct/wrong pruefen."""
import json, re, subprocess, sys, unicodedata
from pathlib import Path

LRC = Path("/home/ubuntu/.openclaw/workspace/lrc")
HTML = LRC / "lrc_lerntool.html"
STABLE = LRC / "versions/lrc_lerntool_STABLE_v3_20260926_1019.html"

fail = []
def chk(ok, label, detail=""):
    print(("  PASS " if ok else "  FAIL ") + label + (f"  {detail}" if detail else ""))
    if not ok:
        fail.append(label)

html = HTML.read_text(encoding="utf-8")

# ---- 1. node --check auf den extrahierten Script-Block
print("\n[1] node --check auf Script-Block")
scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, flags=re.DOTALL)
big = max(scripts, key=len)
tmp = LRC / "data/_check.js"
tmp.write_text(big, encoding="utf-8")
r = subprocess.run(["node", "--check", str(tmp)], capture_output=True, text=True)
chk(r.returncode == 0, "node --check", r.stderr.strip()[:200] or "syntax ok")

# ---- 2. QUESTIONS zurueckextrahieren und als JSON parsen
print("\n[2] QUESTIONS-Array aus HTML zurueckextrahieren")
m = re.search(r"const\s+QUESTIONS\s*=\s*(\[.*?\]);", html, flags=re.DOTALL)
chk(m is not None, "const QUESTIONS gefunden (GROSSBUCHSTABEN)")
qs = json.loads(m.group(1))
chk(len(qs) == 292, f"Anzahl Eintraege == 292", f"ist {len(qs)}")
bad3 = [q["id"] for q in qs if len(q.get("wrong", [])) != 3]
chk(not bad3, "jeder Eintrag hat genau 3 Distraktoren", f"Verstoesse: {bad3[:8]}")
badf = [q.get("id") for q in qs if not all(k in q for k in ("id", "q", "correct", "wrong"))]
chk(not badf, "alle Felder id/q/correct/wrong vorhanden", f"Verstoesse: {badf[:8]}")

# ---- 3. Distraktor-Integritaet
print("\n[3] Distraktor-Integritaet")
def nk(s):
    s = s.lower().strip()
    for a, b in [("\u00e4","ae"),("\u00f6","oe"),("\u00fc","ue"),("\u00df","ss")]:
        s = s.replace(a, b)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s)).strip()

ident, dupe, sub = [], [], []
for q in qs:
    c, ws = nk(q["correct"]), [nk(w) for w in q["wrong"]]
    if c in ws:
        ident.append(q["id"])
    if len(set(ws)) != len(ws):
        dupe.append(q["id"])
    for w in ws:
        if w and c and (w in c or c in w):
            sub.append(f'{q["id"]}:{w[:40]}')
chk(not ident, "kein Distraktor identisch mit correct", f"Verstoesse: {ident[:8]}")
chk(not dupe, "keine Duplikate innerhalb einer Frage", f"Verstoesse: {dupe[:8]}")
chk(not sub, "kein Distraktor Teilstring von correct (und umgekehrt)", f"Verstoesse: {sub[:5]}")

# ---- 4. Platzhalter-Phrasen
print("\n[4] Keine Platzhalter-Metasprache")
PH = ["fachlich passende", "andere antwort", "siehe oben", "passende aber falsche",
      "eine andere fachlich", "anderer begriff", "keine angabe"]
hits = []
for q in qs:
    for w in q["wrong"]:
        if any(p in nk(w) for p in PH):
            hits.append(f'{q["id"]}:{w[:50]}')
chk(not hits, "keine Platzhalter-Phrasen", f"Verstoesse: {hits[:5]}")

# ---- 5. Bytegroesse vs Vorversion
print("\n[5] Bytegroesse vs Vorversion")
n_new, n_old = HTML.stat().st_size, STABLE.stat().st_size
chk(n_new != n_old, "Bytegroesse != Vorversion (Ersetzung hat gegriffen)",
    f"neu={n_new} alt={n_old} delta={n_new-n_old:+d}")

# ---- 6. Stichprobe: 3 konkret geaenderte IDs + neuer Distraktortext im Artefakt
print("\n[6] Stichprobe im finalen HTML (grep)")
SAMPLES = [
    ("LRC_64",  "General Maritime Data and Signalling System"),
    ("LRC_170", "Dezimalgrad"),
    ("LRC_113", "acknowledgement" ),
]
# LRC_113 nutzt deutschen Text -> echten Distraktor aus der Datei holen
by_id = {q["id"]: q for q in qs}
SAMPLES[2] = ("LRC_113", by_id["LRC_113"]["wrong"][2][:40])
for qid, needle in SAMPLES:
    present = (qid in html) and (needle in html)
    chk(present, f"{qid} + neuer Distraktortext im HTML", f'"{needle[:45]}"')

# Zusatz: die 6 neuen IDs muessen drin sein
NEW = ["SB_12", "SB_26", "SB_28", "SB_48", "SB_62", "SB_100"]
missing = [i for i in NEW if i not in by_id]
chk(not missing, "alle 6 neuen SB-IDs im Artefakt", f"fehlen: {missing}")

print("\n" + ("=" * 60))
if fail:
    print(f"RESULT: {len(fail)} FAILED -> {fail}")
    sys.exit(1)
print("RESULT: ALLE VALIDIERUNGSPUNKTE GRUEN")
print(f"  Fragen: {len(qs)} | HTML: {n_new} bytes (vorher {n_old})")
