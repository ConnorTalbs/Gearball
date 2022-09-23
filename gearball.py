#Connor Talbot
#CS 463G
#8/30/2022
#Build a program that displays and randomizes a gearball
#########################################################
from asyncio.windows_events import NULL
import random
from operator import mod
from turtle import right
import heapq

countH = 1
countV = 1

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
    global countH
    temp = ['','','']
    for i in range(3):
        temp[i] = ball[0][1][i]
    for i in range(4):
        for j in range(3):
            ball[i][1][j] = ball[i+1][1][j]
            if i == 3:
                ball[i][1][j] = temp[j]
    countH += 1
    if countH % 6 == 0:
        swapGearH()
    rotate90Clockwise(4)

def topCounterCW():
    global countH
    temp = ['','','']
    for i in range(3):
        temp[i] = ball[3][1][i]
    for i in reversed(range(4)):
        for j in range(3):
            ball[i][1][j] = ball[i-1][1][j]
            if i == 0:
                ball[i][1][j] = temp[j]
    countH -= 1 
    if countH % 6 == 0:
        swapGearH()
    rotate90CounterCW(4)

def bottomClockWise():
    temp = ['','','']
    for i in range(3):
        temp[i] = ball[0][5][i]
    for i in range(4):
        for j in range(3):
            ball[i][5][j] = ball[i+1][5][j]
            if i == 3:
                ball[i][5][j] = temp[j]
    rotate90Clockwise(5)

def bottomCounterCW():
    temp = ['','','']
    for i in range(3):
        temp[i] = ball[3][5][i]
    for i in reversed(range(4)):
        for j in range(3):
            ball[i][5][j] = ball[i-1][5][j]
            if i == 0:
                ball[i][5][j] = temp[j]
    rotate90CounterCW(5)

def rightClockWise():
    global countV
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
    countV += 1
    if countV % 6 == 0:
        swapGearV()
    rotate90Clockwise(1)

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
    rotate90CounterCW(1)

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
    rotate90Clockwise(3)

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
    rotate90CounterCW(3)

def rotate90Clockwise(face):
    # Setup
    A = [['','',''],['','',''],['','','']]
    for j,i in zip(range(2,8,2),range(3)):
        for x in range(3):
            A[i][x] = ball[face][j-1][x]
    # Rotate
    temp = A[0][0]
    A[0][0] = A[2][0]
    A[2][0] = A[2][2]
    A[2][2] = A[0][2]
    A[0][2] = temp

    temp = A[0][1]
    A[0][1] = A[1][0]
    A[1][0] = A[2][1]
    A[2][1] = A[1][2]
    A[1][2] = temp
    # Reset
    for j,i in zip(range(2,8,2), range(3)):
        for x in range(3):
            ball[face][j-1][x] = A[i][x]

def rotate90CounterCW(face):
    # Setup
    A = [['','',''],['','',''],['','','']]
    for j,i in zip(range(2,8,2),range(3)):
        for x in range(3):
            A[i][x] = ball[face][j-1][x]
    # Rotate
    temp = A[0][0]
    A[0][0] = A[0][2]
    A[0][2] = A[2][2]
    A[2][2] = A[2][0]
    A[2][0] = temp

    temp = A[0][1]
    A[0][1] = A[1][2]
    A[1][2] = A[2][1]
    A[2][1] = A[1][0]
    A[1][0] = temp
    
    # Reset
    for j,i in zip(range(2,8,2), range(3)):
        for x in range(3):
            ball[face][j-1][x] = A[i][x]

def swapGearH():
    temp1 = ball[3][4][0]
    for i in range(4):
        if i != 3:
            temp = ball[i][4][0] 
            ball[i][4][0] = ball[i+1][2][0]
            ball[i+1][2][0] = temp
        else:
            ball[3][4][0] = ball[0][2][0]
            ball[0][2][0] = temp1

def swapGearV():
    if ball[0][0][0] == 'r': 
        ball[0][0][0] = 'b'
        ball[4][6][0] = 'r'
    else:
        ball[0][0][0] = 'r'
        ball[4][6][0] = 'b'

    if ball[0][6][0] == 'r':
        ball[0][6][0] = 'g'
        ball[5][0][0] = 'r'
    else:
        ball[0][6][0] = 'r'
        ball[5][0][0] = 'g'

    if ball[5][6][0] == 'g':
        ball[5][6][0] = 'p'
        ball[2][6][0] = 'g'
    else:
        ball[5][6][0] = 'g'
        ball[2][6][0] = 'p'

    if ball[4][0][0] == 'b':
        ball[4][0][0] = 'g'
        ball[2][0][0] = 'p'
    else:
        ball[4][0][0] = 'b'
        ball[2][0][0] = 'p'
    

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

