class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places
        
    def __repr__(self):
        return "%.{}f".format(self.places) % self.number
    
    
class Currency(Decimal):
    pass

print(Currency(15.6789, 3))