# Repository guide
Workspace: /Users/error/Desktop/powerLogger_Project
Updated: 2026-11-06

- `README.md`: current project entry point and folder map.
- `docs/references/original-readme.md`: unchanged original README snapshot; paths are historical.
- `lib/power_logger/power_logger.cpp`: original PowerSample and power helper, no main/firmware entry point.
- `data/fixtures/power_logger_test_data.csv`: 1000-row four-column 250ms fixture.
- `private/references/`: original PDF, ignored locally; contains contact information, do not reproduce it.
- `data/synthetic/fake_car_obd_data.csv`: user-provided untracked 100000-row synthetic OBD data; unrelated current-sensing schema.
- `docs/STAGE_1_DESIGN.md`: audit, proposed hardware, architecture, planned tests and completion gates.
- `docs/STAGES.md`: delivery progress; user wants one stage per turn.
- `reports/input-audit.json`: observed fixture statistics; reproduce with `python3 tools/audit_inputs.py` (passed).
- `reports/stage-1-review.md`: independent design review and resolutions.
- `platformio.ini`: unvalidated native/ESP32 scaffold only, no implementation or tests yet.
- `.gitignore`: excludes local secret files and original contact-bearing PDF; no `.env` or example file supplied.
- `.venv/`: ignored local PlatformIO/pypdf installation.

Verified command (success): `clang++ -std=c++17 -Wall -Wextra -Werror -fsyntax-only lib/power_logger/power_logger.cpp`.
Planned later: `.venv/bin/pio test -e native`, `.venv/bin/pio run -e esp32dev`, `.venv/bin/pio run -e esp32_demo` (not yet run).
