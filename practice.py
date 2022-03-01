possible_w1_values = [-1,1] 
possible_w2_values = [-1,1]
possible_threshold_values = [-2,-1,0,1,2]

class MCP:
    def __init__(self,inputMatrix):
        self.inputMatrix = inputMatrix
        
    def iterateAllValues(self):
        for w1 in possible_w1_values:
            self.w1 = w1
            for w2 in possible_w2_values:
                self.w2 = w2
                for threshold in possible_threshold_values:
                    self.threshold = threshold
                    
                    if self.checkCombination():
                        return True
        return False
                    
    def checkCombination(self):
        valid = True
        for (x1,x2,y) in self.inputMatrix:
            if not self.resultTarget(x1,x2,y):
                return False
        return valid
    
    def resultTarget(self,x1,x2,target):
        if self.neuronActivate(x1,x2) == target:
            return 1
        return 0
    
    def neuronActivate(self,x1,x2):
        if x1*self.w1 + x2*self.w2 >= self.threshold:
            return 1
        return 0


def findValues(mc):
    if mc.iterateAllValues():
        print("Threshold : {} , weight1 : {} , weight2 : {}".format(mc.threshold, mc.w1, mc.w2))
    else:
        print("NOT LINEARLY SEPERABLE")
        return 

OR_MATRIX = [[-1,-1,0],[-1,1,1],[1,-1,1],[1,1,1]]
AND_MATRIX = [[-1,-1,0],[-1,1,0],[1,-1,0],[1,1,1]]
NAND_MATRIX = [[-1,-1,1],[-1,1,1],[1,-1,1],[1,1,0]]
XOR_MATRIX = [[-1,-1,0],[-1,1,1],[1,-1,1],[1,1,0]]

OR_MCP = MCP(OR_MATRIX)
print("------OR GATE-------")
findValues(OR_MCP)
print("--------------------")

AND_MCP = MCP(AND_MATRIX)
print("------AND GATE-------")
findValues(AND_MCP)
print("--------------------")

NAND_MCP = MCP(NAND_MATRIX)
print("------NAND GATE-------")
findValues(NAND_MCP)
print("--------------------")

XOR_MCP = MCP(XOR_MATRIX)
print("------XOR GATE-------")
findValues(XOR_MCP)
print("--------------------")