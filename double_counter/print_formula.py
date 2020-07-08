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