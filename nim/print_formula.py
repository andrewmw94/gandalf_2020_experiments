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

import random

stack_height = 200

atoms = []

for i in range(stack_height+1):
    atoms.append("\"x{}\"".format(i))

halt_prob = 0.9
prob_change=0.00

def generate_clause(clause_len):
    str = "("
    for i in range(clause_len):
        if random.random() < 1.1:
            if random.random() < 0.5:
                str = str + random.choice(atoms) + " & "
            else:
                str = str + random.choice(atoms) + " | "
        else:
            if random.random() < 0.5:
                str = str + "!" + random.choice(atoms) + " & "
            else:
                str = str + "!" + random.choice(atoms) + " | "        
        
    return str[:-3]+")"

def gen_temporal_op():
    if random.random() < 0.3:
        return "(X (!" + generate_clause(1) + "))"
    elif random.random() < 0.6:
        return "(G(!" + generate_clause(1) + "))"
    else:
        return "(F" + generate_clause(1) + ")"

str = ""
while random.random() < halt_prob:
    if random.random() < 0.5:
        str = str + gen_temporal_op() + " & "
    else:
        str = str + gen_temporal_op() + " | "
    halt_prob = halt_prob-prob_change

str = str[:-3]

print("Pmax =? [ (F(G !\"robotwin\")) & " +str+"];")
