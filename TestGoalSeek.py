from GoalSeekAlgo import GoalSeek
from constants import AppConstants
import math

class VehicleRequest:
    gross_vehicle_weight = 0
    wheel_radius = 0
    gear_ratio = 0
    gear_efficiency = 0
    gear_efficiency = gear_efficiency / 100
    rolling_resistance_coefficient = 0

    slope_in_deg = 0
    drag_coefficient = 0
    frontal_area = 0
    request_time_instant = 0

    def to_string(self):
        return "gross_vehicle_weight: " + str(self.gross_vehicle_weight) + "\nwheel_radius: " + str(self.wheel_radius) + "\ngear_ratio: " + str(self.gear_ratio) + "\ngear_efficiency: " + str(self.gear_efficiency) + "\nrolling_resistance_coefficient: " + str(self.rolling_resistance_coefficient) + "\nslope_in_deg: " + str(self.slope_in_deg) + "\ndrag_coefficient: " + str(self.drag_coefficient) + "\nfrontal_area: " + str(self.frontal_area) + "\nrequest_time_instant: " + str(self.request_time_instant)

def motor_torque_function(x, vehicle_req):
    slope_in_rad = vehicle_req.slope_in_deg * AppConstants.PI_VALUE / 180

    val_a = AppConstants.AIR_DENSITY * vehicle_req.drag_coefficient * vehicle_req.frontal_area / (
            2 * vehicle_req.gross_vehicle_weight)

    c1 = (vehicle_req.gear_ratio * vehicle_req.gear_efficiency) / (
            vehicle_req.gross_vehicle_weight * vehicle_req.wheel_radius)

    c2 = AppConstants.ACCELERATION_DUE_TO_GRAVITY * (
            (vehicle_req.rolling_resistance_coefficient * math.cos(slope_in_rad)) + math.sin(slope_in_rad))

    try:
        motor_torque = (
                (math.log(
                    math.exp(2 * math.sqrt(val_a * ((c1 * x) - c2)) * vehicle_req.request_time_instant) + 1) / val_a)
                - (math.sqrt(((c1 * x) - c2) / val_a) * vehicle_req.request_time_instant)
                - (math.log(2) / val_a)
        )
    except ValueError:
        motor_torque = 0
    return motor_torque


vehicle_request = VehicleRequest()
vehicle_request.gross_vehicle_weight = 800
vehicle_request.wheel_radius = 0.23
vehicle_request.gear_ratio = 10
vehicle_request.gear_efficiency_percentage = 90
vehicle_request.rolling_resistance_coefficient = 0.005
vehicle_request.drag_coefficient = 0.15
vehicle_request.frontal_area = 2.3
vehicle_request.slope_in_deg = 5.00
vehicle_request.request_time_instant = 10

res = GoalSeek(motor_torque_function, 17, 0, vehicle_request)
print('jghj',res)

