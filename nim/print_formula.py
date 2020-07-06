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
