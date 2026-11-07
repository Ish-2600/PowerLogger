<div align="center">

# ⚡ Formula SAE Power Logger

### DC power telemetry for the battery and rectifier

![Project stage](https://img.shields.io/badge/stage-foundation-0f766e?style=for-the-badge)
![Language](https://img.shields.io/badge/language-C%2B%2B17-1f6feb?style=for-the-badge)
![Focus](https://img.shields.io/badge/focus-data_acquisition-f59e0b?style=for-the-badge)

</div>

> **Mission:** build the software foundation for a PCB-based logger that captures vehicle DC voltage and high-current measurements, then derives real-time power consumption.

---

## 🏎️ Why it matters

Battery and rectifier measurements reveal what the vehicle is consuming during startup, idle, and dynamic powertrain operation. The project brief identifies a typical idle draw of roughly **16–22 A**, startup draw around **80–120 A**, and peaks approaching **160 A**. Capturing these signals makes system behavior measurable instead of assumed.

| Signal | Measurement path | Result |
| :--- | :--- | :--- |
| **Voltage** | Battery / rectifier DC bus | `voltage_v` |
| **Current** | Ammeter shunt | `current_a` |
| **Power** | \( P = V \times I \) | `power_w` |

## 📊 Data contract

The supplied test set contains **1,000 samples** recorded at 250 ms intervals. Its columns are intentionally unit-bearing so that logs stay unambiguous across firmware, desktop tools, and analysis scripts.

```csv
time_ms,voltage_v,current_a,power_w
0,12.62,0.18,2.27
250,12.58,84.70,1065.53
500,12.41,121.30,1505.33
```

| Observed test-data range | Value |
| :--- | ---: |
| Voltage | 12.08–13.88 V |
| Current | 0.18–158.40 A |
| Power | 2.27–1913.47 W |

## 🧩 Project map

```text
PowerLogger_Project/
├── power_logger.cpp                    # Core C++ data model and P = V × I helper
├── power_logger_test_data.csv          # Supplied representative measurement data
└── Electrical Project Power Logger (1).pdf  # Original project brief
```

The current C++ foundation exposes a `PowerSample` with timestamp, voltage, and current fields, plus a constexpr power calculation. It deliberately has no `main()` yet; the next implementation can target the eventual firmware or a desktop analysis tool without prematurely choosing a platform.

## 🛠️ Quick check

Validate the current source without producing an executable:

```bash
clang++ -std=c++17 -fsyntax-only power_logger.cpp
```

## 🗺️ Roadmap

- [x] Define a unit-aware power-sample representation
- [x] Preserve representative voltage/current/power test data
- [ ] Define shunt calibration and ADC conversion logic
- [ ] Add CSV ingestion and validation
- [ ] Implement logging, fault handling, and hardware-target integration
- [ ] Compare recorded results with the supplied test data

## ⚠️ Engineering note

This repository is a software starting point, not a validated electrical design. Any implementation connected to the vehicle must be reviewed for sensor range, isolation, fusing, grounding, transient protection, and Formula SAE rules before use.

---

<div align="center">
  <sub>Measure clearly. Diagnose confidently. Drive informed.</sub>
</div>
