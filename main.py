from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import colorgram

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My first snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



# rgb_colors = []
# colors = colorgram.extract("StarryNightFull4.jpg", 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(42, 106, 144), (16, 42, 61), (109, 165, 189), (23, 47, 42), (138, 176, 158), (76, 102, 90), (72, 147, 172), (51, 45, 37), (14, 65, 123), (177, 177, 121), (98, 95, 67), (206, 210, 136), (197, 223, 204), (222, 227, 188), (21, 79, 97), (182, 217, 232), (167, 207, 180), (182, 162, 42), (43, 75, 65), (98, 146, 134)]



























screen.exitonclick()