#!/usr/bin/env python3
"""Normalisierte Fenstersuche in audit_src/. Findet zu einer Frage die Fundstelle
samt Kontext (belegte richtige Antwort steht darunter).

Usage:
  find_src.py --id LRC_64            # Frage aus v4 holen und suchen
  find_src.py --q "Freitext..."
  find_src.py --ids LRC_1,LRC_2,...  # Batch
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path

SRC_DIR = Path("/home/ubuntu/.openclaw/workspace/audit_src")
V4 = Path("/home/ubuntu/.openclaw/workspace/lrc_questions_v4.json")
FILES = ["LRC_fragen.txt", "SRC_SB.txt", "SRC_TK.txt", "LRC_GOC.txt"]


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ")
    # Anfuehrungszeichen / Bindestriche vereinheitlichen
    for a, b in [("\u201e", '"'), ("\u201c", '"'), ("\u201d", '"'), ("\u201a", "'"),
                 ("\u2018", "'"), ("\u2019", "'"), ("\u2013", "-"), ("\u2014", "-"),
                 ("\u2212", "-"), ("\u00ad", "")]:
        s = s.replace(a, b)
    s = s.lower()
    # Umlaute
    for a, b in [("\u00e4", "ae"), ("\u00f6", "oe"), ("\u00fc", "ue"), ("\u00df", "ss")]:
        s = s.replace(a, b)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    # Satzzeichen weg
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


class Hay:
    """Normalisierter Haystack mit Rueckabbildung auf Originalzeilen."""

    def __init__(self, path: Path):
        self.path = path
        self.lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        parts, self.map = [], []  # map: (charpos_start, line_idx)
        pos = 0
        for i, ln in enumerate(self.lines):
            n = norm(ln)
            if not n:
                continue
            self.map.append((pos, i))
            parts.append(n)
            pos += len(n) + 1
        self.text = " ".join(parts)

    def line_of(self, charpos: int) -> int:
        lo, hi, best = 0, len(self.map) - 1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.map[mid][0] <= charpos:
                best = self.map[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return best


HAYS = None


def hays():
    global HAYS
    if HAYS is None:
        HAYS = [Hay(SRC_DIR / f) for f in FILES if (SRC_DIR / f).exists()]
    return HAYS


def search(q: str, before=1, after=14, max_hits=2):
    """Absteigend lange Wortfenster 12 -> 4 suchen."""
    words = norm(q).split()
    results = []
    for size in range(min(12, len(words)), 3, -1):
        for start in range(0, len(words) - size + 1):
            needle = " ".join(words[start:start + size])
            for h in hays():
                idx, found_here = 0, 0
                while True:
                    p = h.text.find(needle, idx)
                    if p < 0:
                        break
                    ln = h.line_of(p)
                    results.append({
                        "file": h.path.name, "line": ln + 1, "win": size,
                        "ctx": "\n".join(h.lines[max(0, ln - before): ln + after]),
                    })
                    idx = p + 1
                    found_here += 1
                    if found_here >= max_hits:
                        break
            if results:
                return results[:max_hits]
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id")
    ap.add_argument("--ids")
    ap.add_argument("--q")
    ap.add_argument("--after", type=int, default=14)
    a = ap.parse_args()

    if a.q:
        for r in search(a.q, after=a.after):
            print(f"=== {r['file']}:{r['line']} (win={r['win']})\n{r['ctx']}\n")
        return

    v4 = {x["id"]: x for x in json.loads(V4.read_text(encoding="utf-8"))}
    ids = [a.id] if a.id else a.ids.split(",")
    for qid in ids:
        qid = qid.strip()
        item = v4.get(qid)
        if not item:
            print(f"##### {qid}: NICHT IN V4\n")
            continue
        print(f"##### {qid} | Q: {item['q']}")
        print(f"##### v4-correct: {item['correct']}")
        print(f"##### v4-wrong: {json.dumps(item['wrong'], ensure_ascii=False)}")
        hits = search(item["q"], after=a.after)
        if not hits:
            print("##### KEINE FUNDSTELLE\n")
            continue
        for r in hits[:1]:
            print(f"--- {r['file']}:{r['line']} (win={r['win']})\n{r['ctx']}")
        print()


if __name__ == "__main__":
    main()
