# Calculation of Circle - Area and Perimeter:

class Circle:

# Class variable for pi:
    
    pi = 3.141 

    def __init__(self , radius_list):
        self.radius_list = radius_list

    @classmethod

    def calculate_area(cls, radius ):
        area = cls.pi * ( radius ** 2)
        return area

    @classmethod

    def calculate_perimeter (cls, radius):
        perimeter = 2 * cls.pi * radius
        return perimeter
        
radius_list = [10,501,22,37,100,999,87, 351]

for radius in radius_list:
    area = Circle.calculate_area (radius)
    perimeter = Circle.calculate_perimeter(radius)

    print (f"Radius : {radius}, Area: {area}, Perimeter: {perimeter}")


# Inheritance:
    
class TV:

    def __init__ (self, brand, channel, price, inches, onoff_status, volume):
        self.brand = brand
        self.channel = 1
        self.price = price
        self.inches = inches
        self.on_off_status = onoff_status
        self.volume = 50

    def increase_volume (self):
        self.volume = min(self.volume + 1, 100)

    def decrease_volume (self):
        self.volume = max (self.volume - 1, 0)

    def reset_tv (self):
        self.volume = 50
        self.channel = 1
    
    def status(self):
        return (f" The {self.brand} TV is in channel: {self.channel} and Volume : {self.volume}")

class LED_TV(TV):
    def __init__(self, screen_thickness, energy_usage , Lifespan , Refresh_rate , viewingAngle , Backlight, DisplayDetails):
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.Lifespan = Lifespan
        self.Refresh_rate = Refresh_rate
        self.viewingAngle = viewingAngle
        self.Backlight = Backlight

    def display_details(self):
        return f"(Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}"


class Plasma_TV(TV):
    
    def __init__(self, screen_thickness, energy_usage , Lifespan , Refresh_rate , viewingAngle , Backlight, DisplayDetails):
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.Lifespan = Lifespan
        self.Refresh_rate = Refresh_rate
        self.viewingAngle = viewingAngle
        self.Backlight = Backlight
       

    def display_details(self):
        return f" Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}"
    



