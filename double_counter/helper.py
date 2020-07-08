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

num_bits = 4
max_hum_add = 2
max_robot_add = 2

def int_to_bin(num, prefix, primed):
    ret = []
    str = format(num, "0{}b".format(num_bits))
    counter = 0
    for c in str:
        # print(prefix+c)
        if primed:
            ret.append(prefix+format(counter)+"'"+"="+c)
        else:
            ret.append(prefix+format(counter)+"="+c)
        counter = counter+1
    return ret

def int_to_bin_props(num, prefix, next):
    ret = []
    str = format(num, "0{}b".format(num_bits))
    counter = 0
    if next:
        for c in str:
            if c == '0':
                ret.append("!\""+prefix+format(counter)+"\"")
            else:
                ret.append("\""+prefix+format(counter)+"\"")
            counter = counter+1
    else:
        for c in str:
            if c == '0':
                ret.append("X !\""+prefix+format(counter)+"\"")
            else:
                ret.append("X \""+prefix+format(counter)+"\"")
            counter = counter+1        
    return ret