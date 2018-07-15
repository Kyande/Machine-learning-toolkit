# Kyande Michael John
# P15/34906/2014
# k-Nearest Neighbours algorithm
# import packages
import csv
from operator import itemgetter


class KNN:
    """
    k-Nearest neighbours algorithm class.
    """
    def __init__(self, filename='', limit=0.80, members=3, delimiter=','):
        """
            This is initialization method of the algorithm's class.
            :param filename:
            :param limit:
            :param members:
            :param delimiter:
            """
        self.count = 0  # counter for correct predictions
        self.results = self.load_data(filename=filename, limit=limit, delim=delimiter)  # load data and receive response
        self.test_data = self.results[1]
        self.training_data = self.results[0]
        # get data neighbours of each member of the test data set.
        for x in range(len(self.test_data)):
            neighbours = self.get_neighbours(training_data=self.training_data, instance=self.test_data[x], k=members)
            # make a prediction.
            label = self.count_votes(neighbours=neighbours)
            # compare predicted outcome to actual outcome.
            print("{}). Actual outcome => '{}' & Predicted outcome => '{}'".format(x + 1, self.test_data[x][-1], label))
            if self.test_data[x][-1] == label:
                self.count = self.count + 1

        # Calculate accuracy percentage.
        self.accuracy = (self.count / len(self.test_data)) * 100
        print("\nAccuracy = {0:.2f}%".format(self.accuracy))

    def load_data(self, filename='', limit=0.75, delim=','):
        """
            This method loads data from the file. A
            ny number of columns is accepted but provided the labels are on the last columns to the right.
            :param filename:
            :param limit:
            :param delim:
            :return results:
            """
        with open(filename) as data:
            reader = csv.reader(data, delimiter=delim)
            f = list(reader)
        for x in range(len(f)):
            for y in range(len(f[0]) - 1):
                f[x][y] = float(f[x][y])  # convert elements of each array to type float except the last one

        lim = limit * (len(f))  # calculate where the training data and test data are divided
        lim = int(lim)  # convert limit for indexing purposes
        results = (f[:lim], f[lim:])  # append training data and test data to tuple

        # for x in range(len(f)):
        #     print(f[x])

        del f  # delete f array which was temporary

        return results  # return value


    def get_neighbours(self, training_data=(), instance=(), k=3):
        """
            This method receives the whole training data set, the data instance being predicted and the cluster member size.
            :param training_data:
            :param instance:
            :param k:
            :return prediction:
            """
        data = []
        neighbours = []
        # calculate the query distance
        for x in range(len(training_data)):
            distance = self.query_distance(instance1=training_data[x][:-1], instance2=instance[:-1])
            data.append([training_data[x], distance])
        # sort the neighbours based on key which is the distance in ascending
        data = sorted(data, key=itemgetter(-1))

        # pick the top neighbours of the test data
        for x in range(k):
            neighbours.append(data[:k][x][0])

        # return the neighbours of the test data
        return neighbours


    def query_distance(self, instance1=(), instance2=()):
        """
            This method calculates the query distance between the current data in the training set and the test data in
            question
            :param instance1:
            :param instance2:
            :return distance:
            """
        distance = sum([pow((a - b), 2) for a, b in zip(instance1, instance2)])
        return distance


    def count_votes(self, neighbours=()):
        """
            This method receives the neighbours of the test data and takes a tally of the votes and makes a decision.
            The decision is based on the label with the highest count.
            :param neighbours:
            :return vote:
            """
        labels = []
        data = neighbours
        # create the list made up of labels.
        for x in range(len(data)):
            labels.append(data[x][-1])

        # count the appearance of labels.
        count = [[x, labels.count(x)] for x in set(labels)]
        # Sort the labels in descending order by using their frequency
        vote = sorted(count, key=itemgetter(-1), reverse=True)
        # return the prediction
        # print("[{}]".format(vote[0][0]))
        return vote[0][0]
