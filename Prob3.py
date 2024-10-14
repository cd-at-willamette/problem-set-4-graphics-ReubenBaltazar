########################################
# Name: Reuben Baltazar
# Collaborators: N
# Estimate time spent (hrs): 3
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    square = GRect((GW_WIDTH - SQUARE_SIZE) / 2, (GW_HEIGHT - SQUARE_SIZE) / 2, SQUARE_SIZE, SQUARE_SIZE)
    square.set_filled(True)
    square.set_fill_color("Purple")
    gw.add(square)

    score = 0
    score_label = GLabel(f"Score: {score}", SCORE_DX, GW_HEIGHT - SCORE_DY)
    score_label.set_font(SCORE_FONT)
    gw.add(score_label)

    def get_random_position(max_value):
        return random.randint(0, max_value)

    def update_score(new_score):
        score_label.set_label(f"Score: {new_score}")


    def on_mouse_down(event):
        nonlocal score  
        x, y = event.get_x(), event.get_y()


        if square.get_x() <= x <= square.get_x() + SQUARE_SIZE and square.get_y() <= y <= square.get_y() + SQUARE_SIZE:
            
            new_x = get_random_position(GW_WIDTH - SQUARE_SIZE)
            new_y = get_random_position(GW_HEIGHT - SQUARE_SIZE)
            square.set_location(new_x, new_y)

            
            score += 1
        else:
            
            score = 0

        
        update_score(score)

    
    gw.add_event_listener("click", on_mouse_down)











if __name__ == '__main__':
    clicky_box()
