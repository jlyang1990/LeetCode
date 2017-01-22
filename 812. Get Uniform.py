#A method getRandom01Biased() that generates a random integer in [0, 1], where 0 is generated with probability p and 1 is generated with probability (1-p).
#A method getRandom06Uniform() that generates a random integer in [0, 6] with uniform probability.
#A method getRandomUniform(int a, int b) that generates a random integer in [a, b] with uniform probability.

def getUniform():
	while True:
		randNum1 = getRandom01Biased()
		randNum2 = getRandom01Biased()
		if randNum1 != randNum2:
			return randNum1


def getRandom06Uniform():
	while True:
		randNum1 = getUniform()
		randNum2 = getUniform()
		randNum3 = getUniform()
		result = (randNum1 << 2) + (randNum2 << 1) + randNum3
		if result != 7:
			return result


def getRandomUniform(a, b):
	numDigit = 0
	while (1 << numDigit) <= b-a:
		numDigit += 1
	while True:
		result = 0
		for i in range(numDigit):
			result += (getUniform() << i)
		if result <= b-a:
			return result+a