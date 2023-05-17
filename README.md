## 2D Pygame (Pixel Runner) [In progress]

### Concepts
The display surface is the game window. This screen is unique.
It can contain three type of regular surfaces: plain color, imported image or rendered text
Each regular surface isn't static and has to be put on the display surface to be visible.
It's updating over and over again 60 times per second. (constant fps)

If the game is active, we will display the current game screen
Else, we will show an intro screen/game over screen with instructions and score.

### Position control
Rectangles are used in this project for precise positioning of surfaces and efficient collision detection.

1: Create a surface 
2: Put it inside a rectangle
3: Place it on a image with blit() (block image transfer)

### Collision
rect1.colliderect(rect2) -> returns 0 or 1  (rect2 collided with a rect1)
rect1.collidepoint((x,y)) -> on mouse click ((x,y) point collided with a rect1)

### Player
1: Key input
2: Jump & Gravity
3: Creating floor

### Score
1: Update score on every frame
2: Continuously create new score surface
3: Display the surface

### Spawn objects logic (user event)
1: Create a list of obstacle rectangles
2: Everytime the timer triggers, add a new rectangle to that list
3: Move every rectangle in that list to the left on every frame
4: Delete rectangles too far left from the list

### Animate player and enemies
[in progress]

### Sprite class
Surface for image information -> Placement via rectangle (combines both -> much more easier)