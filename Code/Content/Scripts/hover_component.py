import unreal_engine as ue
from framework import hover
from unreal_engine import FVector

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
            hover.get_axis_torque(angular_velocity.x, rotation.roll),
            hover.get_axis_torque(angular_velocity.y, rotation.pitch),
            0)
        self.static_mesh_component.add_torque(torque, 'None', True)
