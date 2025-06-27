from parkinglot.models.models import SlotAssignmentStrategyEnum
from parkinglot.service.slot_strgy.RandomSlotFinder import RandomSlotFinder


class SlotFactory:

    @staticmethod
    def get_slot_strgy_obj(SlotStrgyEnum):
        if SlotStrgyEnum == SlotAssignmentStrategyEnum.RANDOM:
            return RandomSlotFinder()
