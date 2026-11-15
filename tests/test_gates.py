#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""End-to-end checks for the APEX scaffolders, gate auditors, skill names and installers.

Run from anywhere:  python tests/test_gates.py
No dependencies beyond the standard library. Exits non-zero if any check fails.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I2P = os.path.join(REPO, "skills", "apex")
REV = os.path.join(REPO, "skills", "apex-review")
INIT = os.path.join(I2P, "scripts", "init_project.py")
FIT = os.path.join(I2P, "scripts", "fitness_audit.py")
XRAY = os.path.join(REV, "scripts", "xray_scanner.py")
REVIEW = os.path.join(REV, "scripts", "review_gate_audit.py")

# Do not help the scripts with encoding: emulate a default Windows console.
ENV = {k: v for k, v in os.environ.items() if k not in ("PYTHONIOENCODING", "PYTHONUTF8")}
results = []


def run(script, *args):
    p = subprocess.run([sys.executable, script, *args], capture_output=True, env=ENV)
    return p.returncode, p.stdout.decode("utf-8", "replace") + p.stderr.decode("utf-8", "replace")


def check(name, cond, detail=""):
    results.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else f"\n   -> {str(detail)[-700:]}"))


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def edit_json(path, **changes):
    data = json.loads(read(path))
    data.update(changes)
    write(path, json.dumps(data, ensure_ascii=False))
    return data


def fill_docs(folder, score_label, score):
    """Replace every [[FILL]] marker in the ledger documents (not TRACE.md) with real-looking text."""
    for name in os.listdir(folder):
        if not name.endswith(".md") or name == "TRACE.md":
            continue
        path = os.path.join(folder, name)
        text = read(path)
        text = re.sub(r"(" + score_label + r":\W*)\[\[FILL:[^\]]*\]\]", lambda m: m.group(1) + str(score), text)
        text = re.sub(r"\[\[FILL: (score|/\d+|sum)\]\]", "14", text)
        text = re.sub(r"\[\[FILL:[^\]]*\]\]", "a real project-specific answer", text)
        write(path, text)


def set_slices(state_path, n_done):
    state = json.loads(read(state_path))
    for i, s in enumerate(state["slices"]):
        if i < n_done:
            s["status"], s["verification_proof"] = "done", "pytest tests/ -> 12 passed"
    write(state_path, json.dumps(state, ensure_ascii=False))


def scenarios(n):
    return [
        {"id": f"CS-{i}", "event": "price +15%", "expected": "history unchanged", "status": "pass", "proof": "test ok"}
        for i in range(1, n + 1)
    ]


def trace(rows, header="| ID | Need | Source | Weight | Status | Evidence / Reason |"):
    return "# TRACE\n\n" + header + "\n| :--- | :--- | :--- | :--- | :--- | :--- |\n" + "\n".join(rows) + "\n"


