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