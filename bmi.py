
# how to calculate BMI
def BMI(height, weight):
	bmi = weight/(height**2)
	return bmi

# Driver code
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# calling the BMI function
BMI = weight / (height/100)**2
print(f"You BMI is {BMI}")


# Conditions to find out BMI category
if BMI <= 18.5:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 25:
    print("You are over weight.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")