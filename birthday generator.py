'''
Generate a broup of people with random birthdays multiple times
Final result is a csv file with propabilities of repeating birthdays
'''
import numpy as np

ITERATIONS = 1 # How many times repeat
POPULATION = 10
DAYS = 4

output_array =  np.zeros((POPULATION-1,POPULATION-1))

for i in range(ITERATIONS):
    single_iter = np.random.randint(1,DAYS+1,size=POPULATION)

    #Using np.nique twice outputs how often there are repeats
    for person in range(1,POPULATION):
        unique,counts = np.unique(single_iter[:person+1], return_counts=True)
        repeats,quant  = np.unique(counts,return_counts=True)
        
        # Delete single occurences
        if 1 in repeats:
            repeats = np.delete(repeats,0)
            quant = np.delete(quant,0)
        for r, q in zip(repeats, quant):
            output_array[person-1,r-2] += q
print(output_array)
output_array = np.true_divide(output_array,ITERATIONS)
output_array = np.around(output_array,4)
np.savetxt("Simple Birthday1.csv", output_array, delimiter=",")