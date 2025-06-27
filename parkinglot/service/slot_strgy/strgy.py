from abc import ABC, abstractmethod

from parkinglot.models.models import Ticket, ParkingLot, VehicleType


class strgy(ABC):

    @abstractmethod
    def get_slots(self, vehicleType: VehicleType, parkingLot: ParkingLot):
        pass