def c_to_f(temp):
    return (temp * 9/5)+32
c_temps =[0, 12, 34, 100]
f_temps =map(c_to_f, c_temps)
for temp in f_temps:
    print(temp)