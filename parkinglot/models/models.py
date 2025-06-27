from datetime import datetime
from enum import Enum
from typing import List


class BaseModel:
    def __init__(self, id: int):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


class BillStatus(Enum):
    PAID = 'PAID'
    PENDING = 'PENDING'
    PARTIALLY_PAID = 'PARTIALLY_PAID'


class FloorStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    FULL = 'FULL'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'


class GateStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'


class GateType(Enum):
    ENTRY = 'ENTRY'
    EXIT = 'EXIT'


class ParkingLotStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    FULL = 'FULL'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'


class PaymentModes(Enum):
    CASH = 'CASH'
    ONLINE = 'ONLINE'
    CARD = 'CARD'
    UPI = 'UPI'


class PaymentStatus(Enum):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


class SlotStatus(Enum):
    FILLED = 'FILLED'
    EMPTY = 'EMPTY'
    RESERVED = 'RESERVED'
    BLOCKED = 'BLOCKED'


class SlotAssignmentStrategyEnum(Enum):
    RANDOM = 'RANDOM'


class VehicleType(Enum):
    CAR = 'CAR'
    BIKE = 'BIKE'
    BUS = 'BUS'
    TRUCK = 'TRUCK'


class Bill(BaseModel):
    def __init__(self, id: int, exit_time: datetime, token, exited_at, payments: List, total_amount: int,
                 bill_status: BillStatus):
        super().__init__(id)
        self.exit_time = exit_time
        self.token = token
        self.exited_at = exited_at
        self.payments = payments
        self.total_amount = total_amount
        self.bill_status = bill_status


class Floor(BaseModel):
    def __init__(self, id: int, parking_slots_list: List, floor_number: int, floor_status: FloorStatus,
                 allowed_vehicles: List[VehicleType]):
        super().__init__(id)
        self.parking_slots_list = parking_slots_list
        self.floor_number = floor_number
        self.floor_status = floor_status
        self.allowed_vehicles = allowed_vehicles


class Gate(BaseModel):
    def __init__(self, id: int, gate_number: int, gate_type: GateType, parking_lot, gate_status: GateStatus):
        super().__init__(id)
        self.gate_number = gate_number
        self.gate_type = gate_type
        self.parking_lot = parking_lot
        self.gate_status = gate_status


class ParkingLot(BaseModel):
    def __init__(self, id: int, name: str, address: str, parking_floors: List[Floor], gates: List[Gate],
                 allowed_vehicles: List[VehicleType], capacity: int, status: ParkingLotStatus,
                 slot_assignment_strategy: SlotAssignmentStrategyEnum):
        super().__init__(id)
        self.name = name
        self.address = address
        self.parking_floors = parking_floors
        self.gates = gates
        self.allowed_vehicles = allowed_vehicles
        self.capacity = capacity
        self.status = status
        self.slot_assignment_strategy = slot_assignment_strategy


class Payment(BaseModel):
    def __init__(self, id: int, amount: int, payment_mode: PaymentModes, ref_id: str, bill,
                 payment_status: PaymentStatus, paid_at: datetime):
        super().__init__(id)
        self.amount = amount
        self.payment_mode = payment_mode
        self.ref_id = ref_id
        self.bill = bill
        self.payment_status = payment_status
        self.paid_at = paid_at


class Slot(BaseModel):
    def __init__(self, id: int, slot_number: int, vehicle_type: VehicleType, parking_slot_status: SlotStatus,
                 parking_floor: Floor):
        super().__init__(id)
        self.slot_number = slot_number
        self.vehicle_type = vehicle_type
        self.parking_slot_status = parking_slot_status
        self.parking_floor = parking_floor


class Ticket(BaseModel):
    def __init__(self, id: int, number: str, entry_time: datetime, vehicle, parking_slot: Slot, generated_gate: Gate):
        super().__init__(id)
        self.number = number
        self.entry_time = entry_time
        self.vehicle = vehicle
        self.parking_slot = parking_slot
        self.generated_gate = generated_gate


class Vehicle(BaseModel):
    def __init__(self, id: int, owner_name: str, vehicle_type: VehicleType):
        super().__init__(id)
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type