def checkState(ball, goal):
    close = 0
    for i in range(6):
        for j in range(0,6,2):
            for x in range(3):
                if ball[i][j+1][x] == goal[i][j+1][x]:
                    close += 1
    for i in range(6):
        for j in range(0,6,2):
            if ball[i][j+1][0] == goal[i][j+1][x]:
                close += 1
    return close

def solveAStar(ball):

    class node:
        def __init__(self, state, parent, depth, heuristic):
            self.state = state
            self.parent = parent
            self.depth = depth
            self.heuristic = heuristic

    #Must have state representation
    #Must have child function
    #Must check for solved state immediately before applying child function
    #Must add f and g functions
    #Must use heap/priority queue correctly & appropriately

    goal = [[['r'],['r','r','r'],['r'],['r','r','r'],['r'],['r','r','r'],['r']],
            [['y'],['y','y','y'],['y'],['y','y','y'],['y'],['y','y','y'],['y']],
            [['p'],['p','p','p'],['p'],['p','p','p'],['p'],['p','p','p'],['p']],
            [['o'],['o','o','o'],['o'],['o','o','o'],['o'],['o','o','o'],['o']],
            [['b'],['b','b','b'],['b'],['b','b','b'],['b'],['b','b','b'],['b']],
            [['g'],['g','g','g'],['g'],['g','g','g'],['g'],['g','g','g'],['g']]]

    open = []
    closed = []
    path = []
    selNode = [0]
    listCCW = [topCCW, botCCW, rightCCW, leftCCW]
    heapq.heapify(path)

    open.append(node(ball, NULL, 0, checkState(ball, goal)))

    while(True):
        #printBall()
        #Takes lowest heuristic from open
        max = 0
        index = 0
        for i in range(len(open)):
            #print(open[i].heuristic)
            if open[i].heuristic > max:
                selNode[0] = open[i]
                #print(selNode[0].heuristic)
                print(i)
        #Checks if open is empty and returns False
        if open == NULL:
            return False
        #Removes selected node from open
        open.remove(selNode[0])
        #If selected Node is goal state then return state and False
        if selNode[0].state == goal or selNode[0].heuristic == 72:
            print('Solved!')
            selNode
            return ball,False
        else:
            print('Not Solved!')
        #Gets children of selected state
        newNodes = []
        closed.append(selNode[0])
        #Getting children of selected node
        for i in range(4):
            newNodes.append(node(ball, selNode[0], selNode[0].depth + 1, checkState(ball ,goal)))
        for i,j in zip(newNodes,range(4)):
            if j == 0:
                topCCW()
                i.state = ball
                i.heuristic = checkState(ball, goal)
                topCW()
                if i.state != ball:
                    open.append(i)
            if j == 1:
                botCCW()
                i.state = ball
                i.heuristic = checkState(ball, goal)
                botCW()
                if i.state != ball:
                    open.append(i)
            if j == 2:
                rightCCW()
                i.state = ball
                i.heuristic = checkState(ball, goal)
                rightCW()
                if i.state != ball:
                    open.append(i)
            if j == 3:
                leftCCW()
                i.state = ball
                i.heuristic = checkState(ball, goal)
                leftCW()
                if i.state != ball:
                    open.append(i)


def main():
    choose = input("random or manual: ")
    if choose == "manual":
        while(True):
            printBall()
            face,direc = input("Enter face and direction: ").split()
            if face == 't' and direc == 'cw':
                topClockWise()
                bottomCounterCW()
            if face == 't' and direc == 'ccw':
                topCounterCW()
                bottomClockWise()
            if face == 'b' and direc == 'cw':
                bottomClockWise()
                topCounterCW()
            if face == 'b' and direc == 'ccw':
                bottomCounterCW()
                topClockWise
            if face == 'r' and direc == 'cw':
                rightClockWise()
                leftCounterCW()
            if face == 'r' and direc == 'ccw':
                rightCounterCW()
                leftClockWise()
            if face == 'l' and direc == 'cw':
                leftClockWise()
                rightCounterCW()
            if face == 'l' and direc == 'ccw':
                leftCounterCW()
                rightClockWise()

    if choose == "random":
        list = [topCW,topCCW,botCW,botCCW,rightCW,rightCCW,leftCW,leftCCW]
        listCW = [topCW, botCW, rightCW, leftCW]
        listCWT = [topCW]
        listCCW = [topCCW, botCCW, rightCCW, leftCCW]

        user = input("How many moves would you like to make: ")
        user = int(user)
        while user != 0:
            random.choice(listCWT)()
            user -= 1
        solveAStar(ball)
        printBall()
main()