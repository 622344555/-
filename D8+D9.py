from random import randint 
import pygal
class Die():
	def __init__(self,num_sides=6):
		self.num_sides= num_sides
	def roll(self):
		return randint(1, self.num_sides)
	def show_freq(self):
		for roll_num in range(5000):
			result=die_1.roll()+die_2.roll()
			results.append(result)
		for value in range(2, maxresult+1):
			frequency=results.count(value)
			frequencies.append(frequency)
		return frequencies
die_1=Die(8)
die_2=Die(10)
results=[]
frequencies=[]
maxresult=die_1.num_sides+die_2.num_sides
die_1.show_freq()
hist=pygal.Bar()
hist.title="Result of rolling a D8 and D10 5000 times."
hist.x_labels=[x  for x in range(2,maxresult+1)]
hist.x_title="value"
hist.y_title="result"
hist.add("D9+D10",frequencies)
hist.render_to_file("dice.svg")
