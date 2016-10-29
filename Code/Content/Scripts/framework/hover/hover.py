from configs.config_hover import MAX_AXIS_VELOCITY


def get_axis_torque(axis_rotation: float, axis_angular_velocity: float) -> float:
        pass


def get_desired_axis_velocity(axis_rotation: float) -> float:
    if axis_rotation == 0:
        return 0
    elif axis_rotation > 0:
        return MAX_AXIS_VELOCITY
    else:
        return -MAX_AXIS_VELOCITY
