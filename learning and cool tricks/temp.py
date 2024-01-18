class Temperature:
    def __init__(self,celsius):
        self._celsius = celsius
        
    @property
    def celsius(self):          #getter method
        return self._celsius
    
    @celsius.setter
    def celsius(self,value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    

# Usage
temp = Temperature(100)
temp.celsius = -300