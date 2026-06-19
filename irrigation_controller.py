import random
import time
from datetime import datetime

class SoilMoistureSensor:
    def __init__(self):
        self.moisture = 0

    def read(self):
        self.moisture = random.randint(0, 100)
        return self.moisture

class Relay:
    def __init__(self):
        self.state = "OFF"

    def on(self):
        self.state = "ON"
        print("  💧 PUMP: ON")

    def off(self):
        self.state = "OFF"
        print("  💧 PUMP: OFF")

class IrrigationController:
    def __init__(self, threshold=30):
        self.threshold = threshold
        self.sensor = SoilMoistureSensor()
        self.relay = Relay()
        self.watering = False
        self.last_reading = 0
        self.hysteresis = 5

    def check_soil(self):
        moisture = self.sensor.read()
        self.last_reading = moisture

        print(f"\n[{datetime.now().strftime('%H:%M:%S')}]")
        print(f"  Soil Moisture: {moisture}%")

        if moisture < self.threshold:
            if not self.watering:
                self.relay.on()
                self.watering = True
            else:
                print("  Pump already running")

        elif moisture > (self.threshold + self.hysteresis):
            if self.watering:
                self.relay.off()
                self.watering = False
            else:
                print("  Soil moisture is sufficient")

        else:
            status = "Running" if self.watering else "OFF"
            print(f"  Threshold boundary (hysteresis zone). Pump: {status}")

    def run(self, duration=10):
        print("\n" + "=" * 60)
        print("   AUTOMATED IRRIGATION CONTROLLER")
        print("=" * 60)
        print(f"  Soil Moisture Threshold: {self.threshold}%")
        print(f"  Hysteresis Buffer: ±{self.hysteresis}%")
        print("=" * 60 + "\n")

        try:
            for _ in range(duration):
                self.check_soil()
                time.sleep(2)

        except KeyboardInterrupt:
            print("\n👋 System stopped by user.")

        finally:
            if self.watering:
                self.relay.off()
            print("\nSystem shutdown complete.")

def main():
    controller = IrrigationController(threshold=30)

    controller.run(duration=15)

    print("\n" + "=" * 60)
    print("   SIMULATION COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()