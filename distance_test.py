from Algorithms import Algorithms

algo = Algorithms()

algo.transform_dataset('pima.csv')

for example in algo.D:
    print(example)
