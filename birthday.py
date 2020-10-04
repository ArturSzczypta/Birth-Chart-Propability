import numpy as np


iterations = 10
population = 10
days  = 5


raw =  np.zeros((days,population))
#print(raw)

for i in range(iterations):
	print(i)
	single = np.random.randint(1,high=days+1,size=population)
	#print(single)

	for k in range(population):
		#print('pop',k)
		unique,counts = np.unique(single[:k+1], return_counts=True)

		for u, c in zip(unique,counts):
			#print(f'Letter: {u}')
			#print(f'Number: {c}')
			raw[u-1][k] += c
			#print(u,k)
		#print('---')
print(raw)
