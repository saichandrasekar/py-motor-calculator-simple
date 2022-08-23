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
