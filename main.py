import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross the road")
screen.tracer(0)
screen.listen()

player = Player()
cars = []
score = Scoreboard()

screen.onkey(player.move, "Up")

if __name__ == "__main__":
    game_is_on = True
    while game_is_on:
        if player.ycor() >= 290:
            player.restart()
            score.increase_lvl()
            for i in cars:
                i.lvl_up()
        time.sleep(0.05)
        screen.update()
        if random.randint(1, 7) == 1:
            car = CarManager(score.level)
            cars.append(car)
        for i in cars:
            if i.xcor() >= 310:
                cars.remove(i)
            i.move()
            if (player.ycor() + 10 >= i.ycor() - 10) and (player.ycor() - 8 <= i.ycor() + 10):
                if i.distance(player) <= 30:
                    score.game_over()
                    game_is_on = False
                    break

screen.exitonclick()