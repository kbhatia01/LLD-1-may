
class TicketRepo:
    def __init__(self):
        self.tickets = {}

    def save_ticket(self, ticket):
        if ticket.id in self.tickets:
            raise KeyError(f"Ticket with ID {ticket.id} already exists.")
        self.tickets[ticket.id] = ticket