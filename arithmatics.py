class randVals:
	randVal = 8
	mVal = 0
	MVal = 9
	def __init__(self, minV, maxV):
		self.mVal = minV
		self.MVal = maxV

	def getNext(self, seed):
		self.randVal = self.randVal * 7 + (seed ** 2.5) * 23 + 19
		self.randVal = self.randVal % (self.MVal - self.mVal)
		self.randVal += self.mVal
		self.randVal = int(self.randVal)
		return self.randVal

	def shuffle(self, A):
		n = len(A)
		B = []
		for i in xrange(n):
			self.mVal = 0
			self.MVal = len(A)
			self.getNext(3 * i)
			B.append(A[self.randVal])
			A.pop(self.randVal)
		return B