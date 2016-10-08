from config import SNAKE_MOVE_SPEED, SNAKE_TURN_RATE
from unreal_engine import FVector


class SnakeBody:
    def __init__(self):
        self.prev_snake = None

    def begin_play(self):
        self.prev_snake = None

    def tick(self, delta_time):
        location = self.uobject.get_actor_location()
        location += self.uobject.get_actor_forward() * SNAKE_MOVE_SPEED * delta_time
        self.uobject.set_actor_location(location)

        self.__turn()

    def set_prev_snake(self, snake_object):
        self.prev_snake = snake_object

    def __turn(self):
        if self.prev_snake is None:
            return

        target_vector = self.prev_snake.uobject.get_actor_location() - self.uobject.get_actor_location()
        forward_vector = self.uobject.get_actor_forward()
        cross_z = FVector.cross(target_vector, forward_vector).z
        turn_weight = -1
        if cross_z < 0:
            turn_weight = 1

        rotation = self.uobject.get_actor_rotation()
        rotation.yaw += turn_weight * self.uobject.get_world_delta_seconds() * SNAKE_TURN_RATE
        self.uobject.set_actor_rotation(rotation)
