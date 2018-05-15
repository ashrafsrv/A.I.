import math
import numpy as np
from numpy import array

class Algorithms:
    # preg, plasma, bp, skinfold, insulin, bmi, pedigree, age, classvar
    def transform_dataset(file_str, classVar):

        with open(file_str) as f:
            dataset = []

            for line in f:
                llist = line.split(',')

                tmp = {}
                tmp['preg'] = float(llist[0])
                tmp['plasma'] = float(llist[1])
                tmp['bp'] = float(llist[2])
                tmp['skinfold'] = float(llist[3])
                tmp['insulin'] = float(llist[4])
                tmp['bmi'] = float(llist[5])
                tmp['pedigree'] = float(llist[6])
                tmp['age'] = float(llist[7])

                if classVar:
                    tmp['class'] = llist[8].strip()

                dataset.append(tmp)
            return dataset

    def calculate_distance(trained, test):
        distance_list = []

        for instance in test:
            tmp = []
            for example in trained:
                a = math.pow((example['preg'] - instance['preg']), 2)
                b = math.pow((example['plasma'] - instance['plasma']), 2)
                c = math.pow((example['bp'] - instance['bp']), 2)
                d = math.pow((example['skinfold'] - instance['skinfold']), 2)
                e = math.pow((example['insulin'] - instance['insulin']), 2)
                f = math.pow((example['bmi'] - instance['bmi']), 2)
                g = math.pow((example['pedigree'] - instance['pedigree']), 2)
                h = math.pow((example['age'] - instance['age']), 2)

                distance = math.sqrt(a + b + c + d + e + f + g + h)
                tmp.append(distance)
            distance_list.append(tmp)

        return distance_list


    def __init__(self, training_file, test_file):
        self.training_dataset = Algorithms.transform_dataset(training_file, classVar=True) # A list of dictionaries
        self.test_dataset = Algorithms.transform_dataset(test_file, classVar=False)
        self.distances = Algorithms.calculate_distance(self.training_dataset, self.test_dataset) # A list of lists of Euclidean distances
        self.results = []

    def run_NB(self):
        return None


    def find_nearest_elements(self, k, distances):
        copy_dataset = self.training_dataset[:]
        copy_distances = distances[:]

        elements = []
        indices = []

        for j in range(k):

            minimum = min(copy_distances)
            indices = [i for i, v in enumerate(copy_distances) if v == minimum]

            boolean = False

            for i in indices:
                if copy_dataset[i]['class'] == 'Yes':
                    elements.append(copy_dataset.pop(i))
                    copy_distances.pop(i)
                    boolean = True
                    break

            if boolean == True:
                continue

            elements.append(copy_dataset.pop(indices[0]))
            copy_distances.pop(indices[0])
        return elements

    def run_kNN(self, k):
        classes = []

        for i in range(len(self.distances)):
            elements = self.find_nearest_elements(k, self.distances[i])

            yes = 0
            no = 0
            for example in elements:
                if example['class'] == 'yes':
                    yes += 1
                elif example['class'] == 'no':
                    no += 1

            if yes >= no:
                classes.append('yes')
            else:
                classes.append('no')
        return classes
