from collections import OrderedDict


od = OrderedDict()

od[1] = 3
od[4] = 12
od[5] = 34
od[6] = 53
od[2] = 45
od[1] = 5
od.update({1:634})
od.update({4:334})
od.update({5:324})
od.update({2:345})

for k, v in od.items():
    print(k, v)

