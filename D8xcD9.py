#method1 遍历1到最大的乘积的列表,如果列表值存在于相乘的结果中,添加到新的xc列表中,再遍历xc列表
#计算机不统计不在xc列表中的数据
from random import randint 
import pygal
class Die():
	def __init__(self,num_sides=6):
		self.num_sides= num_sides
	def roll(self):
		return randint(1, self.num_sides)
	def show_freq(self):
		for roll_num in range(5000):
			result=die_1.roll()*die_2.roll()
			results.append(result)
		for value in range(1, maxresult+1):
			if value in results:
				xc.append(value)
		for value in xc:
			frequency=results.count(value)
			frequencies.append(frequency)
		return frequencies
xc=[]
die_1=Die(8)
die_2=Die(10)
results=[]
frequencies=[]
maxresult=die_1.num_sides*die_2.num_sides
die_1.show_freq()
hist=pygal.Bar()
hist.title="Result of rolling a D8 and D10 5000 times."
hist.x_labels=xc
hist.x_title="value"
hist.y_title="result"
hist.add("D9*D10",frequencies)
hist.render_to_file("dice1.svg")

#method2
from die import Die
import pygal
 
#创建两个点数不同的骰子
die_1=Die()
die_2=Die(10)
 
#投掷多次并将相乘结果记录在列表中
results=[]
 
for roll_num in range(50000):
    result=die_1.roll() * die_2.roll()
    results.append(result)
 
#统计频率
frequencies=[]
max_result=die_1.num_sides * die_2.num_sides
for value in range(1,max_result+1):
    if results.count(value):
       frequency=results.count(value)
       frequencies.append(frequency)
 
#可视化结果
#将所有可能的乘积保存在列表xs中，所得乘积并不连续
xs=[]
for value in range(1,max_result+1):
    if value in results:
       xs.append(value)
hist=pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times." 
hist.x_labels=xs
hist.x_title = "Result" 
hist.y_title = "Frequency of Result" 
 
hist.add('D6 * D10', frequencies) 
hist.render_to_file('multiply_visual.svg') 
