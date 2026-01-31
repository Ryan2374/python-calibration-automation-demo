class MockGalil:
    def initialize(self):
        print("Galil controller initialized.")

    def set_voltage(self, voltage):
        print(f"Setting voltage to {voltage}V")
        return voltage
