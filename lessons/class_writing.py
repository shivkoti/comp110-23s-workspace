"""Write a Plane Ticket Class."""

class PlaneTicket:
    departure_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float):
        self.departure_city = city_a
        self.arrival_city = city_b
        self.departure_time = depart
        self.ticket_cost = cost

    def __str__(self) -> str:
        ticket_str: str = f"Flight from {self.departure_city} at {self.departure_time}"
        ticket_str += f"Arrive in {self.arrival_city}. Costs ${self.ticket_cost}"