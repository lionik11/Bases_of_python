from itertools import count, cycle

my_list = []

for ael in count(3):
    if ael > 10:
        break
    else:
        # print(ael)
        my_list.append(ael)

print(my_list)

cycle_list = []
counter = 0
for el in cycle(my_list[4:6]):
    if counter > 15:
        break
    # print(el)
    cycle_list.append(el)
    counter += 1
print(cycle_list)
