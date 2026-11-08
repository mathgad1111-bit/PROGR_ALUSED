
num1 = float(input("Sisestsage esimest arvu: "))
op = input("Valige operatsiooni (+, -, *, /): ")
num2 = float(input("Sisetage teist arvu: "))


if op == "+":
    print("Tulemus:", num1 + num2)
elif op == "-":
    print("Tulemus:", num1 - num2)
elif op == "*":
    print("Tulemus:", num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Jagamine nulliga!")
    else:
        print("Tulemus:", num1 / num2)
else:
    print("Vale operatsioon")
