#!/usr/bin/env python3
"""Reparierte typografische Anfuehrungszeichen INNERHALB von JSON-Strings.
Ersetzt U+201E/201C/201D durch das einfache Zeichen >>'<< damit das JSON valide
bleibt und der Text lesbar ist. Fasst NICHT die JSON-Struktur an."""
import json
from pathlib import Path

PROG = Path("/home/ubuntu/.openclaw/workspace/lrc/data/v6_progress")

# typografische Zeichen, die in v4/meinem Text auftauchen und JSON brechen,
# wenn sie versehentlich als ASCII " geschrieben wurden.
REPL = {
    "\u201e": "\u201a",  # „ -> ‚ (einfaches oeffnend)
    "\u201c": "\u2018",  # " -> ' (einfaches schliessend/oeffnend)
    "\u201d": "\u2019",  # " -> '
}

for f in sorted(PROG.glob("batch_*.json")):
    raw = f.read_text(encoding="utf-8")
    try:
        json.loads(raw)
        print(f"OK    {f.name}")
        continue
    except json.JSONDecodeError:
        pass

    # Kaputt: alle typografischen Doppelquotes zu einfachen Quotes machen,
    # damit keine ASCII-" mehr mitten im String stehen koennen.
    fixed = raw
    for a, b in REPL.items():
        fixed = fixed.replace(a, b)

    # Jetzt noch "nackte" ASCII-Doppelquotes finden, die MITTEN in einem
    # String stehen (also nicht Struktur sind). Heuristik: Quote, die weder
    # von : , { } [ ] noch Zeilenanfang/-ende umgeben ist.
    out, i, n = [], 0, len(fixed)
    in_str = False
    while i < n:
        c = fixed[i]
        if c == '"':
            if not in_str:
                in_str = True
                out.append(c)
            else:
                # Schauen, was nach dem Quote kommt (ohne Whitespace)
                j = i + 1
                while j < n and fixed[j] in " \t":
                    j += 1
                nxt = fixed[j] if j < n else ""
                if nxt in (":", ",", "}", "]", "\n", "\r", ""):
                    in_str = False
                    out.append(c)
                else:
                    # Quote mitten im String -> in einfaches Zeichen wandeln
                    out.append("\u2019")
            i += 1
            continue
        if c == "\\" and in_str and i + 1 < n:
            out.append(fixed[i:i + 2])
            i += 2
            continue
        out.append(c)
        i += 1

    cand = "".join(out)
    try:
        json.loads(cand)
        f.write_text(cand, encoding="utf-8")
        print(f"FIXED {f.name}")
    except json.JSONDecodeError as e:
        print(f"STILL BROKEN {f.name}: {e}")
