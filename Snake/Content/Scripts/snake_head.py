from config import SNAKE_MOVE_SPEED_HEAD, SNAKE_TURN_RATE_HEAD
from snake_body import SnakeBody

BODY_SPAWN_PERIOD = 2


class SnakeHead:
    def __init__(self):
        self.body_spawn_remain_time = BODY_SPAWN_PERIOD
        self.bodys = []

    def begin_play(self):
        self.body_spawn_remain_time = BODY_SPAWN_PERIOD
        self.bodys = []

        self.uobject.bind_axis('TurnRate', self.__turn)

    def tick(self, delta_time):
        return
        self.__move_forward(delta_time)
        self.body_spawn_remain_time -= delta_time
        if self.body_spawn_remain_time < 0:
            self.body_spawn_remain_time += BODY_SPAWN_PERIOD

            snake_body = self.__spawn_body()
            if not self.bodys:
                snake_body.set_prev_snake(self)
            else:
                snake_body.set_prev_snake(self.bodys[-1])

            self.bodys.append(snake_body)

    def __move_forward(self, delta_time):
        location = self.uobject.get_actor_location()
        location += self.uobject.get_actor_forward() * SNAKE_MOVE_SPEED_HEAD * delta_time
        self.uobject.set_actor_location(location)

    def __turn(self, axis_value):
        turn_rate = axis_value * self.uobject.get_world_delta_seconds() * SNAKE_TURN_RATE_HEAD

        rotation = self.uobject.get_actor_rotation()
        rotation.yaw += turn_rate
        self.uobject.set_actor_rotation(rotation)

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
