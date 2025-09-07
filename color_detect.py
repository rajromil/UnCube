
"""
Color Detection Module for Rubik's Cube Solver
Author: ROMIL RAJ
Description: HSV-based color detection for cube face recognition
"""

def fun (hsv_values):

    h = hsv_values[0]
    s = hsv_values[1]
    v = hsv_values[2]
    
    # Low saturation indicates white or very light colors
    if(s < 30 or v > 200):
        return "white"
    
    # Very dark colors (low value) are harder to distinguish
    if(v < 50):
        return "white"  # Default to white for very dark colors
    
    # Color detection based on hue ranges
    if(h < 8 or h > 165):  # Red wraps around at 180
        return "red"
    
    elif(h < 20):
        return "orange"
    
    elif(h < 35):
        return "yellow"
    
    elif(h < 85):
        return "green"
    
    elif(h < 132):
        return "blue"
    
    else:
        return "white"


def fun2(color):

    if(color == 'red'):
        return (0, 0, 255)
    
    elif(color == 'orange'):
        return (0, 140, 255)
    
    elif(color == 'yellow'):
        return (0, 255, 255)
    
    elif(color == 'green'):
        return (0, 255, 0)
    
    elif(color == 'blue'):
        return (255, 0, 0)
    
    else:
        return (255, 255, 255)


