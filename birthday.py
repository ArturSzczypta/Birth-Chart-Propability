import numpy as np


iterations = 1
population = 5
days  = 5


raw =  np.zeros((population,population))
#print(raw)

for i in range(iterations):
	print(i)
	single = np.random.randint(1,high=days+1,size=population)
	print(single)

	for k in range(population):
		#print('pop',k)
		unique,counts = np.unique(single[:k+1], return_counts=True)
		print(list(zip(unique,counts)))
		print('---')
		repeats,quant  = np.unique(counts,return_counts=True)
		print(list(zip(repeats,quant)))
		for r, q in zip(repeats,  quant):
			#print(f'Letter: {u}')
			#print(f'Number: {c}')
			if q > 1:
				raw[r-1][k] += q
			#print(u,k)
		#print('---')
		print('----------')
print(raw)
