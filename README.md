# Python Calibration Automation Demo

A lightweight Python project demonstrating a production-style calibration workflow using mocked instruments.
Includes a Galil-style motion controller mock and a Flask web UI to run the workflow.

## Features
- Calibration workflow orchestration (Python)
- Mocked instrument interfaces (DMM + Galil-style motion)
- Tolerance-based validation
- Unit tests (pytest)
- Minimal Flask web UI to trigger runs and show pass/fail results

## Run (CLI)
```bash
python main.py
