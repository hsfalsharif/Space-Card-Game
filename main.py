import deck
import card
import random
# from global_params import *
import effect_funcs
import player

player_1 = player.Player() # player
effect_functions = effect_funcs.Effect_Function(player_1.fuel, player_1.mass) # instance of Effect_Function

effect_functions.igniter

def empty_func():
    pass

def update_number_of_cards(card, player, effect_functions_1): # player
    if card == 'igniter':
        new_number_of_igniter_card = player.get_number_of_igniter_card() + 1
        player.set_number_of_igniter_card(new_number_of_igniter_card)
        effect_functions_1.igniter()
    elif card == 'rocket_booster':
        new_number_of_rocket_booster_card = player.get_number_of_rocket_booster_card() + 1
        player.set_number_of_rocket_booster_card(new_number_of_rocket_booster_card)
        effect_functions_1.solid_rocket_booster()
    elif card == 'landing_gear':
        new_number_of_landing_gear_card = player.get_number_of_landing_gear_card() + 1
        player.set_number_of_landing_gear_card(new_number_of_landing_gear_card)
        effect_functions_1.landing_gear()
    # elif card == 'rcs_thrusters':
    #     new_number_of_rcs_thrusters_card = player.get_number_of_rcs_thrusters_card() + 1
    #     player.set_number_of_rcs_thrusters_card(new_number_of_rcs_thrusters_card)
    #     effect_functions_1.rcs_thrusters()
    # elif card == 'thruster_gimbel':
    #     new_number_of_thruster_gimbel_card = player.get_number_of_thruster_gimbel_card() + 1
    #     player.set_number_of_thruster_gimbel_card(new_number_of_thruster_gimbel_card)
    #     effect_functions_1.thruster_gimbel()
    elif card == 'electric_propulsion':
        new_number_of_electric_propulsion_card = player.get_number_of_electric_propulsion_card() + 1
        player.set_number_of_electric_propulsion_card(new_number_of_electric_propulsion_card)
        effect_functions_1.electric_propulsion()
    elif card == 'decoupler':
        new_number_of_decoupler_card = player.get_number_of_decoupler_card() + 1
        player.set_number_of_decoupler_card(new_number_of_decoupler_card)
        effect_functions_1.decoupler()
    elif card == 'accelerometer':
        new_number_of_accelerometer_card = player.get_number_of_accelerometer_card() + 1
        player.set_number_of_accelerometer_card(new_number_of_accelerometer_card)
        effect_functions_1.accelerometer()
    elif card == 'ring_laser_gyroscope':
        new_number_of_ring_laser_gyroscope_card = player.get_number_of_ring_laser_gyroscope_card() + 1
        player.set_number_of_ring_laser_gyroscope_card(new_number_of_ring_laser_gyroscope_card)
        effect_functions_1.ring_laser_gyroscope()
    elif card == 'fuel_tank':
        new_number_of_fuel_tank_card = player.get_number_of_fuel_tank_card() + 1
        player.set_number_of_fuel_tank_card(new_number_of_fuel_tank_card)
        effect_functions_1.fuel_tank()
    elif card == 'airbags':
        new_number_of_airbags_card = player.get_number_of_airbags_card() + 1
        player.set_number_of_airbags_card(new_number_of_airbags_card)
        effect_functions_1.airbags()
        # HERE
    elif card == 'thruster':
        new_number_of_thruster_card = player.get_number_of_thruster_card() + 1
        player.set_number_of_thruster_card(new_number_of_thruster_card)
        effect_functions_1.thruster()
    elif card == 'star_tracker':
        new_number_of_star_tracker_card = player.get_number_of_star_tracker_card() + 1
        player.set_number_of_star_tracker_card(new_number_of_star_tracker_card)
        effect_functions_1.star_tracker()
    


igniter_card = card.Card('igniter', empty_func())
solid_rocket_booster_card = card.Card('rocket_booster', empty_func())
landing_gear_card = card.Card('landing_gear', empty_func())
rcs_thrusters = card.Card('rcs_thrusters', empty_func())
thruster_gimbel_card = card.Card('thruster_gimbel', empty_func())
electric_propulsion_card = card.Card('electric_propulsion', empty_func())
decoupler_card = card.Card('decoupler', empty_func())
accelerometer_card = card.Card('accelerometer', empty_func())
ring_laser_gyroscope_card = card.Card('ring_laser_gyroscope', empty_func())
fuel_tank_card = card.Card('fuel_tank', empty_func())
airbags_card = card.Card('airbags', empty_func())
thruster_card = card.Card('thruster', empty_func())
star_tracker = card.Card('star_tracker', empty_func())


list_of_cards = [
    igniter_card,
    solid_rocket_booster_card,
    landing_gear_card,
    rcs_thrusters,
    thruster_gimbel_card,
    electric_propulsion_card,
]

new_object = random.choice(list_of_cards)
print(new_object.name)

print(player_1.get_number_of_igniter_card())
print(player_1.get_number_of_accelerometer_card())
print(player_1.get_number_of_airbags_card())
print(player_1.get_number_of_decoupler_card())
print(player_1.get_number_of_electric_propulsion_card())
print(player_1.get_number_of_fire_engine_card())
print(player_1.get_number_of_fuel_tank_card())
print(player_1.get_number_of_landing_gear_card())
print(player_1.get_number_of_RCS_thrusters_card())
print(player_1.get_number_of_ring_laser_gyroscope_card())
print(player_1.get_number_of_rocket_booster_card())
print(player_1.get_number_of_star_tracker_card())

print('Begin Looping')
while player_1.mass < 20:
    print('mass is' + str(player_1.mass))
    new_object = random.choice(list_of_cards)
    update_number_of_cards(new_object.name, player_1, effect_functions)

print('End Looping')
print(player_1.get_number_of_igniter_card())
print(player_1.get_number_of_accelerometer_card())
print(player_1.get_number_of_airbags_card())
print(player_1.get_number_of_decoupler_card())
print(player_1.get_number_of_electric_propulsion_card())
print(player_1.get_number_of_fire_engine_card())
print(player_1.get_number_of_fuel_tank_card())
print(player_1.get_number_of_landing_gear_card())
print(player_1.get_number_of_RCS_thrusters_card())
print(player_1.get_number_of_ring_laser_gyroscope_card())
print(player_1.get_number_of_rocket_booster_card())
print(player_1.get_number_of_star_tracker_card())