import arcade
import random

# setting the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Template"


# game class
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background=arcade.load_texture("P.2.5/background.png")
        self.car=Car("P.2.5/car.png",0.6)
        self.wall = Wall("P.2.5/wall.png", 0.5)
        self.score=0
    

    # initial values
    def setup(self):
        self.car.center_x=SCREEN_WIDTH/2
        self.car.center_y=100
        self.wall.center_x = SCREEN_WIDTH/2
        self.wall.center_y = SCREEN_HEIGHT
        self.wall.change_y = 5

    # drawing
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.car.draw()
        self.wall.draw()
        arcade.draw_text(f"Score: {self.score}",10,570,arcade.color.GREEN,20)
    # game logic
    def update(self, delta_time):
        self.car.update()
        self.wall.update()
        if arcade.check_for_collision(self.car, self.wall):
            self.car.stop()
            self.wall.stop()
        if self.wall.center_y <0:
            self.score +=1



    # pressing the key
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.car.change_x = 5
            self.car.angle = -15
        if key == arcade.key.LEFT:
            self.car.change_x =-5
            self.car.angle = 15

    # releasing the key
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.car.change_x=0
            self.car.angle = 0
            


class Car(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        if self.left < 50:
            self.left = 50
        if self.right > SCREEN_WIDTH-50:
            self.right = SCREEN_WIDTH-50
class Wall(arcade.Sprite):
    def update(self):
        
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
            self.center_x= random.randint(130,SCREEN_WIDTH-130)
        self.center_y -= self.change_y

window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
