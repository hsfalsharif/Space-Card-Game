from _typeshed import Self
import player

player = player.Player()


class Effect_Function:


    def __init__(self, fuel, mass):
        self.fuel = player.get_fuel()
        self.mass = player.get_mass()
        

    @staticmethod
    def igniter(self):
        player.set_fuel(self.fuel - 4)
        player.set_mass(self.mass + 3)

    def thruster(self):
        player.set_fuel(self.fuel - 3)
        player.set_mass(self.mass + 3)

    def solid_rocket_booster(self):
        player.set_fuel(self.fuel - 1)
        player.set_mass(self.mass + 3)

    def landing_gear(self):
        player.set_fuel(self.fuel - 0)
        player.set_mass(self.mass + 2)

    def rcs_thrusters(self):
        player.set_fuel(self.fuel - 2)
        player.set_mass(self.mass + 1)

    def thruster_gimbel(self):
        player.set_fuel(self.fuel - 4)
        player.set_mass(self.mass + 3)

    def electric_propulsion(self):
        player.set_fuel(self.fuel - 0)
        player.set_mass(self.mass + 6)

    def decoupler(self):
        player.set_fuel(self.fuel - 2)
        player.set_mass(self.mass + 2)

    def accelerometer(self):
        player.set_fuel(self.fuel - 0)
        player.set_mass(self.mass + 2)


    def ring_laser_gyroscope(self):
        player.set_fuel(self.fuel - 1)
        player.set_mass(self.mass + 2)

    def star_tracker(self):
        player.set_fuel(self.fuel - 1)
        player.set_mass(self.mass + 4)
    
    def fuel_tank(self):
        player.set_fuel(self.fuel - 0)
        player.set_mass(self.mass + 3)