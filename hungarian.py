import random
import copy
import numpy as np
from operator import itemgetter

def hungarian_algorithm(mat): 
	dim = mat.shape[0]
	cur_mat = mat.copy()

	#Step 1 - Every column and every row subtract its internal minimum
	for row_num in range(mat.shape[0]): 
		cur_mat[row_num] -= np.nanmin(cur_mat[row_num])
    
	for col_num in range(mat.shape[1]): 
		cur_mat[:,col_num] -= np.nanmin(cur_mat[:,col_num])
	
	return cur_mat

def min_zero_row(zero_mat, mark_zero, seats_left):
	#Find the row
	min_row = [99999, -1]

	for row_num in range(zero_mat.shape[0]): 
		if np.sum(zero_mat[row_num] == True) > 0 and min_row[0] > np.sum(zero_mat[row_num] == True):
			min_row = [np.sum(zero_mat[row_num] == True), row_num]
	zero_index = 0
	for col_num in range(len(zero_mat[min_row[1]])):
		if zero_mat[min_row[1]][col_num] == True:
			zero_index = col_num

	if seats_left[zero_index] > 0:
		mark_zero.append([min_row[1], zero_index])
	zero_mat[min_row[1], :] = np.nan
	if seats_left[zero_index] == 0:
		zero_mat[:, zero_index] = np.nan
	else:
		seats_left[zero_index] -= 1

def extract_col(row):
	return row[1]

def main():
	data_set=[]
	rows, cols, rounds, chairs=10,5,1,2
	for row in range(rows):
		column=[]
		while len(column) != cols:
			r = random.randint(1,cols)
			if r not in column:
				column.append(r)
		data_set.append(column)
	
	mat = np.array(data_set, dtype = float)

	seats_left=[chairs]*cols
	while seats_left.count(0) != cols :

		cur_mat = hungarian_algorithm(mat)
		print(cur_mat)
		print(seats_left)

		bool_mat = (cur_mat == 0)

		parings=[]
		for i in range(rows):
			min_zero_row(bool_mat, parings, seats_left)

		# res = -1
		# index = -1
		# collection=[]*cols
		# for i in range(cols):
		# 	test = np.array(parings)
		# 	print(test[:,1])
		# 	print(sum(test[:,1] == i))
		# 	if res < sum(np.array(parings)[:,1] == i):
		# 		res = i
		# for i in range(len(parings)):
		# 	collection[parings[i][1]].append(parings[i][0])
		# print("collection =", collection)
		
		#set students that are have a seat and companies that have no seats left
		for i in range(len(parings)):
			mat[parings[i][0], :] = np.nan
			if seats_left[parings[i][1]] == 0:
				mat[:, parings[i][1]] = np.nan
		print(parings)
		input("____________________________")
	print(mat)
	# for r in range(rounds):
	# 	# calculate demand weight for each of the companies
	# 	weights=[0]*cols
	# 	for row in range(rows):
	# 		for col in range(cols):
	# 			weights[col] += data_set2[row][col]

	# 	# adjust individual cost with the demand weight
	# 	data_set_round = copy.deepcopy(data_set2)
	# 	for row in range(rows):
	# 		for col in range(cols):
	# 			data_set_round[row][col] *= weights[col]
		
	# 	# subtract min from rows
	# 	for row in range(rows):
	# 		x = min(data_set_round[row])
	# 		for col in range(cols):
	# 			data_set_round[row][col] -= x

	# 	company_chairs_available=[chairs]*cols
	# 	while company_chairs_available.count(0) != len(company_chairs_available):
	# 	# 	subtract min from cols
	# 		trans_data = [list(x) for x in zip(*data_set_round)]
	# 		for col in range(cols):
	# 			x = min(trans_data[col])
	# 			for row in range(rows):
	# 				trans_data[col][row] -= x

	# 		#count how many have this company as best suited
	# 		company_chairs=[0]*cols
	# 		for col in range(cols):
	# 			company_chairs[col] = trans_data[col].count(0)
	# 		data_set_round = [list(x) for x in zip(*trans_data)]

	# 		# find unique zeros in rows which are for companies that still have seats available
	# 		for row in range(rows):
	# 			count = 0
	# 			for col in range(cols):
	# 				if data_set_round[row][col] == 0 and company_chairs[col] < company_chairs_available[col]:
	# 					count += 1
	# 			if count == 1:
	# 				for col in range(cols):
	# 					if data_set_round[row][col] == 0 and company_chairs[col] < company_chairs_available[col]:
	# 						print(row +1, col +1)
	# 						company_chairs_available[col] -= 1
	# 						for i in range(cols):
	# 							data_set_round[row][i] = 100

	# 		for col in range (cols):
	# 			if company_chairs_available[col] == 0:
	# 				for row in range(rows):
	# 					data_set_round[row][col] = 100
			
	# 		for row in range(rows):
	# 			print(data_set_round[row])
	# 		input("press something")
	# 	print(company_chairs_available)

if __name__ == "__main__":
	main()