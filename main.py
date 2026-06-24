import time
from snake import Snake 
from turtle import Screen
from food import Food
from score import Scoreboard


window=Screen()
window.bgcolor("black")
window.setup(600,600)
 
window.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

game_on=True
while game_on:
    snake.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake.up,"Up")
    window.onkey(snake.down,"Down")
    window.onkey(snake.right,"Right")
    window.onkey(snake.left,"Left")
    if snake.head.distance(food)<15:
        food.appear()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>270 or snake.head.xcor() <-270 or snake.head.ycor()>270 or snake.head.ycor()<-270:
       game_on=False
       score.game_over()

    for segment in snake.turtles[:-1]:
      if  snake.head.distance(segment)<10:
        game_on=False
        score.game_over




window.exitonclick()