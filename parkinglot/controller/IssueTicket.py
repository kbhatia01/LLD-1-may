from parkinglot.dtos.TicketIssueRequest import TicketIssueRequest
from parkinglot.dtos.TicketResponseDto import TicketResponseDto
from parkinglot.service.TicketService import TicketService


class IssueTicket:
    def __init__(self, parking_service:TicketService):
        self.parking_service = parking_service


    def issue_ticket(self, ticketIssueRequest: TicketIssueRequest):
        try:
            ticket = self.parking_service.issue_ticket(ticketIssueRequest)
            ticketResponseDto = TicketResponseDto()
            ticketResponseDto.ticketNumber = ticket.id
            ticketResponseDto.vehicleNumber = ticket.vehicle.id
            ticketResponseDto.entryTime = ticket.entry_time
            ticketResponseDto.slotNumber = ticket.parking_slot.slot_number
            ticketResponseDto.floor = ticket.parking_slot.parking_floor.floor_number

            return ticketResponseDto
        except ValueError as e:
            print("Error issuing ticket:", e)