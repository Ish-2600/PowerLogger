#!/usr/bin/env python3
"""Reproduce Stage 1 input checks without modifying original files."""
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    with (ROOT / 'data/fixtures/power_logger_test_data.csv').open(newline='') as source:
        reader = csv.DictReader(source)
        columns = reader.fieldnames
        if columns != ['time_ms', 'voltage_v', 'current_a', 'power_w']:
            raise ValueError('Unexpected power fixture schema')
        rows = [{k: float(v) for k, v in row.items()} for row in reader]
    if not rows:
        raise ValueError('Empty power fixture')
    steps = [b['time_ms'] - a['time_ms'] for a, b in zip(rows, rows[1:])]
    differences = [abs(r['power_w'] - r['voltage_v'] * r['current_a']) for r in rows]
    with (ROOT / 'data/synthetic/fake_car_obd_data.csv').open(newline='') as source:
        reader = csv.DictReader(source)
        obd = {'columns': reader.fieldnames, 'rows': sum(1 for _ in reader)}
    report = {
        'rows': len(rows), 'columns': columns,
        'min': {k: min(r[k] for r in rows) for k in columns},
        'max': {k: max(r[k] for r in rows) for k in columns},
        'timestamp_steps_ms': sorted(set(steps)),
        'nonfinite_rows': [i + 2 for i, r in enumerate(rows)
                           if not all(math.isfinite(v) for v in r.values())],
        'max_power_disagreement_w': max(differences),
        'power_disagreement_over_0_02_w': sum(d > 0.02 for d in differences),
        'unrelated_synthetic_obd': obd,
    }
    destination = ROOT / 'reports' / 'input-audit.json'
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + '\n')
    if report['nonfinite_rows'] or report['power_disagreement_over_0_02_w']:
        raise ValueError('Power fixture validation failed; inspect report')
    if report['timestamp_steps_ms'] != [250.0]:
        raise ValueError('Unexpected fixture timestamp interval')
    print(f"PASS: {len(rows)} power samples; {obd['rows']} synthetic OBD rows")
    print(f'Maximum power rounding difference: {max(differences):.6f} W')

if __name__ == '__main__':
    main()
