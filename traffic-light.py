# Set the operation mode of lights to - Manual or auto

# If manual
# Call Light methods - Red, Green, Amber

# If auto
# Set timer (like 30 seconds)
# Starts toggling lights

# If manual, operator (like a traffic cop) can set lights accordingly
# Note that the system should not allow 2 Greens at the same time

import time

class Traffic:
    operation: str 
    color: str

    def __init__(self, operation):  
        self.operation = operation


    def toggle_lights_auto(self):
        while True:
            time.sleep(30)
            self.red()
            self.green()
            self.amber()

    def red(self):
        self.show_light('red')
    
    def green(self):
        self.show_light('red')

    def amber(self):
        self.show_light('red')
        
    def show_light(self,color):
        time.sleep(1)
        pass
        

if __name__ == "__main__":
    pass