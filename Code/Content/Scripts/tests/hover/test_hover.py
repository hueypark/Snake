from configs.config_hover import DAMP_START_ANGLE, MAX_AXIS_VELOCITY
from framework.hover import get_desired_axis_velocity


class TestHover:
    def test_get_desired_axis_velocity(self):
        assert 0 == get_desired_axis_velocity(0)

        assert MAX_AXIS_VELOCITY == get_desired_axis_velocity(DAMP_START_ANGLE)
        assert -MAX_AXIS_VELOCITY == get_desired_axis_velocity(-DAMP_START_ANGLE)
