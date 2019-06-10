from enum import Enum, auto
import time
import random
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


class States():
	INITIAL = 1
   
class EnemeyStates(States):
	INITIAL = 1

class PlayerStates(States):
	INITIAL = 1
	FINAL = 2
 
class GameObject:
	def __init__(self):
		self.__state = States.INITIAL

	def set_state(self, state):
		self.__state = state

	def get_state(self):
		return self.__state

class Entity(GameObject):
	def __init__(self):
		super().__init__()
		self.__health = 100
		self.__probC = 0.5
		self.__probD = 0.5

	def get_probC(self):
		return self.__probC

	def set_probC(self, probC):
		self.__probC = probC

	def get_probD(self):
		return self.__probD

	def set_probD(self, probC):
		self.__probD = probD

	def sub_health(self):
		self.__health -= 5

	def get_health(self):
		return self.__health

	def set_health(self, health):
		self.__health = health

	def cooperate(self):
		self.__health -=5

	def defect(self):
		self.__health -=0

	def reset(self):
		self.__health = 0

playermoney = []
enemymoney = []

playertransitionlist = [] 
enemytransitionlist = []
enemystratergy = ""
Rounds = 10
total_pool = 2*Rounds
contribution = 0
risk_factor = 1
G = 1000


def swap_random(seq):
	try:
		idx = range(len(seq))
		i1, i2 = random.sample(idx, 2)
		seq[i1], seq[i2] = seq[i2], seq[i1]
	except ValueError:
		print('Sample size exceeded population size.')

def line_plot(list1,list2,num):
	line1, = plt.plot(list1, label="Player Agent")
	line2, = plt.plot(list2, label="Enemy Agent")
	# Place a legend to the right of this smaller subplot.
	
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2)
	plt.xlabel('Generations')
	plt.ylabel('Money units')
	plt.title('Relationship of Stratergy with Risk = 1, C = 0.5, P = 0.5(1 Seq)')
	plt.axis([0, num, -10, 400])
	plt.show()
	
# Declare a dictionary 
dict = {'C': 'D', 'D': 'C'}

for gen in range(G):
	player = Entity()
	player.set_health(200)
	player.set_state(PlayerStates.INITIAL)

	enemy = Entity()
	enemy.set_health(200)
	enemy.set_state(EnemeyStates.INITIAL)
	print("Gen",gen)
	for i in range(Rounds):
		if(i%2 == 0):
			if(i<6):
				if((player.get_probC())>(player.get_probD())):
					player.cooperate()
					playertransitionlist.append("C")
					contribution += 5
					print("player's health", player.get_health())
					if(player.get_state() == PlayerStates.INITIAL):
						player.set_state(PlayerStates.FINAL)
				elif((player.get_probC())==(player.get_probD())):
					val = random.choice(["C","D"])
					if(val=="C"):
						player.cooperate()
						playertransitionlist.append("C")
						player.set_state(PlayerStates.INITIAL)
						contribution += 5
						print("player's health", player.get_health())
					else:
						player.defect()
						playertransitionlist.append("D")
						player.set_state(PlayerStates.INITIAL)
						contribution += 0
						print("player's health", player.get_health())

				else:
						player.defect()
						playertransitionlist.append("D")
						contribution += 0
						print("player's health", player.get_health())
			else:
				newstr = enemystratergy[-3:]
				str = dict.get(newstr)
				playertransitionlist.append(str)
				if(str=="C"):
					player.cooperate()
					contribution += 5
					print("player's health", player.get_health())
					if(player.get_state() == PlayerStates.INITIAL):
						player.set_state(PlayerStates.FINAL)
					
				else:
					player.defect()
					contribution += 0
					print("player's health", player.get_health())
				
		else:
			val = random.choice(["C","D"])
			if(val=="C"):
				enemy.cooperate()
				enemystratergy+="C"
				enemytransitionlist.append("C")
				enemy.set_state(EnemeyStates.INITIAL)
				contribution += 5
				print("enemy's health", enemy.get_health())
			else:
				enemy.defect()
				enemystratergy+="D"
				enemytransitionlist.append("D")
				enemy.set_state(EnemeyStates.INITIAL)
				contribution += 0
				print("enemy's health", enemy.get_health())
	
				
	print("-----------------------------")
	print("contribution",contribution)
	print("total pool",total_pool)

	if(risk_factor == 0):
		print("players keep the money without any loss, as loss factor is 0")
		print("contribution",contribution)
		playermoney.append(player.get_health())
		enemymoney.append(enemy.get_health())


	elif(contribution < total_pool and risk_factor == 0.5):
		print("players keep the money without any loss, as loss factor is 0.5")
		print("contribution",contribution)
		print("after half loss")
		print("player health",player.get_health())
		playermoney.append(player.get_health()/2)
		enemymoney.append(enemy.get_health()/2)
	elif(contribution < total_pool and risk_factor == 1):
		print("you reached here")
		playermoney.append(0)
		enemymoney.append(0)
	else:
		print("you reached here 2")
		print("player health",player.get_health())
		playermoney.append(player.get_health())
		enemymoney.append(enemy.get_health())

	print("player's health ", player.get_health())
	print("enemy's health", enemy.get_health())

	print("Reset the health to zero")
	contribution = 0
	player.reset()
	enemy.reset()


	print("Player Stratergy",playertransitionlist)
	#print("Enemy Stratergy list",enemytransitionlist)
	#print("Enemy Stratergy string",enemystratergy)
	print("player money",playermoney)
	print("enemy money",enemymoney)

line_plot(playermoney,enemymoney,G)

	
		
#(contribution < total_pool and risk_factor > 0.5)
	# 	eval = max(player.get_probC,player.get_probD)
	# 	print("enemy's health", enemy.get_health())
	# enemy.sub_health()
	# print("enemy's health", enemy.get_health())
			





