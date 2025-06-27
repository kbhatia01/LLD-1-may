from parkinglot.models.models import Vehicle


class VehicleRepo:
    def __init__(self):
        self.vehicles = {}


    def find_vehicle_by_number(self, vehicle_number):
        return self.vehicles.get(vehicle_number)

    def save(self, vehicle: Vehicle):
        if vehicle.vehicle_number in self.vehicles:
            raise ValueError("Vehicle already exists")
        self.vehicles[vehicle.vehicle_number] = vehicle