from instruments.mock_dmm import MockDMM
from instruments.mock_galil import MockGalil
from calibration.validator import validate_results

def run_calibration():
    dmm = MockDMM()
    controller = MockGalil()

    print("Starting calibration sequence...")

    controller.initialize()
    voltage = controller.set_voltage(120)

    measurement = dmm.measure_voltage(voltage)
    results = {
        "target_voltage": 120,
        "measured_voltage": measurement
    }

    validate_results(results)
    print("Calibration complete.")
