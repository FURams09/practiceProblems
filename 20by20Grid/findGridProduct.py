
GRID_FILENAME = "numbergrid.txt"

def gridToLists():
        gridFile = open(GRID_FILENAME, 'r')
        gridList = []

        for line in gridFile:
                gridList.append(line.split('/n'))
        for row in range(len(gridList)):
                gridList[row]= gridList[row][0].split(' ')
        return gridList

def getMaxRow(numGrid):
        testProduct = 0
        bestProduct = []
        for i in range(len(numGrid)):
                for j in range(len(numGrid[i]) - 3):
                        testRow = numGrid[i]
                        testProduct = int(testRow[j]) * int(testRow[j+1]) * int(testRow[j+2]) * int(testRow [j+3])
                        bestProduct = isNewMax(bestProduct, testProduct, [i, j], [i, j+3])
        return bestProduct

def getMaxColumn(numGrid):
        bestProduct = []
        testProduct = 0
        for i in range(len(numGrid) - 3):
                for j in range(len(numGrid[i])):
                        testProduct = int(numGrid[i][j]) * int(numGrid[i+1][j]) * int(numGrid[i+2][j]) * int(numGrid [i+3][j])
                        bestProduct = isNewMax(bestProduct, testProduct, [i, j], [i+3, j])
        return bestProduct
def getMaxDiag(numGrid):
        testProduct = 0
        bestProduct = []
        for i in range(len(numGrid) - 3):
                for j in range(len(numGrid[i])):
                        #test from point[i, j] down and to the right
                        if (j + 4) <= len(numGrid[i]):
                                testProduct = int(numGrid[i][j]) * int(numGrid[i+1][j+1]) * int(numGrid[i+2][j+2]) * int(numGrid [i+3][j+3])
                                bestProduct = isNewMax(bestProduct, testProduct, [i, j], [i+3, j+3])
                        if (j-3) >= 0: #test from point i, j down and to the left
                                testProduct = int(numGrid[i][j]) * int(numGrid[i+1][j-1]) * int(numGrid[i+2][j-2]) * int(numGrid [i+3][j-3])
                                bestProduct = isNewMax(bestProduct, testProduct, [i, j], [i+3, j-3])
        return bestProduct

        
def isNewMax(oldMax, testMax, startPosition, endPosition):
        if oldMax == [] or testMax > oldMax[0]:
                return [testMax, startPosition, endPosition ] #returns a list of the product, the start position and the end position (giving us direction)
        else:
                return oldMax
        
def findGridProducts():
        numberGrid = gridToLists()
        testMax = 0
        bestMaxRow = getMaxRow(numberGrid)
        bestMaxColumn = getMaxColumn(numberGrid)
        bestMaxDiag = getMaxDiag(numberGrid)

        if bestMaxRow > bestMaxColumn:
                if bestMaxRow > bestMaxDiag:
                        print 'Max Row is best' + str(bestMaxRow[0])
                else:
                        print 'MaxDiag is best' + str(bestMaxDiag[0])
        elif bestMaxColumn > bestMaxDiag:
                print 'MaxColumn is best' + str(bestMaxColumn[0])
        else:
                print 'MaxDiag is best' + str(bestMaxDiag[0])

