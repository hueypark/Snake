from configs import config_hover
from framework.hover import Hover


class TestHover:
    def test_get_desired_axis_velocity(self):
        assert config_hover.MAX_AXIS_VELOCITY == Hover.get_desired_axis_velocity(config_hover.DAMP_START_ANGLE)
