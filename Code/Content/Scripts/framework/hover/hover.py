from configs import config_hover


class Hover:
    @staticmethod
    def get_axis_torque(axis_rotation: float, axis_angular_velocity: float) -> float:
        pass

    @staticmethod
    def get_desired_axis_velocity(axis_rotation: float) -> float:
        return config_hover.MAX_AXIS_VELOCITY
