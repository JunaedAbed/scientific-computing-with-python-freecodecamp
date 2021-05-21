import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        balls = []
        for _ in range(number):
            choice = random.randrange(len(self.contents))
            balls.append(self.contents.pop(choice))
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    count = []
    for key in expected_balls:
        count.append(expected_balls[key])
    successes = 0

    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        no_of_balls = []
        for key in expected_balls:
            no_of_balls.append(balls.count(key))

        if no_of_balls >= count:
            successes += 1

    return successes/num_experiments