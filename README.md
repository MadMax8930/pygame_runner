## 2D Pygame (Pixel Runner)

### Concept
Mario based type game.
If the game is active, we will display the current game screen with all the graphics.
Else, we will show an pre/post game screen with instructions and score if there is one.

The display surface is the game window screen (800x600). 
It's unique and can contain three type of regular surfaces: 
plain color section, imported image bloc and/or rendered text bloc.
Each regular surface isn't static and has to be put on the display surface to be visible.
It is updating over and over again 60 times per second. (constant fps)

### Position control
Rectangles are used in this project for precise positioning of surfaces and efficient collision detection.

1: Create a surface 
2: Put it inside a rectangle
3: Place it on a image with blit() (block image transfer)

### Collision
- rect1.colliderect(rect2) -> returns 0 or 1  (rect2 collided with a rect1)
- rect1.collidepoint((x,y)) -> on mouse click ((x,y) point collided with a rect1)

### Player
1: Key input
2: Jump & Gravity
3: Creating floor

### Score
1: Update score on every frame
2: Continuously create new score surface
3: Display the surface

### Spawn objects logic
1: Create a list of obstacle rectangles
2: Everytime the timer triggers, add a new rectangle to that list
3: Move every rectangle in that list to the left on every frame
4: Delete rectangles too far left from the list

### Animate player and enemies
- For player:
   - Play walking animation if the player is on floor
   - Display the jump surface when the player is not on floor
- For enemies:
   - User an unbuild timer (like the spawn obstacles timer)
   - On every trigger we update all the surfaces for all types of enemies

For each timer, adding +1, +2, +3 to the USEREVENT will avoid any conflicts with the default python timer.

### Sprite class (player, obstacles)
Class that contains a surface and a rectangle for placement. 
It can be drawn and updated very easily, and is much more efficient.