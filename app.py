import numpy as np

def hard_limiter(u):        #hard limit activation function (step function)
    if u < 0:
        y_pred = 0
        return y_pred


def model(input, weight, bias):          #Perceptron Model    
	y = np.dot(weight, input) + bias
	y = hard_limiter(y)
	return y

##OR Logic Function
def or_logic(input, y_pred):        #initially w1 = 0 , w2 = 0 , bias = -0.2
    w1 = 0
    w2 = 0
    weight = np.array([w1, w2])
    bias = -0.2
    Y_true = [0,1]  
    Y_pred = [y_pred, y_pred]  
    error = np.square(np.subtract(Y_true,Y_pred)).mean()
    print(error)
    return model(input, weight, bias)

# testing the Perceptron Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])

desired1 = 0
desired2 = 1
desired3 = 0
desired4 = 0
"""
out1 = or_logic(test1)
out2 = or_logic(test2)
out3 = or_logic(test3)
out4 = or_logic(test4)

"""

#if desired1 == out1 
"""
print("OR({}, {}) = {}".format(0, 1, or_logic(test1)))
print("OR({}, {}) = {}".format(1, 1, or_logic(test2)))
print("OR({}, {}) = {}".format(0, 0, or_logic(test3)))
print("OR({}, {}) = {}".format(1, 0, or_logic(test4)))
"""

#if out1 = 

#def updating_weights(test2):



