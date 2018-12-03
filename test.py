from arithmatics import randVals
from csvReader import CSV
from mathFunctions import Maths



def makeNetwork(csv, dim):
	n = len(dim)
	generator = randVals(0, 100)
	if dim[0] != len(csv.getHeads()) - 1:
		raise Exception('Dimensions first value should be class size')
		return
	
	nodes = [([0] * n) for n in dim]
	sumVals = [([0] * n) for n in dim]
	xtrain, xtest, ytrain, ytest = csv.getTrainTestData()

	weights = []
	for i in xrange(len(dim) - 1):
		weights.append([0] * (dim[i] * dim[i + 1]))

	for i in xrange(len(weights)):
		for j in xrange(len(weights[i])):
			weights[i][j] = generator.getNext(i * j + (2.0 / (j + 1)) - i)
			weights[i][j] /= 100.0

	mse = 0

	for eta in xrange(10):
		for row_id in xrange(len(xtrain)):
			nodes[0] = [float(t) for t in xtrain[row_id]]
			sumVals[0] = [float(t) for t in xtrain[row_id]]
			expected = xtest[row_id]
			expected = [int(expected == 'Iris-setosa'), int(expected == 'Iris-virginica'), int(expected == 'Iris-versicolor')]
			for i in xrange(len(nodes[1])):
				p = 0
				for j in xrange(len(nodes[0])):
					p += nodes[0][j] * weights[0][(i * len(nodes[0])) + j]
				nodes[1][i] = Maths.tanh(p)
				sumVals[1][i] = p

			for i in xrange(len(nodes[2])):
				p = 0
				for j in xrange(len(nodes[1])):
					p += nodes[1][j] * weights[1][(i * len(nodes[1])) + j]
				nodes[2][i] = Maths.sigmoid(p)

			mse = Maths.MSE(nodes[2], expected)
			eTotal = Maths.eTotal(nodes[2], expected)

			detotal_dout = []

			for i in xrange(len(weights[1])):
				act = nodes[2][i % len(nodes[2])]
				exp = expected[i % len(nodes[2])]

				detotal_dw = (act - exp) * act * (1 - act) * nodes[1][i / len(nodes[2])]
				weights[1][i] -= detotal_dw
				detotal_dout.append(act - exp)


			for i in xrange(len(weights[0])):
				layer_0_node = i / len(nodes[1])
				layer_1_node = i % len(nodes[1])
				de_dout = 0
				for layer_2_node in xrange(len(nodes[2])):
					corresponding_weight_index = (layer_1_node * len(nodes[2])) + layer_2_node
					corresponding_weight = weights[1][corresponding_weight_index]
					out = nodes[2][layer_2_node]
					exp = expected[layer_2_node]
					de_dout += (exp - out) * out * (1 - out) * corresponding_weight
				dout_dnet = nodes[1][layer_1_node] * (1 - nodes[1][layer_1_node])
				dnet_dw = nodes[0][layer_0_node]
				weights[0][i] -= (de_dout * dout_dnet * dnet_dw)

		print mse










DIMS = [4, 5, 3]
reader = CSV('iris.csv')
reader.setY_Col(4)
reader.generateTrainTestCols(0.7)

makeNetwork(reader, DIMS)

# 4 5 3