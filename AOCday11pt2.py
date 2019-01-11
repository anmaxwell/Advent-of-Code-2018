def genBoxVal(gridvalue):

    boxes = {}
    for x in range(301):
        for y in range(301):
            boxname = (x,y)

            boxcalc1 = (x+10)
            boxcalc2 = boxcalc1*y
            boxcalc3 = boxcalc2+gridvalue
            boxcalc4 = boxcalc3*boxcalc1
            boxvalue = int((boxcalc4 / 100) % 10) - 5

            boxes[boxname] = boxvalue

    return boxes

def genGridVal(boxset, size):

    gridSum = {}


    for i in range(299):
        for j in range(299):
            cellSum = 0

            for k in range(size):
                for l in range(size):
                    if j+k >= 300 or i+l >= 300:
                        break

                    else:
                        cellSum += boxset[(i+l, j+k)]
                        gridSum[(i,j)] = cellSum

    maxVal = max(gridSum, key=lambda key: gridSum[key])

    return gridSum, maxVal


boxset = genBoxVal(8868)

for i in range(1,300):
    gridSum, maximum = genGridVal(boxset, i)
    print(i, maximum)
    print(gridSum[maximum])