import numpy as np
import math
from scipy.optimize import minimize
from scipy.optimize import root
from constants import AppConstants

from GoalSeekAlgo import GoalSeek

def b_function(x):
    gross_vehicle_weight = 800
    wheel_radius = 0.23
    gear_ratio = 10
    gear_efficiency = 95 / 100

    c1 = (gear_ratio * gear_efficiency) / (gross_vehicle_weight * wheel_radius)

    rolling_resistance_coefficient = 0.005

    slope_in_deg = 5.00
    slope_in_rad = slope_in_deg * AppConstants.PI_VALUE / 180
    # print(slope_in_rad)
    # print(rolling_resistance_coefficient * math.cos(slope_in_rad))

    c2 = AppConstants.ACCELERATION_DUE_TO_GRAVITY * (
            (rolling_resistance_coefficient * math.cos(slope_in_rad)) + math.sin(slope_in_rad))
    return c1*x - c2


#x0 = np.array([1.07])
#res = minimize(b_function, x0, method='nelder-mead')#, options={'xatol': 1e-8, 'disp': True})
#print(res.x)
#print(res.x)

res = root(b_function, 0)
print(res.x)
res = GoalSeek(b_function, 0.0001, res.x[0])
print(res)
#print(b_function(35))