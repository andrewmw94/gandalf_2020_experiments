from helper import num_bits, max_hum_add, int_to_bin

print_LTL_game=True

print("mdp")
print("")
for i in range(num_bits):
    print("global x{} : [0..1] init 0;".format(i))
for i in range(num_bits):
    print("global y{} : [0..1] init 0;".format(i))
print("global rt : [0..1] init 1;")
print("global gamedone : [0..1] init 0;")

print("")
print("module robot")
print("")
# print("[] (x=0) & (rt=1) -> 1: (x'=0) & (rt'=1);")
if not print_LTL_game:
    for i in range(num_bits):
        print("[] (x{}=0) & (rt=1) -> 1: (x{}'=0) & (rt'=0);".format(i,i))
        print("[] (x{}=0) & (rt=1) -> 1: (x{}'=1) & (rt'=0);".format(i,i))
        print("[] (x{}=1) & (rt=1) -> 1: (x{}'=0) & (rt'=0);".format(i,i))
        print("[] (x{}=1) & (rt=1) -> 1: (x{}'=1) & (rt'=0);".format(i,i))
    print("")
else:
    for i in range(num_bits):
        print("[] (x{}=0) & (rt=1) & (gamedone=0) -> 1: (x{}'=0) & (rt'=0) & (gamedone'=0);".format(i,i))
        print("[] (x{}=0) & (rt=1) & (gamedone=0) -> 1: (x{}'=1) & (rt'=0) & (gamedone'=0);".format(i,i))
        print("[] (x{}=1) & (rt=1) & (gamedone=0) -> 1: (x{}'=0) & (rt'=0) & (gamedone'=0);".format(i,i))
        print("[] (x{}=1) & (rt=1) & (gamedone=0) -> 1: (x{}'=1) & (rt'=0) & (gamedone'=0);".format(i,i))
        print("[] (x{}=0) & (rt=1) & (gamedone=0) -> 1: (x{}'=0) & (rt'=1) & (gamedone'=1);".format(i,i))
        print("[] (x{}=0) & (rt=1) & (gamedone=0) -> 1: (x{}'=1) & (rt'=1) & (gamedone'=1);".format(i,i))
        print("[] (x{}=1) & (rt=1) & (gamedone=0) -> 1: (x{}'=0) & (rt'=1) & (gamedone'=1);".format(i,i))
        print("[] (x{}=1) & (rt=1) & (gamedone=0) -> 1: (x{}'=1) & (rt'=1) & (gamedone'=1);".format(i,i))
    print("")
    print("[] (gamedone=1) & (rt=0) -> 1: (gamedone'=1) & (rt'=1);")
    print("[] (gamedone=1) & (rt=1) -> 1: (gamedone'=1) & (rt'=1);")
    print("")
print("endmodule")

print("")
print("module human")
print("")
for i in range(2**num_bits):
    l = int_to_bin(i, "y", False)
    str = "[] "
    for s in l:
        str = str + "(" + s +") & "
    str = str + " (rt=0) ->".format(i)
    for j in range(max_hum_add):
        res = (i+j) % (2**num_bits)
        str = str + " {}: ".format(1.0/max_hum_add)
        l = int_to_bin(res, "y", True)
        for s in l:
            str = str + "(" + s +") & "
        str = str + " (rt'=0) + "
    print(str[:-3]+";")
print("")
print("endmodule")
print("")

for i in range(num_bits):
    print("label \"p{}\" = (x{} = 1);".format(i,i))
# print("label \"robotwin\" = (x=0) & (rt=0);")
# print("label \"humanwin\" = (x=0) & (rt=1);")

# for i in range(1,stack_height+1):
#     print("label \"x{}\" = (x={});".format(i,i))

str = ""
for i in range(num_bits):
    str = str + "(x{}=y{}) & ".format(i,i)
print("label \"robotturnwin\" = "+str+"(rt=1);")
print("label \"humanturnwin\" = "+str+"(rt=0);")


if print_LTL_game:
    print("label \"done\" = (gamedone=1);")