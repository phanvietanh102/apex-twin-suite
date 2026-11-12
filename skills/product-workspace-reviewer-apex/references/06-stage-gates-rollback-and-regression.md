# 06. Shift-Left Review Stage Gates, Pre-Flight Rollback & Behavioral Parity Verification

## 1. Zero-Bloat Context Isolation for Large Workspaces

When reviewing an existing codebase or workspace that may contain hundreds of files:
1. **Never Read All Files Into Context Blindly:** Always run `scripts/xray_scanner.py` first to generate a statistical & structural map in seconds without burning context tokens.
2. **Phase-Isolated Reference Loading:** Read only the reference module (`01`..`06`) matching the current active phase. During Phase 5 (Surgical Refactoring), drop diagnostic prose and dedicate **95% of output tokens to executing clean, verified upgrades**.
3. **3 Adaptive Review Modes:**
   * **`LEAN` (`/apex-review-lean`):** 1 compact diagnostic & upgrade file + immediate surgical execution.
   * **`STANDARD` (`/apex-review`):** Full 6-gate forensic review and surgical 4-slice upgrade.
   * **`DEEP-ENTERPRISE`:** Full 6-file ledger + Isolated Subagent Forensic Critic + full parity test suite.

---

## 2. Shift-Left Stage-Gate Circuit Breakers (Gates 1 $\rightarrow$ 6)

Just like `idea-to-product-apex`, **never wait until Step 6 to discover an audit or refactoring mistake made at Step 2!**

| Gate | Trigger Point | Mandatory Verification Command / Check | Block / Veto Condition |
| :--- | :--- | :--- | :--- |
| **Gate 1** | End of Phase 1 (X-Ray & Discovery) | `review_gate_audit.py --gate 1` + User confirmation | Blocked if `xray_scanner.py` wasn't run, Sacred Habits weren't locked, or Green/Yellow/Red Zones are undefined. |
| **Gate 2** | End of Phase 2 (Leaks & Kano Spec) | `review_gate_audit.py --gate 2` | Blocked if $<4$ Silent Leaks are quantified or if 30% Kano Modernization upgrades risk breaking Red Zones. |
| **Gate 3** | End of Phase 3 (C-Suite Diagnostic) | `review_gate_audit.py --gate 3` (After Score $\ge 85/100$) | Blocked if Baseline vs. After Delta Scorecard is missing, or if any C-Suite role omitted quantitative forensic proof. |
| **Gate 4** | End of Phase 4 (Strangler Blueprint) | `review_gate_audit.py --gate 4` | Blocked if Tier-B Config extraction plan or Pre-Flight Backup & Rollback path is missing. |
| **Gate 5** | During Phase 5 (After **EVERY** Surgical Slice) | `review_gate_audit.py --gate 5 --scan-target <dir>` + **Parity Tests** | Blocked if Pre-Flight Snapshot wasn't created, if Behavioral Parity test fails, or if `TODO`/stub/duplicate `v1_copy` files remain. |
| **Gate 6** | End of Phase 6 (Delta Report & Handover) | `review_gate_audit.py --gate 6 --scan-target <dir>` | Blocked if Before/After Delta Report, Rollback Test, or Quarterly Drift Prompt is incomplete. |

---

## 3. The 4-Step Surgical Refactor & Behavioral Parity Protocol (Phase 5)

Before modifying, moving, or refactoring ANY existing file in Phase 5, execute these 4 mandatory safety steps:

### Step 1: Pre-Flight Snapshot Backup
* Create a manifest or backup copy of any Yellow/Red Zone files being touched (or verify clean Git working tree) so any change can be reversed in 10 seconds.

### Step 2: Behavioral Parity Regression Test
* Capture 3–5 real historical inputs/cases from the existing system and record their exact outputs.
* Run those same 3–5 inputs through the refactored/upgraded system:
  * Core deterministic numbers/logic MUST match 100% (unless fixing an explicitly confirmed bug documented in `02-KANO-UPGRADE-SPEC.md`).
  * New Kano Delighters must enrich the output without corrupting legacy fields.

### Step 3: Internal Link & Reference Integrity Check
* When reorganizing folders or renaming messy files, scan all scripts, HTML/Markdown links, and spreadsheet/config references to ensure zero broken paths (`FileNotFoundError` / `404`).

### Step 4: Automated Code & Workspace Hygiene Scan
* Run `python "<skill_dir>/scripts/review_gate_audit.py" --dir "<target_dir>" --gate 5 --scan-target "<target_dir>"` to verify zero unfinished `TODO`/`FIXME` stubs and zero newly created duplicate clutter.
