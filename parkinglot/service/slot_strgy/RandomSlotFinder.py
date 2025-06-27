from parkinglot.models.models import SlotStatus, Slot
from parkinglot.service.slot_strgy.strgy import strgy


class RandomSlotFinder(strgy):
    def get_slots(self, vehicleType, parkingLot) -> Slot:
        for floor in parkingLot.parking_floors:
            if vehicleType in floor.allowed_vehicles:
                for slot in floor.parking_slots_list:
                    if slot.parking_slot_status == SlotStatus.EMPTY and slot.vehicle_type == vehicleType:
                        return slot

        return None