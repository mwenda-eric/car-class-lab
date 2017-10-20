"""
car class 
"""
class Car(object):
	"""docstring for Car"""
	def __init__(self, name='General', model='GM',car_type='saloon'):
		"""Car class constructor method"""
		self.name=name
		self.model=model
		self.car_type=car_type
		self.speed=0
		self.num_of_doors=4
		self.num_of_wheels=4

		if self.name in ["Porshe","Koenigsegg"]:
			self.num_of_doors=2
		elif self.car_type == "trailer":
			self.num_of_wheels=8

	def is_saloon(self):
		"""test if a car object is a salon or not"""
		if self.car_type == "trailer":
			return False
		return True	

	def drive(self,speed):
		"""drive method"""
		if speed==7:
			self.speed=77
		elif speed == 3:
			self.speed=1000
		return self
