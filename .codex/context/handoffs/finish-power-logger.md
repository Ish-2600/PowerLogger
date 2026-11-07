# Finish power logger
Workspace: /Users/error/Desktop/powerLogger_Project
Updated: 2026-11-06
Status: Stage 1 complete; folder organization requested afterward is complete. STOP before Stage 2.
User wants one stage per turn (supersedes initial request to finish everything before returning).
Goal: simple C++17 ESP32 firmware; Unity tests for every module; actual PCB design/fab files; enclosure models; full overview.
User explicitly requested another model to check work; stage1_review completed and corrections applied.
Sensitive data: user corrected .env request to .gitignore, explicitly no .env.example. Temporary empty .env/example removed. Ignore secret/private files; do not put values in .gitignore.
Original contact-bearing PDF kept on disk, ignored and git rm --cached staged; prior history remains. Original code/README/CSVs preserved. Synthetic OBD CSV was already user-untracked.
Baseline: dual INA226 with external 200A/75mV four-terminal shunts; genuine 38-pin DevKitC V4 carrier; microSD. High current off PCB. Pin proposal in design doc; not hardware validated.
Organization: C++ moved unchanged to lib/power_logger/; power CSV to data/fixtures/; OBD CSV to data/synthetic/; PDF to ignored private/references/.
Original README archived unchanged in docs/references/original-readme.md; root README now maps folders. Script/documentation paths updated; hardware/models folders have stage placeholders.
Checks PASSED after moves: SHA256 unchanged for all five relocated files; clang++ strict syntax on lib/power_logger/power_logger.cpp; python3 tools/audit_inputs.py. Private PDF remains ignored; no Unity/firmware build yet.
Data: 1000 fixture rows,250ms, max P rounding error0.005W; unrelated 100000-row synthetic OBD file.
Tools: .venv has PlatformIO6.2.0/pypdf. KiCad download succeeded but installation failed needing interactive admin authentication. Homebrew OpenSCAD cask disabled. Neither CAD tool installed; resolve later without bypassing Gatekeeper.
Next only after user says continue: Stage2 implement portable modules and adapters, Unity tests/module matrix, CSV analysis/demo; build native tests and ESP32+demo. Stage3 PCB; Stage4 enclosure; Stage5 final independent review/overview.
PCB must resolve power/transient protection, exact parts/footprints, sizing; quantify accuracy/error budget. No vehicle-use/physical fit claims without hardware.
