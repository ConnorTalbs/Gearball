#Connor Talbot
#CS 463G
#8/30/2022
#Build a program that displays and randomizes a gearball
#########################################################

from operator import mod
from turtle import right

ball = [[['r'],['r','r','r'],['r'],['r','r','r'],['r'],['r','r','r'],['r']],
        [['y'],['y','y','y'],['y'],['y','y','y'],['y'],['y','y','y'],['y']],
        [['o'],['o','o','o'],['o'],['o','o','o'],['o'],['o','o','o'],['o']],
        [['w'],['w','w','w'],['w'],['w','w','w'],['w'],['w','w','w'],['w']],
        [['b'],['b','b','b'],['b'],['b','b','b'],['b'],['b','b','b'],['b']],
        [['g'],['g','g','g'],['g'],['g','g','g'],['g'],['g','g','g'],['g']]]

titles = ['front','right','back','left','top','bottom']

# r - front
# g - right
# b - back
# y - left
# o - top
# p - bottom

def printBall():
    for i in range(6):
        print(titles[i])
        print("          ",ball[i][0])
        print("     ",ball[i][1])
        print(ball[i][2],ball[i][3],ball[i][4])
        print("     ",ball[i][5])
        print("          ",ball[i][6],"\n")

def topClockWise():
    temp = ['','','']
    temp1 = ['','','']
    temp2 = ['','','']
    temp3 = ['','','']
    temp4 = ['','','']
    for i in range(3):
        temp2[i] = ball[0][1][i]
        temp3[i] = ball[1][1][i]
    for i in range(4):
        for j in range(3):
            temp[j] = ball[i][1][j]
            ball[i][1][j] = ball[i+2][1][j]
            ball[i+2][1][j] = temp[j]
            if i == 2:
                ball[i][1][j] = temp2[j]
            if i == 3:
                ball[i][1][j] = temp3[j]
    '''
    for i in range(3):
        temp4[i] = ball[0][3][j]
    for j in range(4):
        for x in range(3):
            if j !=3:
                temp4[x] = ball[j][3][x]
                ball[j][3][x] = ball[j+1][3][x]
                ball[j+1][3][x] = temp4[x]
            else:
                ball[j][3][x] = temp4[x] 
'''
def topCounterCW():
    temp = ['','','']
    temp1 = ['','','']
    temp2 = ['','','']
    temp3 = ['','','']
    for i in range(3):
        temp2[i] = ball[2][1][i]
        temp3[i] = ball[3][1][i]
    for i in reversed(range(4)):
        for j in reversed(range(3)):
            temp[j] = ball[i][1][j]
            ball[i][1][j] = ball[i-2][1][j]
            ball[i-2][1][j] = temp[j]
            if i == 1:
                ball[i][1][j] = temp2[j]
            if i == 0:
                ball[i][1][j] = temp3[j]

def bottomClockWise():
    temp = ['','','']
    for i in range(3):
        temp[i] = ball[0][5][i]
    for i in range(4):
        for j in range(3):
            ball[i][5][j] = ball[i+1][5][j]
            if i == 3:
                ball[i][5][j] = temp[j]

def bottomCounterCW():
    temp = ['','','']
    for i in range(3):
        temp[i] = ball[3][5][i]
    for i in reversed(range(4)):
        for j in reversed(range(3)):
            ball[i][5][j] = ball[i-1][5][j]
            if i == 0:
                ball[i][5][j] = temp[j]

def rightClockWise():
    temp1 = ['','','']
    temp2 = ['','','']
    temp3 = ['','','']
    for i, j in zip(range(0,6,2), range(3)):
        temp1[j] = ball[5][i+1][2]
        temp2[j] = ball[2][i+1][2]
        temp3[j] = ball[0][i+1][2]
    for i in range(5):
        for j,x in zip(range(0,6,2), range(3)):
            if i == 0 or i == 2 or i == 4:
                if i != 4:
                    ball[i][j+1][2] = ball[i+2][j+1][2]
                else:
                    ball[i][j+1][2] = temp3[x]
                    ball[0][j+1][2] = temp1[x]
                    ball[5][j+1][2] = temp2[x]

def rightCounterCW():
    temp1 = ['','','']
    temp2 = ['','','']
    temp3 = ['','','']
    for i, j in zip(range(0,6,2), range(3)):
        temp1[j] = ball[5][i+1][2]
        temp2[j] = ball[0][i+1][2]
        temp3[j] = ball[4][i+1][2]
    for i in reversed(range(5)):
        for j,x in zip(reversed(range(2,8,2)), range(3)):
            if i == 0 or i == 2 or i == 4:
                if i != 0:
                    ball[i][j-1][2] = ball[i-2][j-1][2]
                else:
                    ball[2][j-1][2] = temp1[x]
                    ball[0][j-1][2] = temp3[x]
                    ball[5][j-1][2] = temp2[x]
                    


def leftClockWise():
    temp1 = ['','','']
    temp2 = ['','','']
    temp3 = ['','','']
    for i, j in zip(range(0,6,2), range(3)):
        temp1[j] = ball[5][i+1][0]
        temp2[j] = ball[2][i+1][0]
        temp3[j] = ball[0][i+1][0]
    for i in range(5):
        for j,x in zip(range(0,6,2), range(3)):
            if i == 0 or i == 2 or i == 4:
                if i != 4:
                    ball[i][j+1][0] = ball[i+2][j+1][0]
                else:
                    ball[i][j+1][0] = temp3[x]
                    ball[0][j+1][0] = temp1[x]
                    ball[5][j+1][0] = temp2[x]

def leftCounterCW(count):
    temp1 = ['','','']
    temp2 = ['','','']
    temp3 = ['','','']
    for i, j in zip(range(0,6,2), range(3)):
        temp1[j] = ball[5][i+1][0]
        temp2[j] = ball[0][i+1][0]
        temp3[j] = ball[4][i+1][0]
    for i in reversed(range(5)):
        for j,x in zip(reversed(range(2,8,2)), range(3)):
            if i == 0 or i == 2 or i == 4:
                if i != 0:
                    ball[i][j-1][0] = ball[i-2][j-1][0]
                else:
                    ball[2][j-1][0] = temp1[x]
                    ball[0][j-1][0] = temp3[x]
                    ball[5][j-1][0] = temp2[x]
    if count % 3 == 0:
        for j in range(0,8,2):
            if ball[0][j][0] == 'r':
                ball[0][j][0] = 'b'
            else:
                ball[0][j][0] = 'r'

#def rotate90():


def main():
    count = 1
    while(True):
        printBall()
        face,direc = input("Enter face and direction: ").split()
        if face == 't' and direc == 'cw':
            topClockWise()
            bottomCounterCW()
            count += 1
        if face == 't' and direc == 'ccw':
            topCounterCW()
            bottomClockWise()
            count += 1
        if face == 'r' and direc == 'cw':
            rightClockWise()
            leftCounterCW()
            count += 1
        if face == 'r' and direc == 'ccw':
            rightCounterCW()
            leftClockWise()
            count += 1
        if face == 'l' and direc == 'cw':
            leftClockWise()
            rightCounterCW()
            count += 1
        if face == 'l' and direc == 'ccw':
            leftCounterCW(count)
            rightClockWise()
            count += 1
    #topRightTurn()
    #topLeftTurn()
    #bottomRightTurn()
    #bottomLeftTurn()

main()