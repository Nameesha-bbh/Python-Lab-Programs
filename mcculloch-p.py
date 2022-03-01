w1_weights = [-1,1]
w2_weights = [-1,1]
threshold_weights = [-2,-1,0,1,2]


class mcculloch:
    
    def __init__(self,input_matrix):
        self.input_matrix = input_matrix

    def iterate_all_values(self):
        for w1 in w1_weights:
            self.w1 = w1
            for w2 in w2_weights:
                self.w2 = w2
                for threshold in threshold_weights:
                    self.threshold = threshold
                    
                    if self.checkCombination():
                        return True
        return False
    
    def checkCombination(self):
        valid = True
        for (x1,x2,y) in self.input_matrix:
            if not self.compare_target(x1,x2,y):
                valid = False
        return valid

    def compare_target(self,x1,x2,y):
        if self.neuron_activate(x1,x2) == y:
            return True
        return False
    
    def neuron_activate(self,x1,x2):
        output = self.w1*x1 + self.w2*x2
        if output >= self.threshold:
            return 1
        return 0
        
        
def neuron_calculate(neuron):
    if neuron.iterate_all_values():
        print("weights - {} {} and threshold-{}".format(neuron.w1,neuron.w2,neuron.threshold))
    else:
        print("CANNOT")


AND_Matrix = [
    [-1, -1, 0],
    [-1,  1, 0],
    [ 1, -1, 0],
    [ 1,  1, 1],
]

OR_Matrix = [
    [-1, -1, 0],
    [-1,  1, 1],
    [ 1, -1, 1],
    [ 1,  1, 1],
]

NAND_Matrix = [
    [-1, -1, 1],
    [-1,  1, 1],
    [ 1, -1, 1],
    [ 1,  1, 0],
]

XOR_Matrix = [
    [-1, -1, 0],
    [-1,  1, 1],
    [ 1, -1, 1],
    [ 1,  1, 0],
]


or_mc = mcculloch(OR_Matrix)
and_mc = mcculloch(AND_Matrix)
xor_mc = mcculloch(XOR_Matrix)
nand_mc = mcculloch(NAND_Matrix)
neuron_calculate(or_mc)
neuron_calculate(and_mc)
neuron_calculate(xor_mc)
neuron_calculate(nand_mc)