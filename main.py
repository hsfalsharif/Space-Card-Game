import deck
import card
import random

number_of_igniter_card = 1
number_of_fire_engine_card = 3
number_of_rocket_booster = 0
number_of_landing_gear_card = 1
number_of_RCS_thrusters_card = 0
number_of_electric_propulsion_card = 0

current_fuel = 100
current_mass = 10

def empty_func():
    pass

igniter_card = card.Card('igniter', empty_func())
fire_engine_card = card.Card('fire_engine', empty_func())
solid_rocket_booster_card = card.Card('solid_rocket_booster', empty_func())
landing_gear_card = card.Card('landing_gear', empty_func())
rcs_thrusters = card.Card('rcs_thrusters', empty_func())
thruster_gimbel_card = card.Card('thruster_gimbel', empty_func())
electric_propulsion_card = card.Card('electric_propulsion', empty_func())


list_of_cards = [
    igniter_card,
    fire_engine_card,
    solid_rocket_booster_card,
    landing_gear_card,
    rcs_thrusters,
    thruster_gimbel_card,
    electric_propulsion_card,
]

new_object = random.choice(list_of_cards)
print(new_object.name)