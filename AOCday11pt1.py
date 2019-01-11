



def genBoxVal(gridvalue):

    boxes = {}
    for x in range(220):
        for y in range(220):
            boxname = (x,y)

            boxcalc1 = x+10
            boxcalc2 = boxcalc1*y
            boxcalc3 = boxcalc2+gridvalue
            boxcalc4 = boxcalc3*boxcalc1
            boxvalue = int((boxcalc4 / 100) % 10) - 5

            boxes[boxname] = boxvalue

    return boxes


def genGridVal(boxset):
    pass


boxset = genBoxVal(71)

values = 0


print("box value:", boxset[101, 153])