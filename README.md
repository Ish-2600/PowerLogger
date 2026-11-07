# Formula SAE Power Logger

ESP32 DC voltage, current and power logging for the battery and rectifier.

**Progress:** Stage 1 (audit and design specification) is complete and independently reviewed. Firmware implementation, PCB design and enclosure models are the next stages. Work proceeds one stage at a time.

Start with the [design specification](docs/STAGE_1_DESIGN.md), [delivery stages](docs/STAGES.md) and [independent review](reports/stage-1-review.md).

## Folder map

```text
PowerLogger_Project/
├── README.md                 Project entry point
├── platformio.ini            Draft ESP32/native build configuration
├── lib/power_logger/         Existing portable C++ source
├── src/                      ESP32 application code (planned)
├── include/                  Shared application headers (planned)
├── test/                     Unity module tests (planned)
├── data/
│   ├── fixtures/             Original power measurement fixture
│   └── synthetic/            Separate synthetic OBD dataset
├── docs/
│   ├── STAGE_1_DESIGN.md      Requirements and proposed architecture
│   ├── STAGES.md              Delivery progress
│   └── references/           Original README snapshot
├── reports/                  Input audit and review results
├── tools/                    Local validation scripts
├── hardware/                 PCB files (Stage 3)
├── models/                   Enclosure models (Stage 4)
├── private/references/       Original project PDF; ignored by Git
└── .codex/context/           Project navigation and continuation notes
```

The original source and datasets were moved without changing their contents. The [original README](docs/references/original-readme.md) is retained as a historical snapshot; its old file paths describe the original layout.

## Checks available now

Run from this folder:

```bash
clang++ -std=c++17 -Wall -Wextra -Werror -fsyntax-only lib/power_logger/power_logger.cpp
python3 tools/audit_inputs.py
```

The second command checks the supplied datasets and refreshes `reports/input-audit.json`. The power fixture has 1,000 samples; the separate synthetic OBD file has 100,000 rows.

`platformio.ini` is a scaffold. There are no implemented ESP32 application or Unity tests yet, so it is not a working firmware build.

## Local and private files

`.gitignore` excludes private files, local secret files, `.venv/`, `.pio/` and build artifacts. No `.env` or `.env.example` is needed. The original PDF is preserved in `private/references/` and excluded from future tracking; it remains in earlier Git history.
