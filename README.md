#Connor Talbot
#CS 463G
#8/30/2022
#Build a program that displays and randomizes a gearball
#########################################################

-The data structure that I have used is a system of arrays. How it works is this:

The 3d array is called 'ball' and consists of 3 arrays. The first array holds each face of the gearball and looks like this - [[front],[left],[right],...]. The second array is the individual columns and gears inside of each face: [['r'],['r','r','r'],['r'],['r','r','r'],['r'],['r','r','r'],['r'],...]. The third and final arrays are the values inside of each row on each face. To run all you have to do is run the program.

-The gearball GUI looks like this:

front
           ['r']
      ['r', 'r', 'r']      
['r'] ['r', 'r', 'r'] ['r']
      ['r', 'r', 'r']      
           ['r'] 

right
           ['y']
      ['y', 'y', 'y']
['y'] ['y', 'y', 'y'] ['y']
      ['y', 'y', 'y']
           ['y']

back
           ['p']
      ['p', 'p', 'p']
['p'] ['p', 'p', 'p'] ['p']
      ['p', 'p', 'p']
           ['p']

left
           ['o']
      ['o', 'o', 'o']
['o'] ['o', 'o', 'o'] ['o']
      ['o', 'o', 'o']
           ['o']

top
           ['b']
      ['b', 'b', 'b']
['b'] ['b', 'b', 'b'] ['b']
      ['b', 'b', 'b']
           ['b']

bottom
           ['g']
      ['g', 'g', 'g']
['g'] ['g', 'g', 'g'] ['g']
      ['g', 'g', 'g']
           ['g']

-The randomizer is very simple. I created functions for every move that you can simulate on the gearball and then put them into an array or list. The program will then ask for an input of how many times the user would like to make a move on the gearball. Using the random functions from python I can randomly choose a function or move from the list and apply it to the gearball. A while loop is used to iterate through as many times as the user specified and after all the moves have been completed, it displays the gearball. All you have to do is run the program and type in random and then the number of moves.

-The heuristic that I came up with is 

-I learned from this assignment that this way of coding the gearball is complicated and requires a lot of thinking and managing. I learned to simplify things in a way that made progress easier and take things one step at a time and start big and add details afterwards. I want to take this experience and do better to make my code more structured and optimized so that I don't have to necessarily hard code everything and make things easier on myself in the future.

-The who-did-what for me, Dylan Shade, and Phong Nguyen:
--We all did everything ourselves, Dylan and I had some discussions but nothing is shared between our programs. Phong did not contact the group.

