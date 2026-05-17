import cleaner as cl
import json
import pandas as pd
import re
from numpy import random
import math as mm
def absolute(x):
    if x>=0:
        return x
    if x<0:
        return -1*x
def res_func1(words_p):
    beta,c = 2,1.3 
    L = beta * (words_p * c)
    return L
def res_func2(words_p):
    k = 5
    return k*(mm.log(words_p+1))
def res_func(words_p):
    words_p = int(words_p)
    if words_p==0:
        words_p = words_p+1
        pass

    if words_p>=10:
        return int(2.3*(words_p))
    elif words_p<=67 and words_p >= 11:
        return int(res_func1(words_p))
    else:
        return int(res_func2(words_p))
i=0
while i<i+1:
    t2w = cl.t2w
    user_input = input("Type :")
    user_input = user_input.lower()
    if user_input == "leave" or user_input=="chat":
        break
    else:
        pass
    print("Typing...")
    #user_input = "Hi"
    cl.token_append(user_input)
    data = cl.token_append(user_input)
    #cl.transistor(data)
    cl.transistor(user_input)
    result = []
    with open("transition.json", 'r') as f:
        our_dict = json.load(f)
        for i in range(len(data)):
            first_choices = our_dict.get(str(data[i]))
            if first_choices:
                a = t2w[int(random.choice(first_choices))]
                for j in range(random.choice([random.randint(1,5),int((0.5*len(a))/len(data))+1])):
                    key_a = str(a)
                    next_options = our_dict.get(key_a)
                    if next_options:
                        result.append(a)
                        a = t2w[int(random.choice(next_options))]
                    else:
                        break
    #del("Typing...")
    if len(data)==1:
        print(" ".join(result)+".")
    else:
        print(" ".join(result)+".")
    i += 1