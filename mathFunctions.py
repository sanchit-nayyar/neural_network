class Maths():
	e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353

	@staticmethod
	def dot(a, b):
		if len(a) == len(b):
			sum = 0
			for ix in range(len(a)):
				sum += a[ix] * b[ix]
			return sum
		else:
			raise Exception("Size Of Arrays Is Different")

	@staticmethod
	def tanh(a):
		if isinstance(a, (int, float, long)):
			sinh = (Maths.e ** (2 * a)) - 1
			cosh = (Maths.e ** (2 * a)) + 1
			tanh = sinh / cosh
		else:
			raise Exception("Integer Required")
		return tanh

	@staticmethod
	def dtanh(a):
		if isinstance(a, (int, float, long)):
			dtanh = 1 - (tanh(a) ** 2)
		else:
			raise Exception("Integer Required")
		return dtanh

	@staticmethod
	def sigmoid(a):
		if isinstance(a, (int, float, long)):
			num = Maths.e ** a
			sigmoid = num / (num + 1)
		else:
			raise Exception("Integer Required")
		return sigmoid

	@staticmethod
	def dsigmoid(a):
		if isinstance(a, (int, float, long)):
			dsigmoid = Maths.sigmoid(a) * (1 - Maths.sigmoid(a))
		else:
			raise Exception("Integer Required")
		return dsigmoid

	@staticmethod
	def listProd(A, i):
		return [(t * i)  for t in A]

	@staticmethod
	def listAdd(A, B):
		return [A[x] + B[x]  for x in range(len(A))]

	@staticmethod
	def MSE(A, B):
		E = 0.0
		for i in xrange(len(A)):
			E += (A[i] - B[i]) ** 2
		return E / len(A)

	@staticmethod
	def ArrDiff(A, B):
		return [A[x] - B[x]  for x in range(len(A))]

	@staticmethod
	def ArrProd(A, B):
		return [A[x] * B[x]  for x in range(len(A))]

	@staticmethod
	def eTotal(A, B): # A: Actual, B: Target
		E = 0.0
		for i in xrange(len(A)):
			E += (A[i] - B[i]) ** 2
		return E / 2