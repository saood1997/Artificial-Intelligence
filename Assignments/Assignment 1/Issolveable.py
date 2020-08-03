class Is_solveable:
	
	def check_inversions(self,matrix):
		no_inversions = 0
		check_matrixA = []
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				var = matrix[i][j]
				check_matrixA.append(var)
		val = len(check_matrixA)
		i = 0
		while i<val:
			if check_matrixA[i] == 0:
				i += 1
				continue
			j = i + 1
			while j<val:
				if check_matrixA[j] == 0:
					j += 1
					continue
				elif check_matrixA[i]>check_matrixA[j]:
					no_inversions += 1
				j += 1
			i += 1
		return no_inversions

	def findXPosition(self,mat):
		matrix = []
		for i in range(len(mat)):
			for j in range(len(mat)):
				var = mat[i][j]
				matrix.append(var)

		for i in range(0, 16):
			if matrix[i] == 0:
				return 4 - int(i / 4)

	def is_solveable(self,matrix):
		flag = False
		in_val = self.check_inversions(matrix)
		pos = self.findXPosition(matrix)
		print("Inversion Count = ",in_val)
		print("Postion of 0 from bottom = ",pos)


		if len(matrix)%2 == 0: #gird length is even
			if in_val%2 == 0: # number of inverstions is even
				if pos%2 != 0: #blank is on an odd row counting from the bottom
					flag = True
			elif in_val%2 != 0:
				if pos%2 == 0:
					flag == True

		if len(matrix)%2 != 0: #gird length is odd
			if in_val%2 == 0:  #number of inversions is even
				flag == True
			else:
				flag == False
		return flag
