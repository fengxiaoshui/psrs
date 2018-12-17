#PSRS: Personalized Smartphone Recommendation System

from math import sqrt

def load_matrix():
	matrix = {}
	f = open("shopping.csv")
	columns = f.readline().split(',')

	for line in f:
		scores = line.split(',')
		for i in range(len(scores))[1:]:
			matrix[(scores[0], columns[i])] = scores[i].strip("\n")

	return matrix


def load_customer_list():
	customer_list = {}
	f = open("shopping.csv")
	for line in f:
		scores = line.split(',')
		if (scores[0] != "Name"): customer_list[scores[0]] = "1"
	return customer_list


def load_phone_list():
	phone_list = {}
	f = open("shopping.csv")
	phone_list_t = f.readline().split(',')
	for i in phone_list_t:
		if (i != "Name"): phone_list[i] = "1"
	return phone_list

def sim_distance(matrix, row1, row2):
    columns = set(map(lambda l: l[1], matrix.keys()))
    si = list(filter(lambda l: matrix[(row1, l)] != "" and matrix[(row2, l)] != "", columns))
    if len(si) == 0: return 0
    sum_of_distance = sum([pow(float(matrix[(row1, column)]) - float(matrix[(row2, column)]), 2) for column in si])
    return 1 / (1 + sqrt(sum_of_distance))


def top_matches(matrix, row, similarity=sim_distance):
    rows = set(map(lambda l: l[0], matrix.keys()))
    scores = [(similarity(matrix, row, r), r) for r in rows if r != row]
    scores.sort()
    scores.reverse()
    return scores
 

def transform(matrix):
    rows = set(map(lambda l: l[0], matrix.keys()))
    columns = set(map(lambda l: l[1], matrix.keys()))

    transform_matrix = {}
    for row in rows:
        for column in columns:
            transform_matrix[(column, row)] = matrix[(row, column)]
    return transform_matrix


def get_recommendations(matrix, row, similarity=sim_distance):
    rows = set(map(lambda l: l[0], matrix.keys()))
    columns = set(map(lambda l: l[1], matrix.keys()))

    sum_of_column_sim = {}
    sum_of_column = {}

    for r in rows:
        if r == row: continue
        sim = similarity(matrix, row, r)
        if sim <= 0:  continue

        for c in columns:
            if matrix[(r, c)] == "": continue

            sum_of_column_sim.setdefault(c, 0)
            sum_of_column_sim[c] += sim
            sum_of_column.setdefault(c, 0)
            sum_of_column[c] += float(matrix[(r, c)]) * sim

    scores = [(sum_of_column[c] / sum_of_column_sim[c], c) for c in sum_of_column]
    scores.sort()
    scores.reverse()
    return scores

def main():
	matrix = load_matrix()
	customer_list = load_customer_list()
	phone_list = load_phone_list()
	customer_name = input("Person's name: ")
	if (customer_name not in customer_list.keys()):
		print("The customer does not exist")
		return 0

	phone_brand = input("Smartphone's brand: ")
	if (phone_brand not in phone_list.keys()):
		print("The smartphone's brand does not exist")
		return 0
	
	print ("\n")
	print ("Similarity ranking between ", customer_name, "and other custormers")
	tsim = top_matches(matrix, customer_name)
	print (tsim)
	print ("\n")

	trans_matrix = transform(matrix)
	print ("Similarity ranking between ", phone_brand, "and other smartphone brands")
	print (top_matches(trans_matrix, phone_brand))
	print ("\n")

	print ("The ranking of recommended smartphone brands for: ", customer_name)
	print (get_recommendations(matrix, customer_name))
	print ("\n")
	
	print ("The ranking of recommended custormers for: ", phone_brand)
	print (get_recommendations(trans_matrix,  phone_brand))

	return 0

main()