import tkinter.filedialog


# Create string with instructions.
print('''
Read the three words next to each letter.
Then decide which of the four letter choices is most like you.
Rank that letter with a '4'.
After that, continue to rank the other three letter choices from a 3 to a 1,
where a '1' is the least like you and a '3' would be the most like you.
Your answer should wind up being a list of 4 numbers.
The first number in the list being the ranking of the first group of words and so on.
For example your answer should look similar to this -> 4,1,2,3

''')

introQuestion = input("Would you like to see an example before moving on? Type 'yes' or 'no':  ").lower()

if introQuestion != 'no':
    print('''
Let's go over the first question you will encounter then:

A: Active, opportunistic, spontaneous.
B: Parental, traditional, responsible.
C: Authentic, harmonious, compassionate.
D: Versatile, inventive, competent.

Let's read over each group of words...
Now lets look at the grouping of words in 'A'.
The first number I put in will be how much I think that first group of words is like me.
We will be using a 1-4, with a '4' being the most like me a '1' being the least like me.
Let's say I choose a '3', so it is very much like me, but not the most like me.
The first number I will type in will be a '3' and then seperated by a coma (,).
So I should have something that looks like this -> 3,

Following that comma without using a space, input the number you think that the group B
words fit using now either a '1,2, or 4' since we already used a '3' on the one above.
Let's say now that I think group B is the most like me so I will put a '4'.
Now my input should look like this -> 3,4,
Just continue this for the next two groupings of words. After you are finished inputing your numbers
you should have something like this -> 3,4,1,2
After typing in the last number hit enter and then you will be prompted with 4 new groupings of words.
Continue putting in your answers in the same fashion as you did the previous grouping.
Good luck and have fun.
    ''')

else:
    print('\nLets get started then.')

    
# Create strings with questions for input.
q1 = input ('''
A: Active, opportunistic, spontaneous.
B: Parental, traditional, responsible.
C: Authentic, harmonious, compassionate.
D: Versatile, inventive, competent.
''')
q1List = q1.split(',')


q2 = input ('''
E: Curious, conceptual, knowledgeable.
F: Unique, empathetic, responsible.
G: Practical, sensible, dependable.
H: Competitive, hasty, impactful.
''')
q2List = q2.split(',')


q3 = input ('''
I: Loyal, conservative, organized.
J: Devoted, warm, poetic.
K: Realistic, open-minded, adventuresome.
L: Theoretical, seeking, ingenious.
''')
q3List = q3.split(',')
      
q4 = input ('''
M: Concerned, procedural, cooperative.
N: Daring, impulsive, fun.
O: Tender, inspirational, dramatic.
P: Determined, complex, composed.
''')
q4List = q4.split(',')

      
q5 = input ('''
Q: Philosophical, principled, rational.
R: Cheerful, affectionate, sympathetic.
S: Exciting, courageous, skillful.
T: Orderly, conventional, caring.
''')
q5List = q5.split(',')


# Compile totals for each of the answers in a list.

'''
Orange total comes from A,H,K,N,S
Blue total comes from C,F,J,O,R
Gold total comes from B,G,I,M,T
Green total comes from D,E,L,P,Q
'''
# orange = int(q1List[0]) + int(q2List[3]) + int(q3List[2]) + int(q4List[1]) + int(q5List[2])
# blue = int(q1List[2]) + int(q2List[1]) + int(q3List[1]) + int(q4List[2]) + int(q5List[1])
# gold = int(q1List[1]) + int(q2List[2]) + int(q3List[0]) + int(q4List[0]) + int(q5List[3])
# green = int(q1List[3]) + int(q2List[0]) + int(q3List[3]) + int(q4List[3]) + int(q5List[0])

orange = q1List[0], q2List[3], q3List[2], q4List[1], q5List[2]
sumOrange = sum([int(num) for num in orange])

blue = q1List[2], q2List[1], q3List[1], q4List[2], q5List[1]
sumBlue = sum([int(num) for num in blue])

gold = q1List[1], q2List[2], q3List[0], q4List[0], q5List[3]
sumGold = sum([int(num) for num in gold])

green = q1List[3], q2List[0], q3List[3], q4List[3], q5List[0]
sumGreen = sum([int(num) for num in green])


# Compare the totals of each color to find personality color the user is.
# Open and read text file for the personality color that the user is.

orangeFile = 'enter location of text file/Orange.txt'
blueFile = 'enter location of text file/Blue.txt'
goldFile = 'enter location of text file/Gold.txt'
greenFile = 'enter location of text file/Green.txt'

if sumOrange >= sumBlue and sumOrange >= sumGreen and sumOrange >= sumGold:
    orangeText = open(orangeFile, 'r')
    print(orangeText.read())
    orangeText.close()

if sumBlue >= sumOrange and sumBlue >= sumGreen and sumBlue >= sumGold:
    blueText = open(blueFile, 'r')
    print(blueText.read())
    blueText.close()
    
if sumGold >= sumBlue and sumGold >= sumGreen and sumGold >= sumOrange:
    goldText = open(goldFile, 'r')
    print(goldText.read())
    goldText.close()

if sumGreen >= sumBlue and sumGreen >= sumGold and sumGreen >= sumOrange:
    greenText = open(greenFile, 'r')
    print(greenText.read())
    greenText.close()



