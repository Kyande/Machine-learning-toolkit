k-Nearest Neighbours.
=====================

The above code implements the kNN algorithm where label of the data tested is chosen from the closest neighbours. The label with the highest frequency is considered to be the correct one. The closest neighbours are determined by calculating query distance, that is test data instance subtracted from training data instance and the result is squared(Just like Euclidian distance but without the square root.).

How to use.
-----------
1. Pass the name of the CSV file. 
2. The percentage of training data you require. 
3. Number of neighbours to be picked.
4. The delimiter separating the data.
