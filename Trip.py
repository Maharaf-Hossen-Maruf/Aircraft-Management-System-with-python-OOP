class  Trip:
    def __init__(self,trip_cities,aircraft,price,start_date,route=''):
        self.trip_cities = trip_cities
        self.start_date = start_date
        self.aircraft = aircraft
        self.trip_routes=route
        self.price = price

    def __repr__(self) -> str:
        # return f'Trip {self.trip_cities} Aircraft: {self.aircraft} route : {self.trip_routes} Cost: {self.cost} '
        return f'Trip {self.trip_cities}   Cost: {self.price} '
        