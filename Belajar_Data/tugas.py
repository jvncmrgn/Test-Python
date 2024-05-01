import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input variables
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')

# Output variable
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Membership functions for service
service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['average'] = fuzz.trimf(service.universe, [0, 5, 10])
service['excellent'] = fuzz.trimf(service.universe, [5, 10, 10])

# Membership functions for food
food['poor'] = fuzz.trimf(food.universe, [0, 0, 5])
food['average'] = fuzz.trimf(food.universe, [0, 5, 10])
food['excellent'] = fuzz.trimf(food.universe, [5, 10, 10])

# Membership functions for tip
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Rule base
rule1 = ctrl.Rule(service['poor'] | food['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'] & food['average'], tip['medium'])
rule3 = ctrl.Rule(service['excellent'] | food['excellent'], tip['high'])

# Control System
tip_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tip_calculator = ctrl.ControlSystemSimulation(tip_ctrl)

# Input values
# Change these values according to the last two digits of your NIM
service_value = 6
food_value = 7

# Compute tip
tip_calculator.input['service'] = service_value
tip_calculator.input['food'] = food_value
tip_calculator.compute()

# Output tip
print("Estimated tip:", tip_calculator.output['tip'])
tip.view(sim=tip_calculator)
