########################################
# Name: Reuben Baltazar
# Collaborators: B
# Estimated time spent (hrs): 3
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)


    # You got it from here
    window_width = gw.get_width()
    window_height = gw.get_height()

    pyramid_height = BRICK_HEIGHT * (BRICKS_IN_BASE)
    start_y = (window_height - pyramid_height) // 2 + pyramid_height - BRICK_HEIGHT

    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row
        start_x = (window_width - bricks_in_row * BRICK_WIDTH) // 2
        
        for brick in range(bricks_in_row):
            brick_x = start_x + brick * BRICK_WIDTH
            brick_y = start_y - row * BRICK_HEIGHT
            brick_rect = GRect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
            gw.add(brick_rect)



if __name__ == '__main__':
    draw_pyramid()
