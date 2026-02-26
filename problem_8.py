
#variant 8 Server
class ServerRack:
    def __init__(self , name , total_slots , used_slots = 0) :
        self._name = name
        self.total_slots = total_slots
        self.used_slots = used_slots

    @property
    def name(self):
        return self._name
    
    @property
    def total_slots(self):
        return self._total_slots
    
    @total_slots.setter

    def total_slots(self,amount):
        if amount < 1 :
            raise ValueError("Total slots must be at least 1")
        self._total_slots = amount

    @property
    def used_slots(self):
        return self._used_slots
    
    @used_slots.setter

    def used_slots(self , amount):
        if amount < 0 :
            raise ValueError("Used slots cannot be negative")
        
        if amount > self.total_slots :
            raise ValueError("Used slots cannot exceed total slots")
        self._used_slots = amount

    @property
    def free_slots(self):
        return self.total_slots - self.used_slots
    
    @property
    def usage_rate(self):
        return round(self.used_slots / self.total_slots * 100 , 1)
    
    def install(self , servers):
        if servers <= 0 :
            raise ValueError("Number of servers must be positive")
        if servers > self.free_slots :
            raise ValueError("Not enough free slots")
        
        self.used_slots += servers

    def remove(self,servers):
        if servers <= 0 :
            raise ValueError("Number of servers must be positive")
        if servers > self.used_slots :
            raise ValueError("Cannot remove more than installed")
        self.used_slots -= servers

r = ServerRack("Rack-A1", 42)
print(r.name , r.free_slots , r.usage_rate)

r.install(30)
print(r.used_slots , r.usage_rate)

r.remove(6)
print(r.free_slots)

try :
    r.install(20)
except ValueError as e :
    print(e)

try :
    r.name = "X"
except AttributeError:
    print("Cannot change rack name")