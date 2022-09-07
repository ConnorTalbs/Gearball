#Connor Talbot
#CS 463G
#8/30/2022
#Build a program that displays and randomizes a gearball
#########################################################
import random
from operator import mod
from turtle import right

ball = [[['r'],['r','r','r'],['r'],['r','r','r'],['r'],['r','r','r'],['r']],
        [['y'],['y','y','y'],['y'],['y','y','y'],['y'],['y','y','y'],['y']],
        [['p'],['p','p','p'],['p'],['p','p','p'],['p'],['p','p','p'],['p']],
        [['o'],['o','o','o'],['o'],['o','o','o'],['o'],['o','o','o'],['o']],
        [['b'],['b','b','b'],['b'],['b','b','b'],['b'],['b','b','b'],['b']],
        [['g'],['g','g','g'],['g'],['g','g','g'],['g'],['g','g','g'],['g']]]

titles = ['front','right','back','left','top','bottom']

# r - front
# y - right
# o - back
# w - left
# b - top
# g - bottom

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
    for i in range(3):
        temp[i] = ball[0][1][i]
    for i in range(4):
        for j in range(3):
            ball[i][1][j] = ball[i+1][1][j]
            if i == 3:
                ball[i][1][j] = temp[j]
    rotate90Clockwise()

def topCounterCW():
    temp = ['','','']
    for i in range(3):
        temp[i] = ball[3][1][i]
    for i in reversed(range(4)):
        for j in range(3):
            ball[i][1][j] = ball[i-1][1][j]
            if i == 0:
                ball[i][1][j] = temp[j]         
                

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
        for j in range(3):
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

def leftCounterCW():
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

def rotate90Clockwise():
    # Setup
    A = [['','',''],['','',''],['','','']]
    for i in range(3):
        for j,x in zip(range(2,8,2),range(3)):
            A[i][x] = ball[4][j-1][x]
    '''
    # Rotate
    N = len(A[0])
    for i in range(3):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    '''
    for i in range(3):
        for j in range(3):
            temp = 
    # Reset
    for i in range(3):
        for j,x in zip(range(2,8,2),range(3)):
            ball[4][j-1][x] = A[i][x]

def topCW():
    topClockWise()
    bottomCounterCW()
def topCCW():
    topCounterCW()
    bottomClockWise()
def botCW():
    bottomClockWise()
    topCounterCW()
def botCCW():
    bottomCounterCW()
    topClockWise()
def rightCW():
    rightClockWise()
    leftCounterCW()
def rightCCW():
    rightCounterCW()
    leftClockWise()
def leftCW():
    leftClockWise()
    rightCounterCW()
def leftCCW():
    leftCounterCW()
    rightClockWise()

def main():
    choose = input("random or manual: ")
    if choose == "manual":
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
            if face == 'b' and direc == 'cw':
                bottomClockWise()
                topCounterCW()
            if face == 'b' and direc == 'ccw':
                bottomCounterCW()
                topClockWise
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
                leftCounterCW()
                rightClockWise()
                count += 1

    if choose == "random":
        list = [topCW,topCCW,botCW,botCCW,rightCW,rightCCW,leftCW,leftCCW]
        user = input("How many moves would you like to make: ")
        user = int(user)
        while user != 0:
            random.choice(list)()
            user -= 1
        printBall()

main()