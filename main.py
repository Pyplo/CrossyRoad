import time
from turtle import Screen
from player import Player


from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

gamer = Player()
manager = CarManager()
scoreboardd = Scoreboard()

screen.listen()
screen.onkey(gamer.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    manager.create_cars()
    manager.move_cars()
    for car in manager.all_cars:
        if car.distance(gamer) < 20:
            game_is_on = False
            scoreboardd.game_over()

    if gamer.is_at_finish_line():
        gamer.go_to_start()
        manager.level_up()
        scoreboardd.increase_level()


screen.exitonclick()