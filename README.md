## Setup:
1. ```pipenv init```
2. ```pip install pygame```
3. ```python PongAIvAI.py``` to make sure it runs

## Instructions:
1. Create a file <teamname>_ai.py
2. Write a function pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size) that will:
```
    Return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball, assuming the ball will
    not be moving
    
    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle. 
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively
    
    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the 
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively
    
    The coordinates look as follows:
    
     0             x
     |------------->
     |
     |             
     |
 y   v
```
    
3. Test it by modifying line 387/388 in PongAIvAI.py and running ```python PongAIvAI.py```
