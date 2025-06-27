from parkinglot.dtos.TicketIssueRequest import TicketIssueRequest


class IssueTicket:
    def __init__(self, parking_service):
        self.parking_service = parking_service


    def issue_ticket(self, ticketIssueRequest: TicketIssueRequest):
        pass

