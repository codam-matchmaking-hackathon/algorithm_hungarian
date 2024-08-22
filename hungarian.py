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

def min_zero_row(zero_mat, mark_zero):
	#Find the row
	min_row = [99999, -1]

	for row_num in range(zero_mat.shape[0]): 
		if np.sum(zero_mat[row_num] == True) > 0 and min_row[0] > np.sum(zero_mat[row_num] == True):
			min_row = [np.sum(zero_mat[row_num] == True), row_num]
	zero_index = 0
	for col_num in range(len(zero_mat[min_row[1]])):
		if zero_mat[min_row[1]][col_num] == True:
			zero_index = col_num

	mark_zero.append((min_row[1], zero_index))
	zero_mat[min_row[1], :] = False
	zero_mat[:, zero_index] = False


def mark_matrix(mat):

	#Transform the matrix to boolean matrix(0 = True, others = False)
	cur_mat = mat
	zero_bool_mat = (cur_mat == 0)
	zero_bool_mat_copy = zero_bool_mat.copy()

	#Recording possible answer positions by marked_zero
	marked_zero = []
	while (True in zero_bool_mat_copy):
		min_zero_row(zero_bool_mat_copy, marked_zero)

	#Recording the row and column indexes seperately.
	marked_zero_row = []
	marked_zero_col = []
	for i in range(len(marked_zero)):
		marked_zero_row.append(marked_zero[i][0])
		marked_zero_col.append(marked_zero[i][1])
	#step 2-2-1
	non_marked_row = list(set(range(cur_mat.shape[0])) - set(marked_zero_row))
		
	marked_cols = []
	check_switch = True
	while check_switch:
		check_switch = False
		for i in range(len(non_marked_row)):
			row_array = zero_bool_mat[non_marked_row[i], :]
			for j in range(row_array.shape[0]):
				#step 2-2-2
				if row_array[j] == True and j not in marked_cols:
					#step 2-2-3
					marked_cols.append(j)
					check_switch = True

		for row_num, col_num in marked_zero:
			#step 2-2-4
			if row_num not in non_marked_row and col_num in marked_cols:
				#step 2-2-5
				non_marked_row.append(row_num)
				check_switch = True
	#step 2-2-6
	marked_rows = list(set(range(mat.shape[0])) - set(non_marked_row))
		
	return(marked_zero, marked_rows, marked_cols)

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

		marked_zero, marked_rows, marked_cols = mark_matrix(cur_mat)
		print(marked_zero)
		print(marked_rows)
		print(marked_cols)
		
		input("____________________________")
	print(mat)

if __name__ == "__main__":
	main()