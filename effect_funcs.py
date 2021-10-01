class Effect_Function:

    def __init__(self, current_fuel, current_mass):
        self.current_fuel = current_fuel
        self.current_mass = current_mass

    def igniter(self):
        self.current_fuel -= 4
        self.current_mass -= 3

    def thruster(self):
        self.current_fuel -= 3
        self.current_mass -= 3

    def solid_rocket_booster(self):
        self.current_fuel -= 1
        self.current_mass -= 3

    def landing_gear(self):
        self.current_fuel -= 0
        self.current_mass -= 2

    def rcs_thrusters(self):
        self.current_fuel -= 2
        self.current_mass -= 1

    def thruster_gimbel(self):
        self.current_fuel -= 4
        self.current_mass -= 3

    def electric_propulsion(self):
        self.current_fuel -= 0
        self.current_mass -= 6

    def decoupler(self):
        self.current_fuel -= 2
        self.current_mass -= 2

    def accelerometer(self):
        self.current_fuel -= 0
        self.current_mass -= 2


    def ring_laser_gyroscope(self):
        self.current_fuel -= 1
        self.current_mass -= 2

    def star_tracker(self):
        self.current_fuel -= 1
        self.current_mass -= 4
    
    def fuel_tank(self):
        self.current_fuel -= 0
        self.current_mass -= 3