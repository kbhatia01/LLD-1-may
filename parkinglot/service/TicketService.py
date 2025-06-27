import datetime

from parkinglot.Repo import ParkingLotRepo
from parkinglot.Repo.GateRepo import GateRepo
from parkinglot.Repo.Slots import slotRepo
from parkinglot.Repo.ticketRepo import TicketRepo
from parkinglot.Repo.vehicleRepo import VehicleRepo
from parkinglot.dtos.TicketIssueRequest import TicketIssueRequest
from parkinglot.models.models import Ticket, Vehicle, SlotStatus
from parkinglot.service.slot_strgy.SlotFactory import SlotFactory


class TicketService:

    def __init__(self, gateRepo: GateRepo, vehicleRepo: VehicleRepo,
                 slot_repo: slotRepo, parkingLotRepo: ParkingLotRepo,
                 ticketRepo: TicketRepo):
        self.vehicleRepo = vehicleRepo
        self.gate_repo = gateRepo
        self.slot_repo = slot_repo
        self.parkingLotRepo = parkingLotRepo
        self.ticketRepo = ticketRepo


    def issue_ticket(self, ticketIssueRequest: TicketIssueRequest):
        # create a empty ticket
        ticket = Ticket(-1, ticketIssueRequest.vehicleNumber,
                        entry_time=datetime.datetime.now(), vehicle=None,
                        parking_slot=None, generated_gate=None)

        # gate info
        gate = self.gate_repo.get_gate_by_id(ticketIssueRequest.gateId)
        if not gate:
            raise ValueError("Invalid gate ID")

        ticket.generated_gate = gate
        # add vehicle info
        vehicle = self.vehicleRepo.find_vehicle_by_number(ticketIssueRequest.vehicleNumber)
        if not vehicle:
            vehicle = Vehicle(ticketIssueRequest.vehicleNumber, ticketIssueRequest.ownerName, ticketIssueRequest.vehicleType)
            self.vehicleRepo.save(vehicle)

        ticket.vehicle = vehicle
        #  find a slot
        strgy = SlotFactory.get_slot_strgy_obj(gate.parking_lot.slot_assignment_strategy)

        slot = strgy.get_slots(ticketIssueRequest.vehicleType, gate.parking_lot)

        if slot is None:
            raise ValueError("No slot available for the vehicle type")
        #  assign a slot
        ticket.parking_slot = slot
        slot.parking_slot_status =SlotStatus.FILLED
        # block slot
        self.slot_repo.update_slot(slot.id, slot)
        # update the total capacity of the parking lot
        self.parkingLotRepo.decrease_parking_lot_capacity(parkingLot=gate.parking_lot)
        # return the ticket
        self.ticketRepo.save_ticket(ticket)
        return ticket

    # add a method to check availability of slots