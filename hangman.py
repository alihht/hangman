word = 'strings'
word_arr=[]
dash_word_array=[]
trys = len(word)+5
print("you have " + str(trys))
global u_input

def load_to_array():
    for i in word:
        word_arr.append(i)

def clone_arr():
    for _ in range(len(word_arr)):
        dash_word_array.append('_')

def user_input():
    global trys
    global u_input
    while (trys != 0):
        u_input=input()
        check_input()

def check_input():
    global trys
    global u_input
    k=[]
    #for i, j in zip(word_arr, range(len(word_arr))):
    if(trys != 0):
        if(u_input in word_arr):
            for n in range(len(word_arr)):
                if(word_arr[n] == u_input):
                    k.append(word_arr.index(u_input, n, len(word)))
            for j in k:
                dash_word_array[j] = u_input
            print(dash_word_array)
            print("you have " + str(trys))
            #break
        else:
            check_input2()
            #break

def check_input2():
    global trys
    global u_input
    #for i in word_arr:
    if(trys != 0):
    #print("Im in else")
        trys = trys - 1
        print("you have " + str(trys))
    #break


load_to_array()
clone_arr()
user_input()

