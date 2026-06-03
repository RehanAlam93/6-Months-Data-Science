# BMI Calculator

weight = float(input("Enter your weight "))
height = float(input("Enter your height in meter : "))

bmi = weight / (height ** 2)

print("your body mass index is :", round(bmi, 2))

# BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")