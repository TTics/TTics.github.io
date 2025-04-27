import pygame
from pygame import init

init()

# Check if Pygame is loaded correctly
if not hasattr(initialization, 'loaded'):
    try:
        initialization.load()
    except Exception as e:
        print("Error initializing Pygame:", e)
    else:
        print("Pygame initialized successfully.")
```

### Step 2: Create the Game Board
Set up a grid where the snake and food will move across.

```python
# Grid size (e.g., 20x20)
grid_size = 20

# Initialize the game board with walls
board = [[1 for _ in range(grid_size)] for _ in range(grid_size)]
```

### Step 3: Generate Food and Power Ball
Randomly place food and a power ball.

```python
# Probability of placing food
food_probability = 0.4

# Create variables to track snake's position, direction
snake = [[1 for _ in range(grid_size)] for _ in range(grid_size)]
snake[0][2] = 0  # Start at position (0, 2)
direction = [1, 0]  # Initial direction: right
game_over = False

# Generate food and power ball
food = None
power_ball = None

while not game_over:
    for i in range(grid_size):
        for j in range(grid_size):
            if random.randint(0, grid_size*grid_size) < (food_probability * (i + j)) and board[i][j] == 1:
                food = [i, j]
    # Generate power ball once a few foods are eaten
    if len([k for k in range(len(foods)) if foods[k][0] == i and foods[k][1] == j]) >= 3:
        power_ball = [i, j]
    else:
        food = None
```

### Step 4: Handle Input
Use Pygame's keyboard events to control the snake's movement.

```python
# Keyboard controls
keys = { 'ArrowUp': True,
         'ArrowDown': False,
         'ArrowLeft': False,
         'ArrowRight': True }

def move_snake(direction):
    global direction, snake
    new_snake = [snake[0], snake[1]]
    if direction == 0:  # Up
        new_snake[1] = 1
    elif direction == 2:  # Down
        new_snake[1] = grid_size - 2
    else:
        new_snake[0] = 1
    snake = [new_snake[0], new_snake[1]]

def handle_keydown(event):
    if event == 'ArrowUp' and direction != 0:
        direction = 0
    elif event == 'ArrowDown' and direction != grid_size - 2:
        direction = grid_size - 2
    elif event == 'ArrowLeft' and direction != 1:
        direction = 1
    elif event == 'ArrowRight' and direction != 0:
        direction = 0

def handle_keyup(event):
    if direction in (0, grid_size - 2):
        direction = 0
    elif direction in (1, grid_size - 2):
        direction = 1

# Initialize game loop
running = True
while running:
    for event in sys.stdin:
        handle_keydown(event)

    move_snake(direction=direction)
    handle_keyup(event)

    # Check if snake ate food or power ball
    if all(snake[i] == food for i in range(len(food))):
        score += 1
        board[food[0]][food[1]] = 0

    elif all(snake[i] == power_ball for i in range(len(power_ball))):
        score += 2
        print("Power Ball collected!")

    # Check for wall collisions (snake eats itself)
    if any(snake[i] == board.size or snake[i][j] == board.size for j in [0,1] for i in range(grid_size)):
        game_over = True

    # Draw the board
    board = [[str(board[i][j]) if board[i][j] != 1 else (' ', '')
              for j in range(grid_size)]
             for i in range(grid_size)]

    screen = pygame.display.get_surface()
    screen_rect = screen.get_rect(center=(screen.width//2, screen.height//2))
    board_rect = board.get_rect(center=board.width//2, board.height//2)

    # Draw the snake and food
    pygame.draw.rect(screen, (0, 255, 0),
                   [board_rect.left - 1, board_rect.top - 1,
                    board_rect.width + 3, board_rect.height + 4])
    for i in range(len(board)):
        if board[i][j] == snake[i]:
            pygame.draw.rect(screen, (255, 0, 0),
                           [board_rect.left - 1, board_rect.top - 1,
                            board_rect.width + 3, board_rect.height + 4])