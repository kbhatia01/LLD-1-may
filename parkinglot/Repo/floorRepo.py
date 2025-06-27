
class FloorRepo:
    def __init__(self):
        self.floors = {}

    def add_floor(self, floor_id, floor_data):
        self.floors[floor_id] = floor_data

    def get_floor(self, floor_id):
        return self.floors.get(floor_id)

    def remove_floor(self, floor_id):
        if floor_id in self.floors:
            del self.floors[floor_id]

    def list_floors(self):
        return list(self.floors.keys())