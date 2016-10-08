from config import SNAKE_MOVE_SPEED, SNAKE_TURN_RATE
from snake_body import SnakeBody

BODY_SPAWN_PERIOD = 2


class SnakeHead:
    def __init__(self):
        self.body_spawn_remain_time = BODY_SPAWN_PERIOD

    def begin_play(self):
        self.body_spawn_remain_time = BODY_SPAWN_PERIOD
        self.uobject.bind_axis('TurnRate', self.__turn)

    def tick(self, delta_time):
        self.__move_forward(delta_time)
        self.body_spawn_remain_time -= delta_time
        if self.body_spawn_remain_time < 0:
            self.body_spawn_remain_time += BODY_SPAWN_PERIOD
            snake_body = self.__spawn_body()
            snake_body.set_prev_snake(self)

    def __move_forward(self, delta_time):
        location = self.uobject.get_actor_location()
        location += self.uobject.get_actor_forward() * SNAKE_MOVE_SPEED * delta_time
        self.uobject.set_actor_location(location)

    def __turn(self, axis_value):
        turn_rate = axis_value * self.uobject.get_world_delta_seconds() * SNAKE_TURN_RATE

        rotation = self.uobject.get_actor_rotation()
        rotation.yaw += turn_rate
        self.uobject.set_actor_rotation(rotation)

    def __spawn_body(self) -> SnakeBody:
        snake_body_uobject = self.uobject.call_function('SpawnSnakeBody')[0]
        return snake_body_uobject.get_py_proxy()
