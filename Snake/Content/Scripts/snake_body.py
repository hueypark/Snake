from config import SNAKE_MOVE_SPEED


class SnakeBody:
    def tick(self, delta_time):
        location = self.uobject.get_actor_location()

        location += self.uobject.get_actor_forward() * SNAKE_MOVE_SPEED * delta_time

        self.uobject.set_actor_location(location)