work = tempfile.mkdtemp(prefix="apex-tests-")
try:
    # ------------------------------------------------------------------ greenfield, ledger mode
    g = os.path.join(work, "Từ ý tưởng", "app")
    code = os.path.join(g, "src")
    write(os.path.join(code, "app.js"), "const cls = 'todo-list'; // see https://todo.example\nfetch('https://todoist.com')\n")
    rc, out = run(INIT, "--dir", g, "--name", "Demo")
    check("init_project runs on a non-ASCII path", rc == 0, out)
    bp = os.path.join(g, "docs", "apex-blueprint")
    state_path = os.path.join(bp, "STATE.json")
    trace_path = os.path.join(bp, "TRACE.md")

    rc, out = run(FIT, "--dir", g, "--gate", "1")
    check("blank scaffold: gate 1 vetoed", rc == 2 and "FILL" in out, out)
    rc, out = run(FIT, "--dir", g, "--gate", "4")
    check("blank scaffold: gate 4 vetoed", rc == 2, out)

    fill_docs(bp, "TOTAL C-SUITE AUDIT SCORE", 80)
    rc, out = run(FIT, "--dir", g, "--gate", "1")
    check("documents filled but TRACE.md still has a [[FILL]] row: gate 1 vetoed", rc == 2 and "TRACE.md" in out, out)
    write(trace_path, trace(["| R-01 | Import orders | user | High | OPEN | |"]))
    rc, out = run(FIT, "--dir", g, "--gate", "3")
    check("critique score 80: gate 3 vetoed", rc == 2 and "below 85" in out, out)
    score_doc = os.path.join(bp, "05-FITNESS-FUNCTIONS-AND-RUNBOOK.md")
    write(score_doc, re.sub(r"(AUDIT SCORE:\W*)80", r"\g<1>91", read(score_doc)))
    rc, out = run(FIT, "--dir", g, "--gate", "4")
    check("filled ledger, score 91: gate 4 approved", rc == 0, out)

    # Language independence: translate headings, drop the English score line, record the score in STATE.
    backup = {n: read(os.path.join(bp, n)) for n in os.listdir(bp) if n.endswith(".md")}
    for n, text in backup.items():
        if n == "TRACE.md":
            continue
        text = re.sub(r"(?m)^#+ .*$", "## Tiêu đề tiếng Việt", text)
        text = re.sub(r"(?m)^.*TOTAL C-SUITE AUDIT SCORE.*$", "- Tổng điểm phản biện: 91 trên 100", text)
        write(os.path.join(bp, n), text.replace("JTBD", "Việc cần làm").replace("Non-Goal", "Ngoài phạm vi"))
    rc, out = run(FIT, "--dir", g, "--gate", "4")
    check("ledger in Vietnamese without a score: gate 3+ vetoed with a clear hint", rc == 2 and "c_suite_audit_score" in out, out)
    edit_json(state_path, c_suite_audit_score=91)
    rc, out = run(FIT, "--dir", g, "--gate", "4")
    check("ledger in Vietnamese, score recorded in STATE: gate 4 approved", rc == 0, out)
    for n, text in backup.items():
        write(os.path.join(bp, n), text)
    edit_json(state_path, c_suite_audit_score=0)

    write(os.path.join(bp, "03-ARCHITECTURE-AND-SOPS.md"), "# 03\nok\n")
    rc, out = run(FIT, "--dir", g, "--gate", "4")
    check("nearly empty document: gate 4 vetoed", rc == 2 and "almost empty" in out, out)
    write(os.path.join(bp, "03-ARCHITECTURE-AND-SOPS.md"), backup["03-ARCHITECTURE-AND-SOPS.md"])

    write(trace_path, trace(["| R-01 | Import orders | user | High | OPEN | |"]))
    rc, out = run(FIT, "--dir", g, "--gate", "5", "--scan-code", code)
    check("gate 5 with no proven slice: vetoed", rc == 2 and "at least one slice" in out, out)
    set_slices(state_path, 1)
    rc, out = run(FIT, "--dir", g, "--gate", "5")
    check("gate 5 without --scan-code: vetoed", rc == 2 and "--scan-code" in out, out)
    rc, out = run(FIT, "--dir", g, "--gate", "5", "--scan-code", code)
    check("gate 5, one proven slice; 'todo-list' and URLs not flagged: approved", rc == 0, out)

    write(trace_path, trace(["| R-01 | Import orders | user | High | DONE | |"]))
    rc, out = run(FIT, "--dir", g, "--gate", "5", "--scan-code", code)
    check("DONE row without evidence: vetoed", rc == 2 and "needs evidence" in out, out)
    write(trace_path, trace(["| R-01 | Import orders | user | High | DEFERRED | check later |"]))
    rc, out = run(FIT, "--dir", g, "--gate", "5", "--scan-code", code)
    check("High row deferred without agreement: vetoed", rc == 2 and "without the user's agreement" in out, out)
    write(trace_path, trace(['| R-01 | Import orders | user | High | DEFERRED | agreed: "để sau Tết" |']))
    rc, out = run(FIT, "--dir", g, "--gate", "5", "--scan-code", code)
    check("High row deferred with agreed: quote: approved", rc == 0, out)

    write(trace_path, trace(["| R-01 | Import orders | user | High | OPEN | |"]))
    rc, out = run(FIT, "--dir", g, "--gate", "6", "--scan-code", code)
    check("gate 6 with pending slices: vetoed", rc == 2 and "every slice" in out, out)
    set_slices(state_path, 4)
    rc, out = run(FIT, "--dir", g, "--gate", "6", "--scan-code", code)
    check("gate 6: OPEN row and no change scenarios: vetoed", rc == 2 and "still OPEN" in out and "change_scenarios" in out, out)
    write(trace_path, trace(["| R-01 | Import orders | user | High | DONE | tests/import.test.js 12/12 |"]))
    edit_json(state_path, change_scenarios=scenarios(2))
    rc, out = run(FIT, "--dir", g, "--gate", "6", "--scan-code", code)
    check("gate 6 with 2 of 3 change scenarios: vetoed", rc == 2 and "found 2" in out, out)
    edit_json(state_path, change_scenarios=scenarios(1), change_scenarios_required=1)
    rc, out = run(FIT, "--dir", g, "--gate", "6", "--scan-code", code)
    check("fewer scenarios required without a waiver reason: vetoed", rc == 2 and "waiver" in out, out)
    edit_json(state_path, change_scenarios_waiver="one-off wedding plan; ends 2027-03-20")
    rc, out = run(FIT, "--dir", g, "--gate", "6", "--scan-code", code)
    check("fewer scenarios required with a waiver reason: approved", rc == 0, out)
    edit_json(state_path, change_scenarios=scenarios(3), change_scenarios_required=3, change_scenarios_waiver="")
    rc, out = run(FIT, "--dir", g, "--gate", "6", "--scan-code", code)
    check("gate 6 complete: approved", rc == 0, out)

    write(os.path.join(code, "calc.py"), "def f():\n    # TODO: real math\n    raise NotImplementedError\n")
    rc, out = run(FIT, "--dir", g, "--gate", "6", "--scan-code", code)
    check("real '# TODO' and raise NotImplementedError: vetoed", rc == 2 and "TODO marker" in out and "NotImplementedError" in out, out)

    g2 = os.path.join(work, "clinic")
    rc, out = run(INIT, "--dir", g2, "--name", "Nha khoa", "--domain", "phòng khám nha khoa, Đà Nẵng")
    st = json.loads(read(os.path.join(g2, "docs", "apex-blueprint", "STATE.json")))
    check("free-text domain kept as the label", rc == 0 and st["domain_label"] == "phòng khám nha khoa, Đà Nẵng", out)
    check("scaffolded STATE carries context_profile and required=3", "context_profile" in st and st["change_scenarios_required"] == 3, st.keys())

    # ------------------------------------------------------------------ greenfield, LEAN mode
    lean = os.path.join(work, "lean app")
    lean_code = os.path.join(lean, "src")
    write(os.path.join(lean_code, "main.py"), "print('ok')\n")
    rc, out = run(FIT, "--dir", lean, "--gate", "5", "--scan-code", lean_code)
    check("nothing to audit: exit 1 with a hint", rc == 1 and "--lean" in out, out)
    rc, out = run(INIT, "--dir", lean, "--name", "Lean", "--lean")
    made = sorted(os.listdir(os.path.join(lean, "_apex")))
    check("init --lean creates only _apex/TRACE.md and STATE.json", rc == 0 and made == ["STATE.json", "TRACE.md"] and not os.path.isdir(os.path.join(lean, "docs")), out + str(made))
    lean_trace = os.path.join(lean, "_apex", "TRACE.md")
    lean_state = os.path.join(lean, "_apex", "STATE.json")
    rc, out = run(FIT, "--dir", lean, "--gate", "5", "--scan-code", lean_code)
    check("LEAN: unresolved [[FILL]] row: vetoed", rc == 2 and "LEAN MODE" in out and "FILL" in out, out)
    write(lean_trace, trace(["| R-01 | Nhập đơn | user | High | DEFERRED | check later |"]))
    rc, out = run(FIT, "--dir", lean, "--gate", "2")
    check("LEAN: High row deferred without agreement is caught at any gate", rc == 2 and "without the user's agreement" in out, out)
    write(lean_trace, trace(
        ["| R-01 | Nhập đơn (Shopee \\| Facebook) | người dùng | High | **DONE** | test 12/12 |"],
        header="| Mã | Nhu cầu | Nguồn | Trọng số | Trạng thái | Bằng chứng |",
    ))
    rc, out = run(FIT, "--dir", lean, "--gate", "5", "--scan-code", lean_code)
    check("LEAN: translated header, escaped pipe, bold status: gate 5 approved", rc == 0, out)
    rc, out = run(FIT, "--dir", lean, "--gate", "5")
    check("LEAN: gate 5 without --scan-code: vetoed", rc == 2 and "--scan-code" in out, out)
    rc, out = run(FIT, "--dir", lean, "--gate", "6", "--scan-code", lean_code)
    check("LEAN: gate 6 without change scenarios: vetoed", rc == 2 and "change_scenarios" in out, out)
    edit_json(lean_state, change_scenarios_required=0, change_scenarios_waiver="one-off document")
    rc, out = run(FIT, "--dir", lean, "--gate", "6", "--scan-code", lean_code)
    check("LEAN: one-off work with a waiver: gate 6 approved", rc == 0, out)
    edit_json(lean_state, change_scenarios_required=3, change_scenarios_waiver="", change_scenarios=scenarios(3))
    rc, out = run(FIT, "--dir", lean, "--gate", "6", "--scan-code", lean_code)
    check("LEAN: 3 passed change scenarios: gate 6 approved", rc == 0, out)
    write(lean_trace, trace(["| R-01 | Nhập đơn | user | High | OPEN | |"]))
    rc, out = run(FIT, "--dir", lean, "--gate", "6", "--scan-code", lean_code)
    check("LEAN: OPEN row at gate 6: vetoed", rc == 2 and "still OPEN" in out, out)

    # ------------------------------------------------------------------ reviewer
    b = os.path.join(work, "Hóa đơn workspace")
    names = ["copywriting-notes.md", "dev2.py", "baogia_v2.xlsx", "report - Copy.docx", "Copy of plan.md", "hoadon (1).xlsx", "final_summary.md"]
    for n in names:
        write(os.path.join(b, n), "x")
    rc, out = run(XRAY, "--dir", b, "--name", "Demo", "--scan-only")
    check("xray --scan-only writes nothing", rc == 0 and sorted(os.listdir(b)) == sorted(names), out)
    rc, out = run(XRAY, "--dir", b, "--name", "Demo")
    check("xray_scanner runs on a non-ASCII path", rc == 0, out)
    rd = os.path.join(b, "docs", "apex-review")
    rstate_path = os.path.join(rd, "REVIEW-STATE.json")
    rstate = json.loads(read(rstate_path))
    check("duplicate detector: 4 real duplicates, 'copywriting' and 'dev2' ignored", rstate["xray_summary"]["entropy_count"] == 4, rstate["xray_summary"])
    check("upgraded score is not pre-filled", rstate["upgraded_health_score"] is None, rstate)
    check("no pre-selected option in the ledger", "Option B" not in read(os.path.join(rd, "01-FORENSIC-XRAY-AND-LEAKS.md")))
    rc, out = run(REVIEW, "--dir", b, "--gate", "2")
    check("blank review ledger: gate 2 vetoed", rc == 2 and "FILL" in out, out)
    fill_docs(rd, "TOTAL UPGRADED SCORE", 90)
    write(os.path.join(rd, "TRACE.md"), trace(["| R-01 | Verified backup | discovered | High | OPEN | |"]))
    rc, out = run(REVIEW, "--dir", b, "--gate", "4")
    check("filled review ledger, score 90: gate 4 approved", rc == 0, out)
    rc, out = run(REVIEW, "--dir", b, "--gate", "5", "--scan-target", b)
    check("review gate 5 without a proven slice: vetoed", rc == 2 and "at least one slice" in out, out)
    set_slices(rstate_path, 4)
    write(os.path.join(rd, "TRACE.md"), trace(["| R-01 | Verified backup | discovered | High | DONE | backup.zip sha256 verified |"]))
    edit_json(rstate_path, change_scenarios=scenarios(3))
    rc, out = run(REVIEW, "--dir", b, "--gate", "6", "--scan-target", b)
    check("review gate 6 complete: approved", rc == 0, out)

    b2 = os.path.join(work, "farm")
    write(os.path.join(b2, "so_thu_mua.csv"), "a,b\n")
    rc, out = run(XRAY, "--dir", b2, "--name", "HTX", "--domain", "hợp tác xã nông nghiệp", "--lean")
    made = sorted(os.listdir(os.path.join(b2, "_apex")))
    check("xray --lean creates only _apex/TRACE.md and STATE.json", rc == 0 and made == ["STATE.json", "TRACE.md"] and not os.path.isdir(os.path.join(b2, "docs")), out + str(made))
    rc, out = run(XRAY, "--dir", b2, "--name", "HTX", "--scan-only")
    check("xray does not count its own _apex files", "Total Files Scanned : 1 " in out, out)
    write(os.path.join(b2, "_apex", "TRACE.md"), trace(["| R-01 | Sao lưu | discovered | High | DONE | sha256 ok |"]))
    rc, out = run(REVIEW, "--dir", b2, "--gate", "5", "--scan-target", b2)
    check("review LEAN: gate 5 approved", rc == 0 and "LEAN MODE" in out, out)

    # ------------------------------------------------------------------ projects built with an older APEX version
    old = os.path.join(work, "old app")
    old_bp = os.path.join(old, "docs", "apex-blueprint")
    write(os.path.join(old, "src", "a.py"), "print(1)\n")
    write(os.path.join(old_bp, "STATE.json"), json.dumps({"schema_version": "2.0.0-apex", "c_suite_audit_score": 93, "slices": []}))
    write(os.path.join(old_bp, "00-PROJECT-CONSTITUTION.md"), "# Old\n" + "pre-filled template text " * 30)
    rc, out = run(FIT, "--dir", old, "--gate", "4")
    check("pre-v4 ledger is not audited as if it were real: exit 1 with guidance", rc == 1 and "LEGACY" in out and "--lean" in out, out)
    rc, out = run(INIT, "--dir", old, "--name", "Old")
    check("scaffolder refuses to mix into a pre-v4 ledger", rc == 1 and "LEGACY" in out and read(os.path.join(old_bp, "00-PROJECT-CONSTITUTION.md")).startswith("# Old"), out)
    rc, out = run(XRAY, "--dir", old, "--name", "Old", "--scan-only")
    check("Turn-1 inventory reports earlier APEX files", rc == 0 and "Earlier APEX files" in out and "do not trust its scores" in out, out)
    rc, out = run(INIT, "--dir", old, "--name", "Old", "--lean")
    write(os.path.join(old, "_apex", "TRACE.md"), trace(["| R-01 | Fix totals | user | High | DONE | recalculated, 0 errors |"]))
    rc, out = run(FIT, "--dir", old, "--gate", "5", "--scan-code", os.path.join(old, "src"))
    check("with a fresh _apex trace, the audit ignores the old ledger and runs LEAN checks", rc == 0 and "LEAN MODE" in out, out)

    # ------------------------------------------------------------------ reviewing an app that already has its own TODOs
    live = os.path.join(work, "live app")
    write(os.path.join(live, "legacy", "invoice_service.py"), "def total():\n    # TODO: handle refunds (owner's old note)\n    return 0\n")
    write(os.path.join(live, ".env"), "KEY=x\n")
    write(os.path.join(live, "hoa_don_2024.csv"), "a,b\n")
    write(os.path.join(live, "upgrade", "quote.py"), "def quote():\n    return 1\n")
    rc, out = run(XRAY, "--dir", live, "--name", "Live", "--scan-only")
    red = next((l for l in out.splitlines() if "Red-Zone files" in l), "")
    yellow = next((l for l in out.splitlines() if "Yellow-Zone files" in l), "")
    check("zoning: code named 'invoice' is change-with-tests, .env and invoice data are protected",
          "invoice_service.py" in yellow and "invoice_service.py" not in red and ".env" in red and "hoa_don_2024.csv" in red, out)
    check("no invented baseline score is printed", "Baseline Score" not in out, out)
    rc, out = run(XRAY, "--dir", live, "--name", "Live", "--lean")
    write(os.path.join(live, "_apex", "TRACE.md"), trace(["| R-01 | New quote tool | owner | High | DONE | python upgrade/quote.py -> 1 |"]))
    rc, out = run(REVIEW, "--dir", live, "--gate", "5", "--scan-target", live)
    check("scanning the whole app trips on the owner's old TODO, with advice to scan only your own files",
          rc == 2 and "scan only your own files" in out, out)
    rc, out = run(REVIEW, "--dir", live, "--gate", "5", "--scan-target", os.path.join(live, "upgrade"), os.path.join(live, "upgrade", "quote.py"))
    check("scanning only the files you built (a folder and a file): approved", rc == 0 and "Scanned 2 source files" in out, out)

    broken = os.path.join(work, "broken state")
    rc, out = run(INIT, "--dir", broken, "--name", "B")
    write(os.path.join(broken, "docs", "apex-blueprint", "STATE.json"), "{ not json")
    rc, out = run(FIT, "--dir", broken, "--gate", "1")
    check("a broken STATE.json is reported as an error to fix, not as an old version", rc == 1 and "could not be read" in out and "LEGACY" not in out, out)

    # ------------------------------------------------------------------ packaging consistency
    check("exactly two skills are shipped: apex and apex-review", sorted(os.listdir(os.path.join(REPO, "skills"))) == ["apex", "apex-review"],
          os.listdir(os.path.join(REPO, "skills")))
    names = [re.search(r"(?m)^name: (.+)$", read(os.path.join(s, "SKILL.md"))).group(1).strip() for s in (I2P, REV)]
    check("skill names match their folders, so they are invoked as /apex and /apex-review", names == ["apex", "apex-review"], names)
    check("no separate command files: the two skill names are the only entry points", not os.path.isdir(os.path.join(REPO, "commands")))
    review_desc = re.search(r"(?s)description: >-\n(.*?)\n---", read(os.path.join(REV, "SKILL.md"))).group(1)
    check("apex-review says it is not for code, PR or diff reviews", "pull request" in review_desc and "code review" in review_desc, review_desc[:200])
    check("skill descriptions fit the 1024-character limit",
          all(len(" ".join(re.search(r"(?s)description: >-\n(.*?)\n---", read(os.path.join(s, "SKILL.md"))).group(1).split())) <= 1024 for s in (I2P, REV)))
    installers = read(os.path.join(REPO, "install-skills.ps1")) + read(os.path.join(REPO, "install-skills.sh"))
    check("installers remove the pre-v4.5 skill names and embed no behaviour rules",
          installers.count("idea-to-product-apex") >= 2 and "MANDATORY" not in installers and "2-SECTION" not in installers)
    stale = []
    for root, _dirs, files in os.walk(os.path.join(REPO, "skills")):
        for f in files:
            if f.endswith((".md", ".py")) and re.search(r"idea-to-product-apex|product-workspace-reviewer-apex", read(os.path.join(root, f))):
                stale.append(f)
    check("no old skill names left inside the skills", not stale, stale)
    check("install-skills.ps1 is ASCII-only apart from an optional BOM (safe for Windows PowerShell 5.1)",
          all(ord(ch) < 128 for ch in read(os.path.join(REPO, "install-skills.ps1")).lstrip("﻿")))
    shared = ["07-completeness-lenses.md", "08-definition-of-done-and-traceability.md", "09-domain-discovery-protocol.md"]
    check("shared references 07-09 are identical in both skills",
          all(read(os.path.join(I2P, "references", s)) == read(os.path.join(REV, "references", s)) for s in shared))
    manifests = ["plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json", ".cursor-plugin/plugin.json", ".antigravity-plugin/plugin.json"]
    versions = {json.loads(read(os.path.join(REPO, m)))["version"] for m in manifests}
    market = json.loads(read(os.path.join(REPO, ".claude-plugin", "marketplace.json")))
    versions |= {market["metadata"]["version"]} | {p["version"] for p in market["plugins"]}
    check("all manifests carry the same version", len(versions) == 1, versions)
    links_ok = True
    for skill in (I2P, REV):
        for target in re.findall(r"\]\(\./(references/[^)#]+)", read(os.path.join(skill, "SKILL.md"))):
            links_ok &= os.path.isfile(os.path.join(skill, target))
    check("every reference linked from SKILL.md exists", links_ok)
finally:
    shutil.rmtree(work, ignore_errors=True)

print(f"\n{sum(results)}/{len(results)} checks passed")
sys.exit(0 if all(results) else 1)
