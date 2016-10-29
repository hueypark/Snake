from configs.config_hover import DAMP_START_ANGLE, HOVER_TORQUE, MAX_AXIS_VELOCITY
from framework.math import lerp


def get_axis_torque(axis_rotation: float, axis_angular_velocity: float) -> float:
    desired_velocity = get_desired_axis_velocity(axis_rotation)
    if axis_angular_velocity == desired_velocity:
        return 0
    elif axis_angular_velocity < desired_velocity:
        return -HOVER_TORQUE
    else:
        return HOVER_TORQUE


def get_desired_axis_velocity(axis_rotation: float) -> float:
    if axis_rotation == 0:
        return 0

    abs_axis_ratation = abs(axis_rotation)
    if abs_axis_ratation < DAMP_START_ANGLE:
        desired_velocity = lerp(0, MAX_AXIS_VELOCITY, abs_axis_ratation / DAMP_START_ANGLE)
        if axis_rotation < 0:
            return -desired_velocity
        else:
            return desired_velocity
    else:
        if axis_rotation < 0:
            return -MAX_AXIS_VELOCITY
        else:
            return MAX_AXIS_VELOCITY
