#!/usr/bin/env python3
"""Triage: findet die Fragen in v4, die einen der 4 definierten Defekte haben.
Defekte: unsolvable (Distraktor==correct / Teilstring), placeholder-Metasprache,
kategorie-stub (Blacklist), typ-mismatch (Frequenz/Kanal/JaNein).
Rein regelbasiert -> sagt mir, WO ich fachlich hinschauen muss."""
import json, re, sys
from pathlib import Path

V4 = Path("/home/ubuntu/.openclaw/workspace/lrc_questions_v4.json")


def nk(s):
    s = s.lower().strip()
    s = s.replace("\u00e4", "ae").replace("\u00f6", "oe").replace("\u00fc", "ue").replace("\u00df", "ss")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


STUBS = [
    r"^im seegebiet a\d$", r"^in allen seegebieten$", r"^ueber dsc$", r"^auf kanal 16$",
    r"^durch den kapitaen$", r"^durch die kuestenfunkstelle$", r"^gemaess solas$",
    r"^dsc controller$", r"^gruppenruf$", r"^selektivruf$", r"^dsc anruf$",
    r"^nach bestaetigung$", r"^weltweit$", r"^automatische alarmierung$",
    r"^nur im notfall$", r"^inmarsat abdeckung$", r"^seegebiet a\d$",
    r"^jederzeit$", r"^nein$|^ja$",
]
PLACEHOLDER = [
    "fachlich passende", "andere antwort", "siehe oben", "passende aber falsche",
    "anderer begriff", "sonstiges", "keine angabe",
]
FREQ = re.compile(r"^\d+([,.]\d+)?\s*(khz|mhz|ghz|hz)$")
CHAN = re.compile(r"^kanal\s*\d+$|^ch\s*\d+$")
YESNO = re.compile(r"^(ja|nein)\b")


def main():
    qs = json.loads(V4.read_text(encoding="utf-8"))
    report = []
    for it in qs:
        c, ws = it["correct"], it["wrong"]
        nc, nq = nk(c), nk(it["q"])
        flags = []
        if len(ws) != 3:
            flags.append(f"count={len(ws)}")
        if len(set(nk(w) for w in ws)) != len(ws):
            flags.append("dupe")
        for w in ws:
            nw = nk(w)
            if nw == nc:
                flags.append(f"identical:{w!r}")
            elif nw and (nw in nc or nc in nw):
                flags.append(f"substring:{w!r}")
            if any(p in nw for p in PLACEHOLDER):
                flags.append(f"placeholder:{w!r}")
            if any(re.match(p, nw) for p in STUBS):
                flags.append(f"stub:{w!r}")
        # Typ-Mismatch
        q_asks_freq = any(t in nq for t in ["frequenz", "khz", "mhz"])
        if FREQ.match(nc) or CHAN.match(nc):
            bad = [w for w in ws if not (FREQ.match(nk(w)) or CHAN.match(nk(w)))]
            if bad:
                flags.append(f"type-mismatch-num:{len(bad)}")
        if YESNO.match(nc):
            if not any(YESNO.match(nk(w)) for w in ws):
                flags.append("yesno-no-yesno-distractor")
        if not q_asks_freq:
            nf = [w for w in ws if FREQ.match(nk(w))]
            if nf and not (FREQ.match(nc)):
                flags.append(f"freq-stub:{len(nf)}")
        if flags:
            report.append({"id": it["id"], "flags": sorted(set(flags))})

    print(f"TOTAL {len(qs)} | FLAGGED {len(report)} | CLEAN {len(qs)-len(report)}")
    Path("/home/ubuntu/.openclaw/workspace/lrc/data/triage.json").parent.mkdir(parents=True, exist_ok=True)
    Path("/home/ubuntu/.openclaw/workspace/lrc/data/triage.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in report:
        print(r["id"], "|", "; ".join(r["flags"])[:150])


if __name__ == "__main__":
    main()
