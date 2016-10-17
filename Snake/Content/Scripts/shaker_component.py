import unreal_engine as ue
from random import uniform
from unreal_engine import FVector

SHAKE_COOLDOWN = 10


class ShakerComponent:
    def __init__(self):
        self.static_mesh_component = None
        self.shake_cooldown = 0

    def begin_play(self):
        self.static_mesh_component = self.uobject.get_actor_component_by_type(ue.find_class('StaticMeshComponent'))
        self.shake_cooldown = SHAKE_COOLDOWN

    def tick(self, delta_time: float):
        if self.shake_cooldown < 0:
            self.shake_cooldown = SHAKE_COOLDOWN
            self.__shake()
        else:
            self.shake_cooldown -= delta_time

    def __shake(self):
        self.static_mesh_component.add_torque(
            FVector(self.__get_random_axis_torque(), self.__get_random_axis_torque(), 0),
            'None',
            True)

        ue.print_string('Shake')

    @staticmethod
    def __get_random_axis_torque():
        return uniform(-200, 200)
