#!/usr/bin/env python3
"""Merge: v4 als Basis + alle batch_NN.json Korrekturen + neue Fragen -> v6.json
Konvertiert wrong von [{"t":..,"why":..}] in reine Stringliste (Tool-Format)."""
import json, sys
from pathlib import Path

WS = Path("/home/ubuntu/.openclaw/workspace")
V4 = WS / "lrc_questions_v4.json"
PROG = WS / "lrc/data/v6_progress"
OUT = WS / "lrc/data/lrc_questions_v6.json"
AUDIT = WS / "lrc/data/v6_audit.json"

v4 = json.loads(V4.read_text(encoding="utf-8"))
order = [q["id"] for q in v4]
by_id = {q["id"]: dict(q) for q in v4}

fixes, new_items, audit = {}, [], []
for bf in sorted(PROG.glob("batch_*.json")):
    for it in json.loads(bf.read_text(encoding="utf-8")):
        wrong = [w["t"] if isinstance(w, dict) else w for w in it["wrong"]]
        rec = {"id": it["id"], "q": it["q"], "correct": it["correct"], "wrong": wrong}
        audit.append({**it, "batch": bf.name})
        if it.get("action") == "new" or it["id"] not in by_id:
            new_items.append(rec)
        else:
            fixes[it["id"]] = rec

# Basis anwenden
for qid, rec in fixes.items():
    by_id[qid] = rec

final = [by_id[q] for q in order] + new_items

OUT.write_text(json.dumps(final, ensure_ascii=False, indent=1), encoding="utf-8")
AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=1), encoding="utf-8")

kept = sum(1 for a in audit if a.get("action") == "kept")
fixed = sum(1 for a in audit if a.get("action") == "fixed")
newc = sum(1 for a in audit if a.get("action") == "new")
print(f"v4 base       : {len(v4)}")
print(f"touched       : {len(audit)} (kept={kept} fixed={fixed} new={newc})")
print(f"final total   : {len(final)}")
print(f"unchanged     : {len(v4) - fixed - kept}")
