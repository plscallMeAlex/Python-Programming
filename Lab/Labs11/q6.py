from abc import *
class Transportation(ABC):
    def __init__(self, start_place, end_place, distance):
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance
    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)
    def find_cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)
    def find_cost(self):
        cost = self.distance*40
        return cost

class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station):
        super().__init__(start_place, end_place, distance) 
        self.station = station
    def find_cost(self):
        cost = self.station*5
        return cost

l1 = Walk("KMITL", "Lawson", 0.6)
l2 = Taxi("Lawson", "Station", 5)
l3 = Train("Ladk", "Paya", 40, 6)
l4 = Taxi("Pay", "COun", 3)

re = [l1, l2, l3, l4]
for i in re:
    cost = i.find_cost()
    start = i.start_place
    endss = i.end_place
    print(f"from {start} to {endss} cost " + str(cost) + " Baht")