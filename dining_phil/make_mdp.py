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

import itertools

#   we have else, robot gripper, and the following locations for our states
num_phil = 10

print("mdp")
print("")
print("formula lfree = (p2>=0 & p2<=4) | p2=6 | p2=10;")
print("formula rfree = (p{}>=0 & p{}<=3) | p{}=5 | p{}=7 | p{}=11;".format(num_phil, num_phil, num_phil, num_phil, num_phil))
print("")
print("module phil1")
print("")
print(" p1 : [0..11] init 0;")
print("	[] p1=0 -> (p1'=1); // trying ")
print("	[] p1=1 -> 0.5 : (p1'=2) + 0.5 : (p1'=3); // draw randomly ")
print("	[] p1=2 &  lfree -> (p1'=4); // pick up left ")
print("	[] p1=3 &  rfree -> (p1'=5); // pick up right ")
print("	[] p1=4 &  rfree -> (p1'=8); // pick up right (got left) ")
print("	[] p1=4 & !rfree -> (p1'=6); // right not free (got left) ")
print("	[] p1=5 &  lfree -> (p1'=8); // pick up left (got right) ")
print("	[] p1=5 & !lfree -> (p1'=7); // left not free (got right) ")
print("	[] p1=6  -> (p1'=1); // put down left ")
print("	[] p1=7  -> (p1'=1); // put down right ")
print("	[] p1=8  -> (p1'=9); // move to eating (got forks) ")
print("	[] p1=9  -> (p1'=10); // finished eating and put down left  ")
print("	[] p1=9  -> (p1'=11); // finished eating and put down right ")
print("	[] p1=10 -> (p1'=0); // put down right and return to think ")
print("	[] p1=11 -> (p1'=0); // put down left and return to think ")

print("")
print("endmodule")

print("//// construct further modules through renaming")
for i in range(num_phil-1):
    i = i+2
    print("module phil{} = phil1 [ p1=p{}, p2=p{}, p{}=p{} ] endmodule".format(i, i, i+1, num_phil, i-1))


print("")
print("//// labels")
print("")
str = "((p1>0)&(p1<8))"
for i in range(num_phil):
    i=i+1
    str = str+"|((p{}>0)&(p{}<8))".format(i,i)
print("label \"hungry\" = "+ str + ";")

str = "((p1>=8)&(p1<=9))"
for i in range(num_phil-1):
    i=i+1
    str = str+"|((p{}>=8)&(p{}<=9))".format(i,i)
print("label \"eat\" = "+ str + ";")

for i in range(num_phil):
    i=i+1
    print("////philosopher {} is hungry".format(i))
    print("label \"hungry{}\" = (p{}>0)&(p{}<8);".format(i,i,i))

for i in range(num_phil):
    i=i+1
    print("////philosopher {} eats".format(i))
    print("label \"eat{}\" = (p{}>=8)&(p{}<=9);".format(i,i,i))
