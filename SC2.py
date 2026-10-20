#Name: Bensen Avans
#Class: 6th Hour
#Assignment: SC2

print("BMI calculator")
Height = int(input("Enter Height in centimeters: "))
Weight = int(input("Enter Weight in kilograms: "))

print(Height)
print(Weight)

#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

BMI = (Weight/(Height/100)**2)

print(BMI)

if BMI <= 18.5:
    print("Underweight")
elif BMI < 24.9:
    print("Normal")
elif BMI < 29.9:
    print("Overweight")
elif BMI >= 30:
    print("Obese")