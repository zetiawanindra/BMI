#Input weight and height from user
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in centimeters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI Category
if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal weight"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"

# Print results
print("Your BMI is: ", round(bmi, 2))
print("Your BMI category is: ", category)