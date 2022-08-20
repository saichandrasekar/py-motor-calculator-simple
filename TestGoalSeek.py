from GoalSeekAlgo import GoalSeek
from constants import AppConstants
import math

def b_function(x):
    gross_vehicle_weight = 800
    wheel_radius = 0.23
    gear_ratio = 10
    gear_efficiency = 95 / 100

    c1 = (gear_ratio * gear_efficiency) / (gross_vehicle_weight * wheel_radius)

    rolling_resistance_coefficient = 0.005

    slope_in_deg = 4.00
    slope_in_rad = slope_in_deg * AppConstants.PI_VALUE / 180
    # print(slope_in_rad)
    # print(rolling_resistance_coefficient * math.cos(slope_in_rad))

    c2 = AppConstants.ACCELERATION_DUE_TO_GRAVITY * (
            (rolling_resistance_coefficient * math.cos(slope_in_rad)) + math.sin(slope_in_rad))
    return c1*x - c2

# Get the motor torque for the expected B
#res = GoalSeek(b_function, 1.07, 30)
#print(math.ceil(res))

def motor_torque_function(x):
    gross_vehicle_weight = 700
    wheel_radius = 0.23
    gear_ratio = 10
    gear_efficiency = 95 / 100

    rolling_resistance_coefficient = 0.005

    slope_in_deg = 4.00
    slope_in_rad = slope_in_deg * AppConstants.PI_VALUE / 180
    # print(slope_in_rad)
    # print(rolling_resistance_coefficient * math.cos(slope_in_rad))

    drag_coefficient = 0.15
    frontal_area = 2.3

    val_A = AppConstants.AIR_DENSITY * drag_coefficient * frontal_area / (2 * gross_vehicle_weight)

    c1 = (gear_ratio * gear_efficiency) / (gross_vehicle_weight * wheel_radius)

    c2 = AppConstants.ACCELERATION_DUE_TO_GRAVITY * (
            (rolling_resistance_coefficient * math.cos(slope_in_rad)) + math.sin(slope_in_rad))
    val_B = (c1 * x) - c2
    print(x)
    print(val_B)
    return (
            (math.log(math.exp(2 * math.sqrt(val_A * val_B) * 10) + 1) / val_A)
            - (math.sqrt(val_B / val_A) * 10)
            - (math.log(2) / val_A)
           )

res = GoalSeek(motor_torque_function, 17, 35)
print(res)