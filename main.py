import math
from constants import AppConstants


class Result:
    time = 0
    speed = 0
    power = 0
    distance = 0

    def __init__(self, time):
        self.time = time
        self.speed = 0
        self.power = 0
        self.distance = 0

    def set_speed(self, val_A, val_B):
        self.speed = math.sqrt(val_B / val_A) * (1 - 2 / (math.exp(2 * math.sqrt(val_A * val_B) * self.time) + 1))
        # print(self.speed)

    def get_speed_kmph(self):
        return self.speed * 3.6

    def get_speed_rpm(self, wheel_radius, gear_ratio):
        return self.speed / (2 * AppConstants.PI_VALUE * wheel_radius) * gear_ratio * 60

    def get_power(self, motor_torque, wheel_radius, gear_ratio):
        return motor_torque * self.get_speed_rpm(wheel_radius, gear_ratio) / 9.55 / 1000

    def get_distance(self, val_A, val_B):
        return (math.log(math.exp(2 * math.sqrt(val_A * val_B) * self.time) + 1) / val_A - math.sqrt(
            val_B / val_A) * self.time - math.log(2) / val_A) / 1000


def find_motor_peak_motor_torque():
    print('Computation Starting')

    # Vehicle Parameters
    gross_vehile_weight = 700  # D4
    gear_ratio = 10  # D5
    wheel_radius = 0.23  # D6
    frontal_areas = 2.3  # D7
    drag_coefficient = 0.15  # D8
    rolling_resistance_coefficient = 0.005  # D9
    gear_efficiency_percentage = 95  # D10

    # Performance Specs
    rated_speed = 45  # D13
    max_speed = 80  # D14
    gradeability = 12.25  # D15
    cross_grade_time = 10  # D16
    grade_length = 17  # D17
    acceleration_from_rest_to_req_speed = 30  # D18
    time_to_accelerate = 9  # D19

    # Run condition parameters
    slope = 5  # G9

    request_time_instant = 10

    # Output spec
    motor_torque = 23  # G10

    # calculate slope in gradient, rad and percentage
    slope_in_rad = (slope / 180) * AppConstants.PI_VALUE  # G12
    print('Slope in rad: ', slope_in_rad)
    slope_in_gradient = math.tan(slope_in_rad)
    slope_in_gradient_percentage = slope_in_gradient * 100  # G8 TODO: Apply TAN

    # calculate ARMS
    arms = motor_torque / AppConstants.H10_VAL

    # calculate Wheel Torque in Nm
    wheel_torque = motor_torque * gear_ratio * gear_efficiency_percentage / 100  # G13
    print('Wheel Torque: ', wheel_torque)
    val_A = (AppConstants.AIR_DENSITY * drag_coefficient * frontal_areas) / (2 * gross_vehile_weight)  # G14
    print('val_A: ', val_A)
    val_B = (wheel_torque / (gross_vehile_weight * wheel_radius)) - AppConstants.ACCELERATION_DUE_TO_GRAVITY * ((
                (rolling_resistance_coefficient * math.cos(slope_in_rad)) + math.sin(
            slope_in_rad)))  # G15 TODO: Check computation order
    print('val_B: ', val_B)

    # while True:
    #     result = Result(request_time_instant)
    #     result.set_speed(val_A, val_B)
    #     distance = math.floor(result.get_distance(val_A, val_B) * 1000)
    #
    #     if(distance > AppConstants.ARAI_TEST_DISTANCE):
    #         #print('redu')
    #         motor_torque=-1
    #         continue
    #     elif(distance < AppConstants.ARAI_TEST_DISTANCE):
    #         motor_torque=+1
    #         continue
    #     else:
    #         break

    print('\nCalculated Motor Torque: ', motor_torque)
    print('Computation Finished')

    print('Result Summary:')
    print('===============\n')

    result_summary = []
    time_intervals = [0, 1, 2, 3, 5, 10, 8, 55, 145, 1000, 2000]
    for time in time_intervals:
        # print(time)
        result = Result(time)
        result.set_speed(val_A, val_B)
        result_summary.append(result)

        print('Time: ', result.time)
        print('Speed in m/s: ', result.speed)
        print('Speed in kmph: ', result.get_speed_kmph())
        print('Speed in motor rpm: ', result.get_speed_rpm(wheel_radius, gear_ratio))
        print('Power in KW: ', result.get_power(motor_torque, wheel_radius, gear_ratio))
        print('Distance in Km: ', result.get_distance(val_A, val_B))
        print('---')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_motor_peak_motor_torque()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
