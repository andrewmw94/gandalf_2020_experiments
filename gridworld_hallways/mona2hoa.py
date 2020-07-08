# MIT License

# Copyright (c) 2020 Andrew Wells

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys
import itertools

def convertMONAStringToHOA(str):
    out_str = ""
    for i in range(len(str)):
        if str[i] == "1":
            out_str = out_str + "{}& ".format(i)
        elif str[i] == "0":
            out_str = out_str + "!{}& ".format(i)
        elif str[i] == "X":
            out_str = out_str
        elif str[i] == " ":
            pass
        else:
            print("Error")

    return out_str[:-2]

def assgnToStr(bitList):
    out_str = ""
    for i in range(len(bitList)):
        if bitList[i] == 1:
            out_str = out_str + "{}& ".format(i)
        elif bitList[i] == 0:
            out_str = out_str + "!{}& ".format(i)
    return out_str[:-2]

def getAssgnDest(state_index, assgn, t_start, t_label, t_dest):
    ass = assgn
    for i in range(len(t_start)):
        if(t_start[i] == state_index):
            for j in range(len(ass)):
                if(ass[j] == 1 and t_label[i][j] == "0"):
                    break
                elif(ass[j] == 0 and t_label[i][j] == "1"):
                    break
                if(j == len(ass)-1):
                    return t_dest[i]

def convertMONAStateTransitionsToHOA(state_index, t_start, t_label, t_dest, num_AP, final_index, num_states):
    lst = list(itertools.product([0, 1], repeat=num_AP))
    if(state_index == final_index):
        for assgn in lst:
            print("[ {} ] {}".format(assgnToStr(assgn), final_index))
    else:
        for assgn in lst:
            #we need to deal with negated variables from PRISM
            #for now we assume the last bit is the negated one
            assgn_fixed = list(assgn[:-1])
            if(assgn[num_AP-1] == 1):
                assgn_fixed.append(0)
            else:
                assgn_fixed.append(1)
            print("[ {} ] {}".format(assgnToStr(assgn_fixed), getAssgnDest(state_index, assgn, t_start, t_label, t_dest)))

        #acceping state is num_states
        # if(state_index == final_index):
        #     print("[ {}& !{} ] {}".format(assgnToStr(assgn), num_AP, num_states))
        # else:
        #     print("[ {}& !{} ] {}".format(assgnToStr(assgn), num_AP, num_states+1))

# #accept state is num_states
# def addAcceptState(num_AP, num_states):
#     print("State: {}".format(num_states) + " { 0 }")
#     lst = list(itertools.product([0, 1], repeat=num_AP+1))
#     for assgn in lst:
#         print("[ {} ] {}".format(assgnToStr(assgn), num_states))

# #reject state is num_states+1
# def addRejectState(num_AP, num_states):
#     print("State: {}".format(num_states+1))
#     lst = list(itertools.product([0, 1], repeat=num_AP+1))
#     for assgn in lst:
#         print("[ {} ] {}".format(assgnToStr(assgn), num_states+1))

f=open(sys.argv[1], "r")
flines=f.readlines()

num_states = -1
num_AP = -1
AP_string = ""
start_state = -1
final_state = -1

transition_start = [] #ints
transition_label = [] #strings
transition_dest = [] #ints

for l in flines:
    if(l.startswith("State ")):
        transition_start.append(int(l[5:l.find(":")]))
        transition_label.append(l[l.find(": ")+2: l.find("->")-1])
        transition_dest.append(int(l[l.find("-> state")+8:-1]))
    elif(l.startswith("DFA for formula with free variables: ")):
        AP_string = l[37:-1] # I think this only removes the newline
        num_AP = len(AP_string.split())
    elif(l.startswith("Automaton has ")):
        num_states = int(l[13: 14+l[14:].find(" ")])
    elif(l.startswith("Initial state: ")):
        #start_state = l[14: l[15:].find(" ")]
        start_state = int(l[14:])
    elif(l.startswith("Accepting states: ")):
        #final_state = l[17: l[18:].find(" ")]
        final_state = int(l[17:])
    else:
        pass
        # print("can't parse: ")
        # print(l)

print("HOA: v1")
print("States: {}".format(num_states))
print("AP: {} {}".format(num_AP, AP_string))
print("Start: {}".format(start_state))
print("acc-name: Buchi")
print("Acceptance: 1 Inf(0)")
print("properties: trans-labels explicit-labels state-acc no-univ-branch deterministic")
print("--BODY--")
j = 0
for i in range(num_states):
    if(i == final_state):
        print("State: {}".format(i) + " { 0 } ")
    else:
        print("State: {}".format(i))

    convertMONAStateTransitionsToHOA(i, transition_start, transition_label, transition_dest, num_AP, final_state, num_states)

# addAcceptState(num_AP, num_states)
# addRejectState(num_AP, num_states)


    # while(j < len(transition_start) and transition_start[j] == i):
    #     print("[{}] {}".format(convertMONAStringToHOA(transition_label[j]), transition_dest[j]))
    #     j = j+1

#print("State: {}".format(s_num))
#print("[{}] {}".format(edge_label, edge_dest))
print("--END--")
