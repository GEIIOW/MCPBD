#!/usr/bin/env python3
"""Checks the Portuguese translations against the English database.

Run from the repository root:   python3 tools/pt_missing.py
 - lists the English paragraphs that have no translation yet  -> pt/_missing.json
 - lists translations whose English text no longer exists     -> pt/_orphans.json
Send pt/_missing.json to Claude (or translate it by hand), then add the pairs to the matching pt/*.json file.
"""
import json, os, sys

FILES = ["characters", "teamcards", "crisis", "gems"]
TEXT_KEYS = {"special_rules", "rules", "description", "setup_text", "scoring_text"}
SPLIT = {"description", "special_rules"}          # these fields may hold several paragraphs separated by blank lines

def paragraphs(obj, key=None, out=None):
    out = out if out is not None else []
    if isinstance(obj, dict):
        for k, v in obj.items(): paragraphs(v, k, out)
    elif isinstance(obj, list):
        for v in obj: paragraphs(v, key, out)
    elif isinstance(obj, str) and key in TEXT_KEYS and obj.strip():
        for p in (obj.split("\n\n") if key in SPLIT else [obj]):
            p = p.strip()
            if p and p not in out: out.append(p)
    return out

missing, orphans, total, done = {}, {}, 0, 0
for f in FILES:
    en = paragraphs(json.load(open(f + ".json", encoding="utf-8")))
    path = os.path.join("pt", f + ".json")
    pt = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    miss = [p for p in en if p not in pt]
    orph = [k for k in pt if k not in en]
    total += len(en); done += len(en) - len(miss)
    if miss: missing[f] = miss
    if orph: orphans[f] = orph
    print(f"{f:11} {len(en) - len(miss):4}/{len(en):<4} translated   {len(miss):3} missing   {len(orph):3} orphan")

json.dump(missing, open("pt/_missing.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(orphans, open("pt/_orphans.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"\nTotal: {done}/{total} paragraphs translated. Missing -> pt/_missing.json · orphans -> pt/_orphans.json")
sys.exit(1 if missing else 0)
