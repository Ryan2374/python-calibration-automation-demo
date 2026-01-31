from instruments.mock_dmm import MockDMM
from instruments.mock_galil import MockGalilController
from calibration.validator import validate_results

def run_calibration():
    """
    Runs a simple calibration sequence using mocked instruments.
    Demonstrates a motion step (Galil-style) + measurement + validation.
    Returns a results dict suitable for validation and UI display.
    """
    galil = MockGalilController()
    dmm = MockDMM()

    # Motion step (simulated)
    galil.servo_on("A")
    galil.move_absolute("A", position=120)

    # Measurement step
    target_voltage = 120.0
    measured_voltage = dmm.measure_voltage(target_voltage)

    results = {
        "target_voltage": target_voltage,
        "measured_voltage": measured_voltage,
        "axis_position": galil.position,
    }

    validate_results(results, tolerance=1.0)
    return results
