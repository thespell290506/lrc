#!/usr/bin/env python3
"""Baut lrc_lerntool.html aus STABLE_v3 + lrc_questions_v6.json.
Ersetzt NUR das QUESTIONS-Array, berührt nichts sonst."""
import json, re
from pathlib import Path

STABLE = Path("/home/ubuntu/.openclaw/workspace/lrc/versions/lrc_lerntool_STABLE_v3_20260926_1019.html")
V6 = Path("/home/ubuntu/.openclaw/workspace/lrc/data/lrc_questions_v6.json")
OUT = Path("/home/ubuntu/.openclaw/workspace/lrc/lrc_lerntool.html")

html = STABLE.read_text(encoding="utf-8")
v6 = json.loads(V6.read_text(encoding="utf-8"))

# JS-Literal bauen: json.dumps ueber die GANZE Struktur
js_array = json.dumps(v6, ensure_ascii=False, indent=1)

# Regex: sucht 'const QUESTIONS = [' bis zum matchenden ']' (kann mehrzeilig sein)
pattern = r'(const\s+QUESTIONS\s*=\s*)\[.*?\];'
replacement = r'\g<1>' + js_array + ';'

html_new = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)

if html_new == html:
    print("ERROR: Replacement did not match (QUESTIONS array not found or wrong case)")
    exit(1)

OUT.write_text(html_new, encoding="utf-8")
print(f"Built {OUT}")
print(f"  {len(v6)} questions")
print(f"  {len(html_new)} bytes (was {len(html)} bytes)")
