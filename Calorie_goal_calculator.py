'''
kanaan gute
'''
class CalorieCalculator:
	def __init__(self, age = "Not Given", weight = "Not Given", height = "Not Given", gender = "Not Given"):
		self.age = age
		self.weight = weight
		self.height = height
		self.gender = gender.lower()
	
	def calculate_bmr(self):
		if self.gender == 'male':
			bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
		elif self.gender == 'female':
			bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age) 
		else:
			print("Invalid input. Please specify 'male' or 'female'.")
			return None
		return bmr
		
	def daily_calorie_goal(self, goal):
		bmr = self.calculate_bmr()
		if bmr is None:
			return None
		if goal == 'gain':
			daily_calories = bmr * 1.2 
		elif goal == 'lose':
			daily_calories = bmr * 0.8
		elif goal == 'maintain':
			daily_calories = bmr
		else:
			print("This is not a goal. Choose from 'gain', 'lose', or 'maintain'.")
			return None
		return daily_calories

while True:
	age = int(input("Enter your age: "))
	if age >= 18:
		break 
	print("This calculator is for adults (18+). Enter a valid age.")

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
gender = input("Enter your gnder (male/female): ").lower()
goal = input("Do you want to gain, lose, or maintain you weight?: ").lower()

calculator = CalorieCalculator(age, weight, height, gender)
calories_goal = calculator.daily_calorie_goal(goal)
print(f'Your daily calorie goal is: {calories_goal:.0f}') 
		

