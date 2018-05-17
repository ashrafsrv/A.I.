# Algorithms.py: atom://teletype/portal/1560ee10-95db-41b7-8c87-0062903bac64
# Join this portal^^^
import sys
from Algorithms import Algorithms

trainingFile = sys.argv[1]
testFile = sys.argv[2]
algorithm = sys.argv[3]
stratify_data = False

# Just an extra parameter for running stratification or not
if len(sys.argv) == 5:
    stratify_data = True

algo = Algorithms(trainingFile, testFile)
classes = []

if algorithm == "NB":
    
    pass

if algorithm[1:3] == "NN":
    k = int(algorithm[0])
    if stratify_data:
        classes = algo.cross_validate_kNN(k)
    else:
        classes = algo.run_kNN(k)

for result in classes:
    print(result)
