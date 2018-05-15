import math

class Algorithms:
    # preg, plasma, bp, skinfold, insulin, bmi, pedigree, age, classvar
    def transform_dataset(file_str):

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
                h = g = math.pow((example['age'] - instance['age']), 2)

                distance = math.sqrt(a + b + c + d + e + f + g + h)
                tmp.append(distance)
            distance_list.append(tmp)

        return distance_list


    def __init__(self, training_file, test_file):
        self.training_dataset = Algorithms.transform_dataset(training_file) # A list of dictionaries
        self.test_dataset = Algorithms.transform_dataset(test_file)
        self.distances = Algorithms.calculate_distance(self.training_dataset, self.test_dataset) # A list of lists of Euclidean distances


    def run_NB(self):
        return None



    def run_kNN(self, k):
        return None
