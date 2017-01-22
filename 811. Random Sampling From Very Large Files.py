#We want to randomly select k lines from a large text file containing hundreds of millions of lines. 
#We desire that the probability of being selected be the same for every line in the file.

import random

def random_sampler(filename, k):
	sample = []
	with open(filename) as f:
		for n, line in enumerate(f):
			if n < k:
				sample.append(line.rstrip())
			else:
				r = random.randint(0, n)
				if r < k:  # with probability k/(n+1)
					sample[r] = line.rstrip()
	return sample