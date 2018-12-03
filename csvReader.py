from arithmatics import randVals

class CSV:
	filePath = ''
	fstream = None
	heads = []
	rows = []
	x_vals = []
	y_vals = []
	y_index = -1

	xTrain = []
	xTest = []
	yTrain = []
	yTest = []

	def __init__(self, path):
		self.filePath = path
		self.generateHeads()
		self.generateRows()

	def generateHeads(self):
		self.fstream = open(self.filePath)
		self.heads = self.fstream.read().split('\n')[0].split(',')
		self.fstream.close()

	def generateRows(self):
		self.fstream = open(self.filePath)
		for row in self.fstream.read().split('\n')[1:-1]:
			self.rows.append(row.split(','))
		self.fstream.close()

	def setY_Col(self, index):
		self.y_index = index
		self.y_vals = []
		self.x_vals = []
		for row in self.rows:
			self.x_vals.append([])
			for i in xrange(len(row)):
				if i == index:
					self.y_vals.append(row[i])
				else:
					self.x_vals[-1].append(row[i])

	def generateTrainTestCols(self, trainSize):
		if self.y_index == -1:
			raise Exception('Cannot execute Generate Train Test Cols without setting Y Col first.\nUse setY_Col(self, index)')

		trainCount = int(float(trainSize) * len(self.rows))
		randomGenerator = randVals(0, len(self.rows))
		self.rows = randomGenerator.shuffle(self.rows)
		self.setY_Col(self.y_index)
		self.xTrain = self.x_vals[0:trainCount]
		self.yTrain = self.y_vals[0:trainCount]
		self.xTest = self.x_vals[trainCount:]
		self.yTest = self.y_vals[trainCount:]


	def getHeads(self):
		return self.heads

	def getRows(self):
		return self.rows

	def getTrainTestData(self):
		return self.xTrain, self.yTrain, self.xTest, self.yTest

	def getCol(self, index):
		return [row[index] for row in self.rows]

	def getTrainCol(self, index):
		if self.y_index == -1:
			raise Exception('Set X and Y Cols first')
		return [row[index] for row in self.xTrain]

	def getTestCol(self, index):
		if self.y_index == -1:
			raise Exception('Set X and Y Cols first')
		return [row[index] for row in self.xTest]