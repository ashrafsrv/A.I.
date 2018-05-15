import math

class Algorithms:
    def __init__(self):
        self.D = []

    # preg, plasma, bp, skinfold, insulin, bmi, pedigree, age, classvar
    def transform_dataset(self, file_str):

        with open(file_str) as f:
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

                self.D.append(tmp)


    def calculate_distance(self, dataset, target):
        return


    def run_NB(self, trainingFile, testFile):
        return None



    def run_kNN(self, k, trainingFile, testFile):
        return None
