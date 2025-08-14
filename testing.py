class Time:
    def __init__(self,Hours=0,minutes=0,seconds=0):
        self._Hours=Hours
        self._minutes=minutes
        self._seconds=seconds

    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_Hours(self):
        return self.Hours
    
    def get_Minutes(self):
        return self.minutes
    
    def get_Seconds(self):
        return self.seconds
    
    def to_Seconds(self)->int:
        return f"{self._Hours*3600 + self._minutes*60 + self._seconds} sec"
    
    def print_toseconds(self):
        return f"{self.get_Hours()}hrs.{self.get_Minutes()}mins.{self.get_Seconds()}sec.equals {self.to_Seconds()}sec"    
    
    def getDifference(self,t) ->int:
        return self.toSeconds() - t.toSeconds()

    def __str__(self):
        return f" »{self._Hours}h {self._minutes}' {self._seconds}\"«"

t1=Time(24,1,1)
print(t1)      


#new update
#new