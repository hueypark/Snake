from framework.math import lerp


class TestMath:
    def test_lerp(self):
        assert 0 == lerp(0, 1, 0)
        assert 1 == lerp(0, 1, 1)
        assert 0.5 == lerp(0, 1, 0.5)
        assert 1.5 == lerp(0, 3, 0.5)
