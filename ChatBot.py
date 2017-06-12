import time
import os.path
from random import randint

def distance(x, y):
    """
    Find the Levenshtein distance between two strings.
    """
    x = str(x)
    y = str(y)
    if len(x) > len(y):
        x, y = y, x
    if len(y) == 0:
        return len(x)
    x_length = len(x) + 1
    y_length = len(y) + 1
    dis = [[0] * y_length for x in range(x_length)]
    for i in range(x_length):
       dis[i][0] = i
    for j in range(y_length):
       dis[0][j]=j
    for i in range(1, x_length):
        for j in range(1, y_length):
            delete = dis[i-1][j] + 1
            insert = dis[i][j-1] + 1
            sub = dis[i-1][j-1]
            if x[i-1] != y[j-1]:
                sub += 1
            dis[i][j] = min(insert, delete, sub)
    return dis[x_length-1][y_length-1]

def perdif(x, y):
    '''
    Finds the percentage difference between two strings
    '''
    x = str(x)
    y = str(y)
    return 100 * distance(x, y) / float(max(len(x), len(y)))

def rd(x):
    '''
    x = what you want to find in the list
    returns the following line to the line you search
    '''
    path = "E:\Development\ChatBot"
    file = str(name)+ ".txt"
    complete = os.path.join(path, file)
    f = open(complete, "r")
    r = f.readlines()
    r = [s.strip("\n") for s in r]
    a = ""
    for i in range(0, len(r)):
        #Incase of mispelling, this will check for the percentage difference
        if float('%.2f' % perdif(r[i],x)) < 40 and r[i-1] == "":
            a += r[i+1]
            break
        else:
            continue
    return a

def ad(x):
    '''
    x = what to add to the document
    '''
    path = "E:\Development\Chatbot"
    file = str(name) + ".txt"
    complete = os.path.join(path, file)
    f = open(complete, "a")
    f.write("\n" + x)
    f.close()

def wd(x,y,z):
    '''
    x = which input's answer to overwrite
    y = what to overwrite
    z = what to overwrite y with
    '''
    path = "E:\Development\Chatbot"
    file = str(name) + ".txt"
    complete = os.path.join(path, file)
    f = open(complete, "r")
    read = f.readlines()
    if y  + "\n" == read[read.index(x +"\n")+1]:
        read = [i.replace(y,z) for i in read]
    f = open(complete, "w")
    f.writelines(read)
    f.close()

name = "data"

#Different greetings to start off the conversation
start = ["Hello","Hey!","How are you?","How's it going?",
         "How is everything?","How have you been?"]
x = input(start[randint(0,len(start)-1)] + "\n")


while True:
    #converts all input into lowercase
    x = x.lower()
    #strips all punctuation
    for i in [",", ".", "!", "?","'"]:
        if i in x:
            x = x.replace(i, "")
    #If the input is not a part of the data list
    #This will ask for a sample output and save it
    if rd(x) == "":
        a = input("How should I reply you?" + "\n")
        ad(str(x).lower())
        ad(str(a))
        ad("\n")
        time.sleep(0.1)
        x = input("Ok, next time I'll say, " + str(a) + "\n")
    #Continues with the conversation
    else:
       time.sleep(0.1)
       x = input(rd(x) + "\n")
    #Replace vocabulary with new suggestion
    if x == "Replace":
        wd(input("After which input do you want to change? "),
            input("Which output do you want to replace? "),
            input("What do you want to replace it with? "))
