from random import choice
import matplotlib.pyplot as plt
class RandomWalk():
	def __init__(self,num_points=5000):
		self.num_points=num_points
		self.x_value= [0]
		self.y_value= [0]
	def get_step(self):
		direction=choice([-1,1])
		distance=choice([0, 1, 2, 3, 4])
		step=direction*distance
		return step

	def fill_walk(self):
		while len(self.x_value)<self.num_points:
			x_step= self.get_step()
			y_step= self.get_step()
			if x_step==0 and y_step ==0:
				continue
			x_next=self.x_value[-1]+x_step
			y_next=self.y_value[-1]+y_step
			self.x_value.append(x_next)
			self.y_value.append(y_next)

while True:
	nb=RandomWalk()
	nb.fill_walk()
	plt.figure(dpi=128,figsize=(10,6))
	point_num = list(range(nb.num_points))
	plt.scatter(nb.x_value, nb.y_value,edgecolor="none",c=point_num,cmap=plt.cm.Reds, s=5)
	plt.scatter(0, 0,edgecolor="none",c="black", s=100)
	plt.scatter(nb.x_value[-1], nb.y_value[-1],edgecolor="none",c="green", s=100)
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()
	keep_goo =input("make another walk?(y/n):")
	if keep_goo =="n":
		break
