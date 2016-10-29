import unreal_engine as ue
from framework.hover import get_desired_axis_velocity
from unreal_engine import FVector
from unreal_engine.classes import KismetMathLibrary

DAMP_START_ANGLE = 60
MAX_AXIS_VELOCITY = 100


class HoverComponent:
    def __init__(self):
        self.static_mesh_component = None

    def begin_play(self):
        self.static_mesh_component = self.uobject.get_actor_component_by_type(ue.find_class('StaticMeshComponent'))

    def tick(self, delta_time: float):
        angular_velocity = self.static_mesh_component.get_physics_angular_velocity()
        rotation = self.static_mesh_component.get_world_rotation()
        torque = FVector(
            self.__get_axis_torque(angular_velocity.x, rotation.roll),
            self.__get_axis_torque(angular_velocity.y, rotation.pitch),
            0)
        self.static_mesh_component.add_torque(torque, 'None', True)

    def __get_axis_torque(self, axis_rotation: float, axis_angular_velocity: float) -> float:
        desired_velocity = get_desired_axis_velocity(axis_rotation)
        if axis_angular_velocity < desired_velocity:
            return -1
        else:
            return 1
