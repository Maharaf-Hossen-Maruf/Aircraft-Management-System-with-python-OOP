class Airport:
    def __init__(self,code,name,city,country,lat,long,rate):
        self.name = name
        self.code = code
        self.city = city
        self.country = country
        self.lat = float(lat)
        self.lon = float(long)
        self.rate = float(rate)
    
    def __repr__(self):
        return f'Airport: {self.name} in: {self.country} lat: {self.lat} long: {self.lon} rate: {self.rate}'


