
class slotRepo:
    def __init__(self):
        self.slots = {}

    def update_slot(self, slot_id, slot):
        if slot_id in self.slots:
            self.slots[slot_id] = slot
        else:
            raise KeyError(f"Slot with ID {slot_id} does not exist.")