############################################################
# Name: Reuben Baltazar
# Name(s) of anyone worked with: N
# Est time spent (hr): 4
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!
    body = GRect(150, 250, 100, 120)
    body.set_color("Blue")
    body.set_filled(True)
    gw.add(body)

    head = GOval(135, 150, 130, 130)
    head.set_color("Orange")
    head.set_filled(True)
    gw.add(head)

    left_eye = GOval(155, 180, 25, 25)
    left_eye.set_color("White")
    left_eye.set_filled(True)
    gw.add(left_eye)

    right_eye = GOval(220, 180, 25, 25)
    right_eye.set_color("White")
    right_eye.set_filled(True)
    gw.add(right_eye)

    left_pupil = GOval(165, 190, 8, 8)
    left_pupil.set_color("Black")
    left_pupil.set_filled(True)
    gw.add(left_pupil)

    right_pupil = GOval(230, 190, 8, 8)
    right_pupil.set_color("Black")
    right_pupil.set_filled(True)
    gw.add(right_pupil)

    mouth = GRect(175, 230, 50, 10)
    mouth.set_color("Black")
    mouth.set_filled(True)
    gw.add(mouth)

    # Draw the hair (a triangular shape with ovals)
    hair_oval_1 = GOval(160, 100, 20, 60)
    hair_oval_1.set_color("Brown")
    hair_oval_1.set_filled(True)
    gw.add(hair_oval_1)

    hair_oval_2 = GOval(185, 70, 30, 90)
    hair_oval_2.set_color("Brown")
    hair_oval_2.set_filled(True)
    gw.add(hair_oval_2)

    hair_oval_3 = GOval(220, 100, 20, 60)
    hair_oval_3.set_color("Brown")
    hair_oval_3.set_filled(True)
    gw.add(hair_oval_3)

    left_arm = GLine(150, 280, 100, 240)  
    gw.add(left_arm)

    right_arm = GLine(250, 280, 300, 240) 
    gw.add(right_arm)

    
    left_hand = GRect(90, 220, 20, 20)  
    left_hand.set_color("Orange")
    left_hand.set_filled(True)
    gw.add(left_hand)

    left_middle_finger = GLine(100, 220, 100, 200)  
    gw.add(left_middle_finger)

    right_hand = GRect(290, 220, 20, 20)  
    right_hand.set_color("Orange")
    right_hand.set_filled(True)
    gw.add(right_hand)

    right_middle_finger = GLine(300, 220, 300, 200)  
    gw.add(right_middle_finger)





if __name__ == '__main__':
    draw_image()
