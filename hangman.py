word = 'string'
word_arr=[]
dash_word_array=[]
count=0
global u_input

def load_to_array():
    for i in word:
        word_arr.append(i)

def clone_arr():
    for i in range(len(word_arr)):
        dash_word_array.append('_')

def user_input():
    global u_input
    for i in range(len(word)):
        u_input=input()
        check_input()

def check_input():
    global u_input
    for i, j in zip(word_arr, range(len(word_arr))):
        if(u_input == i):
            dash_word_array[j] = i
            print(dash_word_array)

load_to_array()
clone_arr()
user_input()

