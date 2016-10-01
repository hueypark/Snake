SNAKE_MOVE_SPEED = 300


class SnakeHead:
    def tick(self, delta_time):
        location = self.uobject.get_actor_location()

        location += self.uobject.get_actor_forward() * SNAKE_MOVE_SPEED * delta_time

        self.uobject.set_actor_location(location)
