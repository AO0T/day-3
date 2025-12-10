def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi_value = calculate_bmi(weight, height)
print(f"Your BMI is {bmi_value:.2f}")


if bmi_value < 18.5:
    print("You are Underweight.")
elif bmi_value < 24.9:
    print("You are Normal weight.")
elif bmi_value < 29.9:
    print("You are Overweight.")
else:
    print("You are Obese.")



