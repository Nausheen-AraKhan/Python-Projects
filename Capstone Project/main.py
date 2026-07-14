from turtle import Screen
import time
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
player=Player()
car_manager=Car()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(fun=player.move_up,key="Up")
is_game_on=True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on=False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_starting_pos()
        car_manager.level_up()
screen.exitonclick()
