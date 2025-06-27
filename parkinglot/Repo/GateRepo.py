from parkinglot.models.models import Gate


class GateRepo:
    def __init__(self):
        self.gates = {}


    def get_gate_by_id(self, gate_id) -> Gate:
        return self.gates.get(gate_id)