from helper import num_bits, max_robot_add, int_to_bin_props


adder_formula = ""
for i in range(2**num_bits):
    l = int_to_bin_props(i, "p", False)
    str = "(!( "
    for s in l:
        str = str + "(" + s +") & "
    str = str[:-3]
    str = str + " ) | ( ("
    for j in range(max_robot_add):
        res = (i+j) % (2**num_bits)
        l = int_to_bin_props(res, "p", True)
        for s in l:
            str = str + "(" + s +") & "
        str = str[:-3] + " ) | ("
    str = str[:-4] + ")) & "
    adder_formula = adder_formula + str
adder_formula = adder_formula[:-3]

# goal_formula = ""
# for i in range(num_bits):
#     goal_formula = goal_formula + "(x{} = y{}) & ".format(i,i)
# goal_formula = goal_formula[:-3]

# formula = "(G("+adder_formula+")) & (F("+goal_formula+"))"

formula = "(G("+adder_formula+")) & (F(\"robotturnwin\" | \"humanturnwin\"))"


print("Pmax =? [" + formula + "];")