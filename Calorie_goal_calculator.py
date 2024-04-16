'''
kanaan gute
'''
class CalorieCalculator:
	def __init__(self, age = "Not Given", weight = "Not Given", height = "Not Given", gender = "Not Given"):
		'''this is the CalorieCalculator object with input values for age,
		weight, height, and gender. if nothing is input, default values 
		are placed as "Not Given"'''
		self.age = age
		self.weight = weight
		self.height = height
		self.gender = gender.lower() #used .lower() function to ensure no errors because python is case sensitive
	
	def feet_to_inches(self):
		inches = 0
		self.height = self.height.split("'")
		feet1 = (int(self.height[0]) * 12)
		inches = feet1 + int(self.height[1])
		inches = int(inches)
		return inches
	
	def calculate_bmr(self):
		'''calculates basal metabolic rate (bmr) based on age, weight, height, and gender
		and returns your bmr as a float. if gender input is invalid, it will ask you to input again
		bmr calculations uses the harrison-benedict formula in english units.'''
		self.height = self.feet_to_inches()
		if self.gender == 'male':
			bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
		elif self.gender == 'female':
			bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age) 
		else:
			print()
			print("Gender input is invalid. Please specify 'male' or 'female'.")
			self.gender = input("Enter your gender (male/female): ").lower()
			if self.gender == 'male':
				bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
			elif self.gender == 'female':
				bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age) 
		return bmr
		
	def daily_calorie_goal(self, goal):
		'''calculates your daily calorie goal based on bmr and goal which is 
		input by user and returns a float as your calories goal. if your
		goal input is invalid, it will ask you to input again'''
		
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
			print()
			print("Goal input is invalid. Choose from 'gain', 'lose', or 'maintain'.")
			goal = input("Do you want to gain, lose, or maintain you weight?: ").lower()
			if bmr is None:
				return None
			if goal == 'gain':
				daily_calories = bmr * 1.2 
			elif goal == 'lose':
				daily_calories = bmr * 0.8
			elif goal == 'maintain':
				daily_calories = bmr
		return daily_calories

#This is the main program for the user to input values 
while True:
	age = int(input("Enter your age: "))
	if age >= 18:
		break 
	print("This calculator is for adults (18+). Enter a valid age.")

#initialize my variables as inputs
weight = float(input("Enter your weight in pounds: "))
height = (input("Enter your height in feet and inches in this format; (height'inches): "))
gender = input("Enter your gender (male/female): ").lower()
goal = input("Do you want to gain, lose, or maintain you weight?: ").lower() 

#creates a CalorieCalculator instance with user inputs
calculator = CalorieCalculator(age, weight, height, gender)

#calculates and shows the daily calorie goal based on your specified goal.
calories_goal = calculator.daily_calorie_goal(goal)
print(f'Your daily calorie goal is: {calories_goal:.0f}') 


