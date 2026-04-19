import csv
from random import shuffle, uniform

class Perceptron:
    def __init__(self):
        self.weights = None
        self.learning_rate = 0.1
        self.epoch = 1000
        self.bias = 0.0

    def hypothesis(self, X):
        dot_product = self.dot_product(X)

        if dot_product >= 0:
            return 1
        else:
            return 0

    def learning(self, X, y):
        self.weights = [uniform(-1, 1) for _ in range(len(X[0]))]

        for _ in range(self.epoch):
            combined = list(zip(X, y))
            shuffle(combined)

            for cur_x, supposed in combined:
                error = (supposed - self.hypothesis(cur_x))

                learning_rule = (self.learning_rate * error)

                self.bias += learning_rule # hmm why is this

                for i in range(len(self.weights)):
                    self.weights[i] += learning_rule * cur_x[i]

        print("Done.")

    def dot_product(self, X):
        ret_dot_product = 0

        for input, weight in zip(X, self.weights):
            single = input * weight

            ret_dot_product += single

        return ret_dot_product + self.bias

def main():
    file = input("file: ")

    with open(file) as f:
        reader = csv.reader(f)
        next(reader)

        data = []
        for row in reader:
            data.append({
                "evidence": [float(cell) for cell in row[:2]],
                "label": int(row[2])
            })

    perceptron = Perceptron()

    shuffle(data)

    half = int(len(data)/2)

    learning = data[:half]
    testing = data[half:]

    X_learning = [row["evidence"] for row in learning]
    y_learning = [row["label"] for row in learning]

    perceptron.learning(X_learning, y_learning)

    correct = 0
    incorrect = 0

    for test in testing:
        verdict = test["label"] == perceptron.hypothesis(test["evidence"])
        
        if verdict:
            correct += 1
        else:
            incorrect += 1

    print("Correct:", correct, "out of", correct + incorrect)
    print("Incorrect:", incorrect, "out of", correct + incorrect)

if __name__ == "__main__":
    main()