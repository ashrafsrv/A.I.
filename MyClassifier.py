

#Todo for ashraf
# Create functions for naive bayes and kNN, i'll integrate main with them
# If we use multiple files, how do we integrate it with teletype?
# can we use a single file then :P otherwise just share other files like i did for this one. Okay

# Algorithms.py: atom://teletype/portal/1560ee10-95db-41b7-8c87-0062903bac64
# Join this portal^^^
import sys
from Algorithms import Algorithms

trainingFile = sys.argv[1]
testFile = sys.argv[2]
algorithm = sys.argv[3]

if (algorithm == "NB"):
    Algorithms.run_NB(trainingFile, testFile)
else:
    algoSplit = list(algorithm)
    if ("".join(algoSplit[1:3]) == "NN"):
        run_kNN(int(algoSplit[0]), trainingFile, testFile)
