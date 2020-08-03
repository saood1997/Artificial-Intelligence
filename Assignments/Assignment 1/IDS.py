from gird_state import gird_info
import copy
class IDS:

	goal0 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	goal1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

	sol_flag = False
	depth = 9999999
	goalState = []
	girdToSolve = []
	gird_flag = True
	updateGird = []
	previous = {}


	def __init__(self,gird):
		self.girdToSolve = gird

	def g(self):
		for i in self.girdToSolve:
			print(i)
	def IDSs(self):
		for limit in range(0,self.depth):
			self.Limit_DFS(self.girdToSolve,2)
			if self.sol_flag == True:
				print("solution found at level ",i)
				break
			print("At level ",limit,"solution not found")
			# print(goalState)
			# break
			# self.previous = {}
		else:
			print("solution not found")



	def Limit_DFS(self,gird,limit):
		# if root node is Goal state
		print("At limit",limit,"list",gird)
		print("pre",self.previous)
		if self.check_goal_state(gird,self.goal0):
			self.goalState = gird
			self.sol_flag = True
			return
		elif self.check_goal_state(gird,self.goal1):
			self.goalState = gird
			self.sol_flag = True
			return

		if limit <= 0:
			return

		self.finding_goal(gird,limit-1)


	def check_goal_state(self,gird,goal):
		count = 0
		for i in range(0,len(gird)):
			if gird[i] == goal[i]:
				count += 1
		if count == len(gird):
			return True
		else:
			return False

	def finding_goal(self,gird,limit):
		if self.sol_flag!=True:
			self.move_left(gird,limit)
		elif self.sol_flag!=True:
			self.move_right(gird,limit)
		elif self.sol_flag!=True:
			self.move_up(gird,limit)
		elif self.sol_flag!= True:
			self.move_down(gird,limit)
	def convertIntoString(self,gird):
		st = ""
		for i in gird:
			j = str(i)
			st += j
		return st
	def makestack(self,next,pre,gird,limit):
		if next not in self.previous:
			self.previous[next] = pre
			self.Limit_DFS(gird,limit)

	def move_left(self,gird,limit):
		co = copy.deepcopy(gird)
		if self.canMoveLeft(gird):
			move0 = self.finding_index_zero(gird)
			for i in range (0,len(gird)):
				if move0 == i:
					val = co[i-1]
					co[i] = val
					co[i-1] = 0
					break
			self.makestack(self.convertIntoString(co),self.convertIntoString(gird),co,limit)


	def move_right(self,gird,limit):
		co = copy.deepcopy(gird)
		if self.canMoveRight(gird):
			move0 = self.finding_index_zero(gird)
			for i in range (0,len(gird)):
				if move0 == i:
					val = co[i+1]
					co[i] = val
					co[i+1] = 0
					break
			self.makestack(self.convertIntoString(co),self.convertIntoString(gird),co,limit)
	def move_up(self,gird,limit):
		co = copy.deepcopy(gird)
		if self.canMoveUp(gird):
			move0 = self.finding_index_zero(gird)
			for i in range (0,len(gird)):
				if move0 == i:
					val = co[i-4]
					co[i] = val
					co[i-4] = 0
					break
			self.makestack(self.convertIntoString(co),self.convertIntoString(gird),co,limit)

	def move_down(self,gird,limit):
		co = copy.deepcopy(gird)
		if self.canMoveDown(gird):
			move0 = self.finding_index_zero(gird)
			for i in range (0,len(gird)):
				if move0 == i:
					val = co[i+4]
					co[i] = val 
					co[i+4] = 0
					break
			self.makestack(self.convertIntoString(co),self.convertIntoString(gird),co,limit)



	def finding_index_zero(self,gird):
		for i in range (0,len(gird)):
			if gird[i] == 0:
				return i

	def canMoveLeft(self,gird):
		index = self.finding_index_zero(gird)
		if index % 4 != 0:
			return True
		return False
	def canMoveRight(self,gird):
		index = self.finding_index_zero(gird)
		if (index-3)%4 != 0:
			return True
		return False
	def canMoveUp(self,gird):
		index = self.finding_index_zero(gird)
		if index-3>0:
			return True
		return False
	def canMoveDown(self,gird):
		index = self.finding_index_zero(gird)
		if index-12<0:
			return True
		return False

