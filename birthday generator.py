'''
Generate a broup of people with random birthdays multiple times
Final result is a csv file with propabilities of repeating birthdays
'''
import numpy as np

iterations = 1
population = 10
days  = 5

raw =  np.zeros((population-1,population-1))

for i in range(iterations):
	print(i)
	single = np.random.randint(1,high=days+1,size=population)
	print(single)

	for k in range(1,population):
		#print('pop',k+1)
		#print(single)
		unique,counts = np.unique(single[:k+1], return_counts=True)
		#print(list(zip(unique,counts)))
		#print('------')
		repeats,quant  = np.unique(counts,return_counts=True)
		#print('all:',list(zip(repeats,quant)))

		if 1 in repeats:
			#https://www.codegrepper.com/code-examples/swift/numpy+find+index+of+value
			#print(repeats)
			repeats = np.delete(repeats,0)
			quant = np.delete(quant,0)
		#print('duplicates:',list(zip(repeats,quant)))
		for r, q in zip(repeats,  quant):
			#print(f'duplicates: {r}')
			#print(f'how offen: {q}')
			#print(k-1,r-2)
			raw[k-1,r-2] += q
			#print(raw)
		#print('---------------------------------')
print(raw)
raw = np.true_divide(raw,iterations)
raw = np.around(raw,4)
np.savetxt("Simple Birthday1.csv", raw, delimiter=",")