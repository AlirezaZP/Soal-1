vazn=float(input("Vazn khod ra vared koni:"))
qad=float(input("Qad khod ra vared koni:"))
bmi=vazn/(qad*qad)
if 0<bmi<= 18.5:
    print(bmi,"Underweight")
elif 18.5<bmi<=24.9:
    print(bmi,'Normal')
elif 25<bmi<=29.9:
    print(bmi,'Overweight')
elif 30<bmi<=34.9:
    print(bmi,"Obese")
elif bmi>=35:
    print(bmi,'Extremely Obese')