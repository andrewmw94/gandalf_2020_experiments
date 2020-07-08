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

stack_height = 200
pieces_per_turn = 3

print_LTL_game = True

print("mdp")
print("")
print("global x : [0..{}] init {};".format(stack_height+1, stack_height))
print("global rt : [0..1] init 1;")
print("")
print("module robot")
print("")
print("[] (x=0) & (rt=1) -> 1: (x'=0) & (rt'=1);")
for i in range(1,stack_height+1):
    for j in range(1,pieces_per_turn+1):
        if i-j <= 0:
            print("[] (x={}) & (rt=1) -> 1: (x'=0) & (rt'=1);".format(i))
        else:
            print("[] (x={}) & (rt=1) -> 1: (x'={}) & (rt'=0);".format(i, i-j))

if print_LTL_game:
    for i in range(stack_height+2):
        print("[] (x={}) & (rt=1) -> 1: (x'={}) & (rt'=1);".format(i, stack_height+1))
        print("[] (x={}) & (rt=0) -> 1: (x'={}) & (rt'=1);".format(i, stack_height+1))

print("")
print("endmodule")

print("")
print("module human")
print("")
print("[] (x=0) & (rt=0) -> 1: (x'=0) & (rt'=0);")
for i in range(1,stack_height+1):
    str = "[] (x={}) & (rt=0) ->".format(i)
    for j in range(1,pieces_per_turn+1):
        if i-j <= 0:
            str = str + " {}: (x'={}) & (rt'=0) + ".format(1.0/pieces_per_turn, 0)
        else:
            str = str + " {}: (x'={}) & (rt'=1) + ".format(1.0/pieces_per_turn, i-j)
    print(str[:-3]+";")

print("")
print("endmodule")
print("")
print("label \"robotwin\" = (x=0) & (rt=0);")
print("label \"humanwin\" = (x=0) & (rt=1);")

for i in range(1,stack_height+1):
    print("label \"x{}\" = (x={});".format(i,i))

if print_LTL_game:
    print("label \"done\" = (x={});".format(stack_height+1))