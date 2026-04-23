#!/usr/bin/env python3
"""
Lint script for knowledge base system.
Performs 9 checks and writes report to wiki/outputs/lint-YYYY-MM-DD.md
"""

import os
import sys
import yaml
import hashlib
import datetime
import re
from pathlib import Path
from typing import List, Dict, Tuple, Set
import itertools

# Configuration
WIKI_DIR = Path(__file__).parent.parent / "wiki"
RAW_DIR = Path(__file__).parent.parent / "raw"
OUTPUTS_DIR = WIKI_DIR / "outputs"
TODAY = datetime.date.today().isoformat()

def load_frontmatter(filepath: Path) -> Tuple[Dict, str]:
    """Load YAML frontmatter from markdown file.
    Returns (frontmatter_dict, content_without_frontmatter)"""
    content = filepath.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return {}, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    try:
        frontmatter = yaml.safe_load(parts[1])
        if frontmatter is None:
            frontmatter = {}
        return frontmatter, parts[2]
    except yaml.YAMLError:
        return {}, content

def check1_frontmatter_validity() -> List[str]:
    """Check 1: YAML frontmatter validity"""
    issues = []
    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.is_file():
            frontmatter, _ = load_frontmatter(md_file)
            if not frontmatter:
                issues.append(f"❌ {md_file.relative_to(WIKI_DIR)}: Missing or invalid YAML frontmatter")
            elif 'type' not in frontmatter:
                issues.append(f"❌ {md_file.relative_to(WIKI_DIR)}: Missing 'type' field")
            elif 'date' not in frontmatter:
                issues.append(f"❌ {md_file.relative_to(WIKI_DIR)}: Missing 'date' field")
    return issues

def check2_broken_wikilinks() -> List[str]:
    """Check 2: Broken wikilinks [[xxx]]"""
    issues = []
    # Collect all valid page slugs (without .md)
    valid_slugs = set()
    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.is_file():
            slug = md_file.stem
            valid_slugs.add(slug)

    # Check all wikilinks
    wikilink_pattern = re.compile(r'\[\[([^\]]+)\]\]')
    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.is_file():
            content = md_file.read_text(encoding='utf-8')
            for match in wikilink_pattern.finditer(content):
                target = match.group(1)
                # Remove anchor (#) if present
                target = target.split('#')[0]
                if target not in valid_slugs:
                    issues.append(f"❌ {md_file.relative_to(WIKI_DIR)}: Broken wikilink [[{target}]]")
    return issues

def check3_index_consistency() -> List[str]:
    """Check 3: Index consistency"""
    issues = []
    index_file = WIKI_DIR / "index.md"
    if not index_file.exists():
        issues.append("❌ wiki/index.md does not exist")
        return issues

    # This check would need to parse index.md content
    # For now, placeholder
    issues.append("⚠️ Check 3 (Index consistency) not fully implemented")
    return issues

def check4_stub_pages() -> List[str]:
    """Check 4: Stub pages (< 100 characters of content)"""
    issues = []
    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.is_file():
            frontmatter, content = load_frontmatter(md_file)
            # Count non-whitespace characters in content
            content_chars = len(re.sub(r'\s', '', content))
            if content_chars < 100:
                issues.append(f"⚠️ {md_file.relative_to(WIKI_DIR)}: Stub page ({content_chars} chars)")
    return issues

def jaccard_similarity(a: str, b: str) -> float:
    """Calculate Jaccard similarity between two strings"""
    set_a = set(a.lower())
    set_b = set(b.lower())
    if not set_a or not set_b:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)

def check5_near_duplicate_concepts() -> List[str]:
    """Check 5: Near duplicate concept names (Jaccard similarity > 0.7)"""
    issues = []
    concept_files = []
    for md_file in (WIKI_DIR / "concepts").glob("*.md"):
        if md_file.is_file():
            concept_files.append(md_file)

    for i, file1 in enumerate(concept_files):
        for file2 in concept_files[i+1:]:
            sim = jaccard_similarity(file1.stem, file2.stem)
            if sim > 0.7:
                issues.append(f"⚠️ Near duplicate: {file1.stem} ↔ {file2.stem} (similarity: {sim:.2f})")
    return issues

