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

def genGridVal(boxset):

    gridSum = {}


    for i in range(299):
        for j in range(299):
            cellSum = 0

            cellSum += boxset[(i, j)]
            cellSum += boxset[(i, j+1)]
            cellSum += boxset[(i, j+2)]
            cellSum += boxset[(i+1, j)]
            cellSum += boxset[(i+1, j+1)]
            cellSum += boxset[(i+1, j+2)]
            cellSum += boxset[(i+2, j)]
            cellSum += boxset[(i+2, j+1)]
            cellSum += boxset[(i+2, j+2)]
            gridSum[(i,j)] = cellSum

    maxVal = max(gridSum, key=lambda key: gridSum[key])

    return gridSum, maxVal



boxset = genBoxVal(18)
gridSum, maximum = genGridVal(boxset)

print(maximum)
print(gridSum[maximum])