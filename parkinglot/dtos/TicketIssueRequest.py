from parkinglot.models.models import BaseModel


class TicketIssueRequest:
    def __init__(self, vehicleNumber, ownerName, vehicleType, gateId):
        self.vehicleNumber = vehicleNumber
        self.ownerName = ownerName
        self.vehicleType = vehicleType
        self.gateId = gateId