def check6_sha256_integrity() -> List[str]:
    """Check 6: SHA-256 integrity"""
    issues = []
    for md_file in (WIKI_DIR / "sources").glob("*.md"):
        if md_file.is_file():
            frontmatter, _ = load_frontmatter(md_file)
            if 'raw_file' in frontmatter and 'raw_sha256' in frontmatter:
                raw_path = RAW_DIR / frontmatter['raw_file']
                if raw_path.exists():
                    # Calculate SHA-256
                    sha256_hash = hashlib.sha256()
                    with open(raw_path, "rb") as f:
                        for byte_block in iter(lambda: f.read(4096), b""):
                            sha256_hash.update(byte_block)
                    calculated = sha256_hash.hexdigest()
                    if calculated != frontmatter['raw_sha256']:
                        issues.append(f"⚠️ SOURCE MODIFIED: {md_file.relative_to(WIKI_DIR)} - raw file hash mismatch")
                else:
                    issues.append(f"❌ {md_file.relative_to(WIKI_DIR)}: Raw file not found: {frontmatter['raw_file']}")
    return issues

def check7_stale_pages() -> List[str]:
    """Check 7: Stale pages"""
    issues = []
    volatility_thresholds = {'high': 90, 'medium': 180, 'low': 365}

    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.is_file():
            frontmatter, _ = load_frontmatter(md_file)
            if 'date' in frontmatter and 'domain_volatility' in frontmatter:
                try:
                    page_date = datetime.date.fromisoformat(frontmatter['date'])
                    days_old = (datetime.date.today() - page_date).days
                    threshold = volatility_thresholds.get(frontmatter['domain_volatility'], 365)
                    if days_old > threshold:
                        issues.append(f"⚠️ {md_file.relative_to(WIKI_DIR)}: Stale ({days_old} days old, threshold: {threshold})")
                except ValueError:
                    pass
    return issues

def check8_cross_language_duplicates() -> List[str]:
    """Check 8: Cross-language duplicates"""
    issues = []
    # Placeholder - would need to check source URLs and concept aliases
    issues.append("⚠️ Check 8 (Cross-language duplicates) not fully implemented")
    return issues

def check9_wikilink_format() -> List[str]:
    """Check 9: Wikilink format规范"""
    issues = []
    wikilink_pattern = re.compile(r'\[\[([^\]]+)\]\]')
    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.is_file():
            content = md_file.read_text(encoding='utf-8')
            for match in wikilink_pattern.finditer(content):
                target = match.group(1)
                # Check for non-English lowercase hyphenated format
                if re.search(r'[^a-z0-9\-]', target):
                    issues.append(f"❌ {md_file.relative_to(WIKI_DIR)}: Non-standard wikilink [[{target}]]")
    return issues

def main():
    """Main lint function"""
    print("Running knowledge base lint checks...")

    # Run all checks
    checks = [
        ("1. YAML frontmatter validity", check1_frontmatter_validity),
        ("2. Broken wikilinks", check2_broken_wikilinks),
        ("3. Index consistency", check3_index_consistency),
        ("4. Stub pages", check4_stub_pages),
        ("5. Near duplicate concept names", check5_near_duplicate_concepts),
        ("6. SHA-256 integrity", check6_sha256_integrity),
        ("7. Stale pages", check7_stale_pages),
        ("8. Cross-language duplicates", check8_cross_language_duplicates),
        ("9. Wikilink format规范", check9_wikilink_format),
    ]

    all_issues = []
    for check_name, check_func in checks:
        issues = check_func()
        all_issues.append((check_name, issues))
        print(f"{check_name}: {len(issues)} issues")

    # Create report
    OUTPUTS_DIR.mkdir(exist_ok=True)
    report_file = OUTPUTS_DIR / f"lint-{TODAY}.md"

    report_content = f"""---
graph-excluded: true
---

# Lint Report {TODAY}

Generated by scripts/lint.py

"""

    for check_name, issues in all_issues:
        report_content += f"\n## {check_name}\n\n"
        if issues:
            for issue in issues:
                report_content += f"- {issue}\n"
        else:
            report_content += "✅ No issues found\n"

    report_file.write_text(report_content, encoding='utf-8')
    print(f"\nReport written to: {report_file}")

    # Summary
    total_issues = sum(len(issues) for _, issues in all_issues)
    print(f"\nTotal issues found: {total_issues}")

    if total_issues > 0:
        print("\n⚠️  Some issues found. Review the report for details.")
        return 1
    else:
        print("\n✅ All checks passed!")
        return 0

if __name__ == "__main__":
    sys.exit(main())