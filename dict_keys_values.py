''' generate a dictionary where the keys are numbers
between 1 and 20 (both included) and
the values are square of keys. '''


def gen_dict():
    d={}
    for i in range(1,21):
        d.update({i: i**2})
    return d
gen_dict()
