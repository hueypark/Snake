from config import SNAKE_MOVE_SPEED


class SnakeHead:
    def begin_play(self):
        self.uobject.bind_axis('TurnRate', self.__turn)

    def tick(self, delta_time):
        self.__move_forward(delta_time)

    def __move_forward(self, delta_time):
        location = self.uobject.get_actor_location()
        location += self.uobject.get_actor_forward() * SNAKE_MOVE_SPEED * delta_time
        self.uobject.set_actor_location(location)

    def __turn(self, axis_value):
        turn_rate = axis_value * self.uobject.get_world_delta_seconds() * 45

        rotation = self.uobject.get_actor_rotation()
        rotation.yaw += turn_rate
        self.uobject.set_actor_rotation(rotation)

    def __spawn_body(self):
        snake_body = self.uobject.call_function('SpawnSnakeBody')


