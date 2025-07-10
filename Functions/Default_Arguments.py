# Types of Arguments 
# 1- Positional , 2- Default , 3- Keyword, 4- Arbitary

# def net_price(list_price, discount=0, tax=0.05):   # here discount and tax is initialized with default value because sometimes discount is not given and we assume it as zero
#     return list_price * (1-discount)* (1+tax)

# print(net_price(500))
# print(net_price(500,0.1))  # if there is a special discount then we can pass it from function
# print(net_price(500,0.1,0))  # if there customer doesn't pay any tax then tax=0


import time
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(30,15)