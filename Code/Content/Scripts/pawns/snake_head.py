import unreal_engine as ue
from config import SNAKE_ACCELERATION, SNAKE_MAX_SPEED
from framework import hover
from unreal_engine import FVector
from pawns.snake_body import SnakeBody

SQUARE_SNAKE_MAX_SPEED = SNAKE_MAX_SPEED * SNAKE_MAX_SPEED
SNAKE_TURN_RATE_HEAD = 360
BODY_SPAWN_PERIOD = 2


class SnakeHead:
    def __init__(self):
        self.static_mesh_component = None
        self.body_spawn_remain_time = BODY_SPAWN_PERIOD
        self.bodys = []

    def begin_play(self):
        self.static_mesh_component = self.uobject.get_actor_component_by_type(ue.find_class('StaticMeshComponent'))
        self.body_spawn_remain_time = BODY_SPAWN_PERIOD
        self.bodys = []

        self.uobject.bind_axis('TurnRate', self.__turn)

    def tick(self, delta_time):
        self.__hover()

        self.__move_forward()
        return

        self.body_spawn_remain_time -= delta_time
        if self.body_spawn_remain_time < 0:
            self.body_spawn_remain_time += BODY_SPAWN_PERIOD

            snake_body = self.__spawn_body()
            if not self.bodys:
                snake_body.set_prev_snake(self)
            else:
                snake_body.set_prev_snake(self.bodys[-1])

            self.bodys.append(snake_body)

    def __hover(self):
        angular_velocity = self.static_mesh_component.get_physics_angular_velocity()
        rotation = self.static_mesh_component.get_world_rotation()
        torque = FVector(
            hover.get_axis_torque(angular_velocity.x, rotation.roll),
            hover.get_axis_torque(angular_velocity.y, rotation.pitch),
            0)
        self.static_mesh_component.add_torque(torque, 'None', True)

    def __move_forward(self):
        velocity = self.static_mesh_component.get_physics_linear_velocity()
        forward = self.static_mesh_component.get_forward_vector()
        forward_velocity = velocity.project_on_to_normal(forward)
        if forward_velocity.length_squared() < SQUARE_SNAKE_MAX_SPEED:
            self.static_mesh_component.add_force(forward * SNAKE_ACCELERATION, 'None', True)

    def __turn(self, axis_value):
        angular_velocity = self.static_mesh_component.get_physics_angular_velocity()
        if axis_value < 0:
            if angular_velocity.z < -SNAKE_TURN_RATE_HEAD:
                return
        elif axis_value > 0:
            if angular_velocity.z > SNAKE_TURN_RATE_HEAD:
                return
        else:
            if angular_velocity.z > 0:
                self.static_mesh_component.add_torque(
                    FVector(
                        0,
                        0,
                        -10),
                    'None',
                    True)
            elif angular_velocity.z < 0:
                self.static_mesh_component.add_torque(
                    FVector(
                        0,
                        0,
                        10),
                    'None',
                    True)

        self.static_mesh_component.add_torque(
            FVector(
                0,
                0,
                axis_value * 10),
            'None',
            True)

    def __spawn_body(self) -> SnakeBody:
        location = None
        rotation = None
        if not self.bodys:
            uobject = self.uobject
            location = uobject.get_actor_location()
            rotation = uobject.get_actor_rotation()
        else:
            uobject = self.bodys[-1].uobject
            location = uobject.get_actor_location()
            rotation = uobject.get_actor_rotation()

        snake_body_uobject = self.uobject.call_function('SpawnSnakeBody', location, rotation)[0]
        return snake_body_uobject.get_py_proxy()
