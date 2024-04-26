import turtle
import random

# Constants (consider using a config file for flexibility)
WIDTH = 800
HEIGHT = 600
DELAY = 75
FOOD_SIZE = 32
SNAKE_SIZE = 20
DIRECTIONS = ["up", "down", "left", "right"]
SNAKE_STEP = SNAKE_SIZE

# Global variables
snake = []
snake_direction = "up"
food_pos = (0, 0)
score = 0
high_score = 0

# Define movement offsets for each direction
DIRECTION_OFFSETS = {
    "up": (0, SNAKE_SIZE),
    "down": (0, -SNAKE_SIZE),
    "left": (-SNAKE_SIZE, 0),
    "right": (SNAKE_SIZE, 0)
}

# Initialize screen
def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Snake")
    try:
        screen.bgpic("./assets/bg2.gif")  # Assuming correct path, adjust if needed
    except turtle.TurtleGraphicsError:
        print("Error: Background image not found. Using default background.")
    screen.tracer(0)
    return screen

# Helper functions
def update_high_score():
    global high_score
    if score > high_score:
        high_score = score
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))

def set_snake_direction(direction):
    global snake_direction
    if direction in DIRECTIONS:
        if (direction == "up" and snake_direction != "down") or \
           (direction == "down" and snake_direction != "up") or \
           (direction == "left" and snake_direction != "right") or \
           (direction == "right" and snake_direction != "left"):
            snake_direction = direction

def food_collision(food):
    global food_pos, score
    if get_distance(snake[-1], food_pos) < SNAKE_SIZE:
        score += 1
        update_high_score()
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def check_collision(new_head):
    x, y = new_head
    return (
        new_head in snake or
        x < -WIDTH / 2 or x > WIDTH / 2 or
        y < -HEIGHT / 2 or y > HEIGHT / 2
    )

def game_over():
    # Clear the screen and draw game over message
    screen.clear()
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("Game Over", align="center", font=("Arial", 24, "normal"))

    # Remove event handlers to prevent user interaction
    screen.onkeyrelease(None, "Up")
    screen.onkeyrelease(None, "Down")
    screen.onkeyrelease(None, "Left")
    screen.onkeyrelease(None, "Right")

def start_new_game(x, y):
    # Reset the game and restart the game loop
    reset_game()
    game_loop(stamper, food)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def get_random_food_pos():
    x = random.randint(-int(WIDTH/2) + FOOD_SIZE, int(WIDTH/2) - FOOD_SIZE)
    y = random.randint(-int(HEIGHT/2) + FOOD_SIZE, int(HEIGHT/2) - FOOD_SIZE)
    return (x, y)

def reset_game():
    # Clear the screen and reset game state
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [SNAKE_STEP, 0], [SNAKE_STEP * 2, 0], [SNAKE_STEP * 3, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)

def draw_snake(stamper):
    stamper.shape("circle")
    stamper.color("#009ef1")
    stamper.penup()
    stamper.clear()
    stamper.goto(snake[-1][0], snake[-1][1])
    stamper.stamp()
    stamper.shape("circle")
    for segment in snake[:-1]:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

def game_loop(stamper, food):
    stamper.clearstamps()

    new_head = snake[-1].copy()
    offset_x, offset_y = DIRECTION_OFFSETS[snake_direction]
    new_head[0] += offset_x
    new_head[1] += offset_y

    if check_collision(new_head):
        game_over()
    else:
        snake.append(new_head)

        if not food_collision(food):
            snake.pop(0)

        draw_snake(stamper)
        screen.title(f"Snake Game. Score: {score} High Score: {high_score}")
        screen.update()
        turtle.ontimer(lambda: game_loop(stamper, food), DELAY)

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")

# Main program
if __name__ == "__main__":
    screen = init_screen()
    stamper = turtle.Turtle()  # Create a turtle to draw the snake

    # Food
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()

    # Event handlers
    screen.listen()
    bind_direction_keys()

    # Initialize game
    reset_game()

    # Start the game loop
    game_loop(stamper, food)

    screen.exitonclick()  # Keep the window open until closed manually
