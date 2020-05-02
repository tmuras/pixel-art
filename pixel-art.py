import json

# At the beginning only 8x8 sprites.

white = "000000"
black = "FFFFFF"

step1 = [
[black,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white]
]

step2 = [
[black,black,white,white,white,white,white,white],
[white,black,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white]
]

step3 = [
[black,black,black,white,white,white,white,white],
[white,black,white,white,white,white,white,white],
[white,white,black,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white]
]

step4 = [
[black,black,black,black,white,white,white,white],
[white,black,white,white,white,white,white,white],
[white,white,black,white,white,white,white,white],
[white,white,white,black,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white]
]

step5 = [
[black,black,black,black,black,white,white,white],
[white,black,white,white,white,white,white,white],
[white,white,black,white,white,white,white,white],
[white,white,white,black,white,white,white,white],
[white,white,white,white,black,white,white,white],
[white,white,white,white,white,white,white,white],
[white,white,white,white,white,white,white,white]
]

step6 = [
[black,black,black,black,black,black,white,white],
[white,black,white,white,white,white,white,white],
[white,white,black,white,white,white,white,white],
[white,white,white,black,white,white,white,white],
[white,white,white,white,black,white,white,white],
[white,white,white,white,white,black,white,white],
[white,white,white,white,white,white,white,white]
]

step7 = [
[black,black,black,black,black,black,black,white],
[white,black,white,white,white,white,white,white],
[white,white,black,white,white,white,white,white],
[white,white,white,black,white,white,white,white],
[white,white,white,white,black,white,white,white],
[white,white,white,white,white,black,white,white],
[white,white,white,white,white,white,black,white]
]

step8 = [
[black,black,black,black,black,black,black,black],
[white,black,white,white,white,white,white,white],
[white,white,black,white,white,white,white,white],
[white,white,white,black,white,white,white,white],
[white,white,white,white,black,white,white,white],
[white,white,white,white,white,black,white,white],
[white,white,white,white,white,white,black,black]
]

# time in milliseconds
animation = [
    {'time':0,'data':step1},
    {'time':1000,'data':step2},
    {'time':2000,'data':step3},
    {'time':3000,'data':step4},
    {'time':4000,'data':step5},
    {'time':5000,'data':step6},
    {'time':6000,'data':step7},
    {'time':7000,'data':step8},
]
print(json.dumps(animation))