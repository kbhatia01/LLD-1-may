from parkinglot.models.models import ParkingLot, ParkingLotStatus


class ParkingLotRepo:
    def __init__(self):
        self.parkingLot = {}




    def decrease_parking_lot_capacity(self, parkingLot: ParkingLot):
        if parkingLot.capacity > 0:
            parkingLot.capacity -= 1
        if parkingLot.capacity == 0:
           parkingLot.status = ParkingLotStatus.FULL

        self.parkingLot[parkingLot.id] = parkingLot