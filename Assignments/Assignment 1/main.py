# from puzzle import puzzle
from Issolveable import Is_solveable
from gird_state import gird_info
from IDS import IDS
from gird_state import gird_info
# g1 = gird_info()

def input_matrix():
    print("Enter the entries rowwise:") 
    matrix = []
    for i in range(4):
        a =[] 
        for j in range(4):  
            a.append(int(input()))
        matrix.append(a)
    return matrix
def gird(matrix):
	gird = []
	for i in range(0,len(matrix)):
		for j in range(0,len(matrix)):
			var = matrix[i][j]
			gird.append(var)
	return gird


# matrix = input_matrix()
matrix = [[1,2,3,4],[5,6,7,8],[9,0,11,12],[13,10,14,15]]
gird = gird(matrix)
print("gird = ",gird)
s1 = Is_solveable()
# print("len = ",len(matrix))
# s = gird_info(4,4,matrix)
flag = s1.is_solveable(matrix)
if flag == True:
    print("puzzle is solveable") #if the blank in goal gird is on the left corner
# else:
#     print("puzzle is not solveable") #if the blank in goal gird is on the right corner

d1 = IDS(gird)
d1.IDSs()