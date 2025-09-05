"""
Info Display Module for Rubik's Cube Solver
Author: ROMIL RAJ
Description: Handles solution display and augmented reality arrows
"""

import cv2 as cv

def output(text, frame, AnsIndex):

    if(AnsIndex == -1):
        return

    text = text.split()

    # followed the sequence correctly
    if(AnsIndex >= len(text)):
        cv.putText(frame, 'CUBE SOLVED!', (120, 80), cv.FONT_HERSHEY_SIMPLEX, 1.8, (0, 255, 0), 3)
        cv.putText(frame, 'Congratulations!', (150, 120), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
        return

    # current move
    move = text[AnsIndex]

    # augmented arrows
    if(move == 'R'):
        cv.arrowedLine(frame, (600, 540), (600, 180), (0, 0, 0), 10)

    elif(move == "R'"):
        cv.arrowedLine(frame, (600, 180), (600, 540), (0, 0, 0), 10)

    elif(move == "R2"):
        cv.arrowedLine(frame, (570, 540), (570, 180), (0, 0, 0), 10)
        cv.arrowedLine(frame, (630, 540), (630, 180), (0, 0, 0), 10)

    elif(move == "R'2"):
        cv.arrowedLine(frame, (570, 180), (570, 540), (0, 0, 0), 10)
        cv.arrowedLine(frame, (630, 180), (630, 540), (0, 0, 0), 10)

    elif(move == 'L'):
        cv.arrowedLine(frame, (120, 180), (120, 540), (0, 0, 0), 10)

    elif(move == "L'"):
        cv.arrowedLine(frame, (120, 540), (120, 180), (0, 0, 0), 10)

    elif(move == 'L2'):
        cv.arrowedLine(frame, (90, 180), (90, 540), (0, 0, 0), 10)
        cv.arrowedLine(frame, (150, 180), (150, 540), (0, 0, 0), 10)

    elif(move == "L'2"):
        cv.arrowedLine(frame, (90, 540), (90, 180), (0, 0, 0), 10)
        cv.arrowedLine(frame, (150, 540), (150, 180), (0, 0, 0), 10)

    elif(move == 'U'):
        cv.arrowedLine(frame, (540, 120), (180, 120), (0, 0, 0), 10)

    elif(move == "U'"):
         cv.arrowedLine(frame, (180, 120), (540, 120), (0, 0, 0), 10)

    elif(move == 'U2'):
        cv.arrowedLine(frame, (540, 90), (180, 90), (0, 0, 0), 10)
        cv.arrowedLine(frame, (540, 150), (180, 150), (0, 0, 0), 10)

    elif(move == "U'2"):
        cv.arrowedLine(frame, (180, 90), (540, 90), (0, 0, 0), 10)
        cv.arrowedLine(frame, (180, 150), (540, 150), (0, 0, 0), 10)

    elif(move == 'D'):
        cv.arrowedLine(frame, (180, 600), (540, 600), (0, 0, 0), 10)

    elif(move == "D'"):
        cv.arrowedLine(frame, (540, 600), (180, 600), (0, 0, 0), 10)

    elif(move == 'D2'):
        cv.arrowedLine(frame, (180, 570), (540, 570), (0, 0, 0), 10)
        cv.arrowedLine(frame, (180, 630), (540, 630), (0, 0, 0), 10)

    elif(move == "D'2"):
        cv.arrowedLine(frame, (540, 570), (180, 570), (0, 0, 0), 10)
        cv.arrowedLine(frame, (540, 630), (180, 630), (0, 0, 0), 10)

    elif(move == 'F'):
        cv.line(frame, (120, 120), (120, 300), (0, 0, 0), 10)
        cv.arrowedLine(frame, (120, 120), (300, 120), (0, 0, 0), 10)
        cv.line(frame, (600, 600), (600, 420), (0, 0, 0), 10)
        cv.arrowedLine(frame, (600, 600), (420, 600), (0, 0, 0), 10)

    elif(move == "F'"):
        cv.arrowedLine(frame, (120, 120), (120, 300), (0, 0, 0), 10)
        cv.line(frame, (120, 120), (300, 120), (0, 0, 0), 10)
        cv.arrowedLine(frame, (600, 600), (600, 420), (0, 0, 0), 10)
        cv.line(frame, (600, 600), (420, 600), (0, 0, 0), 10)

    elif(move == 'F2'):
        cv.line(frame, (120, 120), (120, 300), (0, 0, 0), 10)
        cv.arrowedLine(frame, (120, 120), (300, 120), (0, 0, 0), 10)
        cv.line(frame, (600, 600), (600, 420), (0, 0, 0), 10)
        cv.arrowedLine(frame, (600, 600), (420, 600), (0, 0, 0), 10)

        cv.line(frame, (150, 150), (200, 150), (0, 0, 0), 10)
        cv.line(frame, (150, 150), (150, 200), (0, 0, 0), 10)

        cv.line(frame, (570, 570), (570, 520), (0, 0, 0), 10)
        cv.line(frame, (570, 570), (520, 570), (0, 0, 0), 10)

    elif(move == "F'2"):
        cv.arrowedLine(frame, (120, 120), (120, 300), (0, 0, 0), 10)
        cv.line(frame, (120, 120), (300, 120), (0, 0, 0), 10)
        cv.arrowedLine(frame, (600, 600), (600, 420), (0, 0, 0), 10)
        cv.line(frame, (600, 600), (420, 600), (0, 0, 0), 10)

        cv.line(frame, (150, 150), (200, 150), (0, 0, 0), 10)
        cv.line(frame, (150, 150), (150, 200), (0, 0, 0), 10)

        cv.line(frame, (570, 570), (570, 520), (0, 0, 0), 10)
        cv.line(frame, (570, 570), (520, 570), (0, 0, 0), 10)

    elif(move == 'B'):

        cv.putText(frame, 'BACK FACE TURN', (120, 80), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)
        cv.arrowedLine(frame, (120, 120), (120, 300), (0, 0, 0), 10)
        cv.line(frame, (120, 120), (300, 120), (0, 0, 0), 10)
        cv.arrowedLine(frame, (600, 600), (600, 420), (0, 0, 0), 10)
        cv.line(frame, (600, 600), (420, 600), (0, 0, 0), 10)

    elif(move == "B'"):

        cv.putText(frame, "BACK FACE TURN'", (120, 80), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)
        cv.line(frame, (120, 120), (120, 300), (0, 0, 0), 10)
        cv.arrowedLine(frame, (120, 120), (300, 120), (0, 0, 0), 10)
        cv.line(frame, (600, 600), (600, 420), (0, 0, 0), 10)
        cv.arrowedLine(frame, (600, 600), (420, 600), (0, 0, 0), 10)

    elif(move == "B2"):

        cv.putText(frame, 'BACK FACE TURN x2', (120, 80), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)
        cv.arrowedLine(frame, (120, 120), (120, 300), (0, 0, 0), 10)
        cv.line(frame, (120, 120), (300, 120), (0, 0, 0), 10)
        cv.arrowedLine(frame, (600, 600), (600, 420), (0, 0, 0), 10)
        cv.line(frame, (600, 600), (420, 600), (0, 0, 0), 10)

        cv.line(frame, (150, 150), (200, 150), (0, 0, 0), 10)
        cv.line(frame, (150, 150), (150, 200), (0, 0, 0), 10)

        cv.line(frame, (570, 570), (570, 520), (0, 0, 0), 10)
        cv.line(frame, (570, 570), (520, 570), (0, 0, 0), 10)

    elif(move == "B'2"):

        cv.putText(frame, "BACK FACE TURN' x2", (120, 80), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)
        cv.line(frame, (120, 120), (120, 300), (0, 0, 0), 10)
        cv.arrowedLine(frame, (120, 120), (300, 120), (0, 0, 0), 10)
        cv.line(frame, (600, 600), (600, 420), (0, 0, 0), 10)
        cv.arrowedLine(frame, (600, 600), (420, 600), (0, 0, 0), 10)

        cv.line(frame, (150, 150), (200, 150), (0, 0, 0), 10)
        cv.line(frame, (150, 150), (150, 200), (0, 0, 0), 10)

        cv.line(frame, (570, 570), (570, 520), (0, 0, 0), 10)
        cv.line(frame, (570, 570), (520, 570), (0, 0, 0), 10)



# printing invalid cube on screen
def outputIV(text, blank2):
        cv.putText(blank2, 'ERROR: Invalid Cube Configuration!', (300, 150), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
        cv.putText(blank2, 'Please rescan all faces correctly', (320, 180), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)


# else printing correct seq of answer
def outputAns(text, blank2):
        cv.putText(blank2, 'SOLUTION:', (250, 60), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        cv.putText(blank2, text, (250, 100), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)




