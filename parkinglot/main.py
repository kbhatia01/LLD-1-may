from parkinglot.Repo.GateRepo import GateRepo
from parkinglot.Repo.ParkingLotRepo import ParkingLotRepo
from parkinglot.Repo.Slots import slotRepo
from parkinglot.Repo.floorRepo import FloorRepo
from parkinglot.Repo.ticketRepo import TicketRepo
from parkinglot.Repo.vehicleRepo import VehicleRepo
from parkinglot.controller.IssueTicket import IssueTicket
from parkinglot.dtos.TicketIssueRequest import TicketIssueRequest
from parkinglot.dtos.TicketResponseDto import TicketResponseDto
from parkinglot.models.models import ParkingLot, VehicleType, SlotAssignmentStrategyEnum, ParkingLotStatus, Floor, \
    FloorStatus, Slot, SlotStatus, Gate, GateType, GateStatus
from parkinglot.service.TicketService import TicketService


def admin(gateRepo, parkingRepo, slotsRepo):
    parking_lot = ParkingLot(
        id=1,
        name="Main Parking Lot",
        address="123 Main St",
        parking_floors=[],
        gates=[],
        allowed_vehicles=[VehicleType.CAR, VehicleType.BIKE],
        capacity=2,
        status=ParkingLotStatus.OPEN,
        slot_assignment_strategy=SlotAssignmentStrategyEnum.RANDOM
    )
    # Create Floor
    floor = Floor(
        id=1,
        parking_slots_list=[],
        floor_number=1,
        floor_status=FloorStatus.OPEN,
        allowed_vehicles=[VehicleType.CAR, VehicleType.BIKE]
    )

    slot1 = Slot(
        id=1,
        slot_number=1,
        vehicle_type=VehicleType.CAR,
        parking_slot_status=SlotStatus.EMPTY,
        parking_floor=floor
    )
    slot2 = Slot(
        id=2,
        slot_number=2,
        vehicle_type=VehicleType.BIKE,
        parking_slot_status=SlotStatus.EMPTY,
        parking_floor=floor
    )

    floor.parking_slots_list = [slot1, slot2]

    parking_lot.parking_floors = [floor]

    parkingRepo.parkingLot[parking_lot.id] = parking_lot

    gate = Gate(
        id=1,
        gate_number=1,
        gate_type=GateType.ENTRY,
        parking_lot=parking_lot,
        gate_status=GateStatus.OPEN
    )

    parking_lot.gates = [gate]
    gateRepo.gates[gate.id] = gate

    slotsRepo.slots[slot1.id] = slot1
    slotsRepo.slots[slot2.id] = slot2


if __name__ == '__main__':
    gateRepo = GateRepo()
    parkingRepo = ParkingLotRepo()
    slotsRepo = slotRepo()
    floorRepo = FloorRepo()
    ticketRepo = TicketRepo()
    vehicleRepo = VehicleRepo()

    admin(gateRepo, parkingRepo, slotsRepo)
    ticketService = TicketService(gateRepo, vehicleRepo, slotsRepo, parkingRepo, ticketRepo)
    ticketController = IssueTicket(
        ticketService)

    request = TicketIssueRequest("123", "John Doe", VehicleType.CAR, 1)
    request2 = TicketIssueRequest("234", "John Doe 2", VehicleType.CAR, 1)
    response: TicketResponseDto = ticketController.issue_ticket(request)
    response2: TicketResponseDto = ticketController.issue_ticket(request2)
    print(response)



