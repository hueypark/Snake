from config import SNAKE_BODY_ACTIVE_STANBY_TIME, SNAKE_INTERVAL, SNAKE_MOVE_SPEED_BODY, SNAKE_TURN_RATE_BODY
from unreal_engine import FVector


class SnakeBody:
    def __init__(self):
        self.prev_snake = None
        self.active = False
        self.active_stanby_time = SNAKE_BODY_ACTIVE_STANBY_TIME

    def begin_play(self):
        self.prev_snake = None
        self.active = False
        self.active_stanby_time = SNAKE_BODY_ACTIVE_STANBY_TIME

    def tick(self, delta_time):
        if self.active is False:
            self.active_stanby_time -= delta_time
            if self.active_stanby_time < 0:
                self.active = True

            return

        location = self.uobject.get_actor_location()
        location += self.uobject.get_actor_forward() * SNAKE_MOVE_SPEED_BODY * delta_time
        self.uobject.set_actor_location(location)

        self.__turn()

    def set_prev_snake(self, snake_object):
        self.prev_snake = snake_object

    def __turn(self):
        if self.prev_snake is None:
            return

        target_vector = self.__get_tail_location(self.prev_snake.uobject) - self.uobject.get_actor_location()
        forward_vector = self.uobject.get_actor_forward()
        cross_z = FVector.cross(target_vector, forward_vector).z
        turn_weight = -1
        if cross_z < 0:
            turn_weight = 1

        rotation = self.uobject.get_actor_rotation()
        rotation.yaw += turn_weight * self.uobject.get_world_delta_seconds() * SNAKE_TURN_RATE_BODY
        self.uobject.set_actor_rotation(rotation)

    @staticmethod
    def __get_tail_location(uobject):
        return uobject.get_actor_location() - (uobject.get_actor_forward() * SNAKE_INTERVAL)
