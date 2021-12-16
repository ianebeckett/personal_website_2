
print("This program informs the user of their 10-year risk of heart attack.")

# reads in the user's heart attack risk factors

sex = input("Enter your sex (M/F): ")
age = int(input("Enter your age (years, 20-79): "))
cholesterol = int((input("Enter your total cholesterol: ")))
hdl = int(input("Enter your HDL (mg/dL): "))
sys_bp = int((input("Enter your systolic blood pressure (mmHg): ")))
smoker = input("Do you smoke? (Y/N): ")
bp_med = input("Are you taking blood pressure medication? (Y/N): ")

points = 0

if sex == 'M':

    # age and cholesterol

    # 20-34

    if 20 <= age <= 34:
        points += -9
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 4
        elif 200 <= cholesterol <= 239:
            points += 7
        elif 240 <= cholesterol <= 279:
            points += 9
        elif cholesterol >= 280:
            points += 11
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 35-39

    elif 35 <= age <= 39:
        points += -4
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 4
        elif 200 <= cholesterol <= 239:
            points += 7
        elif 240 <= cholesterol <= 279:
            points += 9
        elif cholesterol >= 280:
            points += 11
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 40-44

    elif 40 <= age <= 44:
        points += 0
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 3
        elif 200 <= cholesterol <= 239:
            points += 5
        elif 240 <= cholesterol <= 279:
            points += 6
        elif cholesterol >= 280:
            points += 8
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 45-49

    elif 45 <= age <= 49:
        points += 3
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 3
        elif 200 <= cholesterol <= 239:
            points += 5
        elif 240 <= cholesterol <= 279:
            points += 6
        elif cholesterol >= 280:
            points += 8
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 50-54

    elif 50 <= age <= 54:
        points += 6
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 2
        elif 200 <= cholesterol <= 239:
            points += 3
        elif 240 <= cholesterol <= 279:
            points += 4
        elif cholesterol >= 280:
            points += 5
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 55-59

    elif 55 <= age <= 59:
        points += 8
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 2
        elif 200 <= cholesterol <= 239:
            points += 3
        elif 240 <= cholesterol <= 279:
            points += 4
        elif cholesterol >= 280:
            points += 5
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 60-64

    elif 60 <= age <= 64:
        points += 10
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 1
        elif 200 <= cholesterol <= 239:
            points += 1
        elif 240 <= cholesterol <= 279:
            points += 2
        elif cholesterol >= 280:
            points += 3
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 65-69

    elif 65 <= age <= 69:
        points += 11
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 1
        elif 200 <= cholesterol <= 239:
            points += 1
        elif 240 <= cholesterol <= 279:
            points += 2
        elif cholesterol >= 280:
            points += 3
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 70-74

    elif 70 <= age <= 74:
        points += 12
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 0
        elif 200 <= cholesterol <= 239:
            points += 0
        elif 240 <= cholesterol <= 279:
            points += 1
        elif cholesterol >= 280:
            points += 1
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 75-79

    elif 75 <= age <= 79:
        points += 13
        if 0 <= cholesterol < 160:
            points += 0
        elif 160 <= cholesterol <= 199:
            points += 0
        elif 200 <= cholesterol <= 239:
            points += 0
        elif 240 <= cholesterol <= 279:
            points += 1
        elif cholesterol >= 280:
            points += 1
        else:  # invalid input
            print("Invalid input for cholesterol.")

    else:  # invalid input
        print("Invalid input for age")

    # Smoker/non-smoker

    if smoker == 'Y':
        if 20 <= age <= 39:
            points += 8
        elif 40 <= age <= 49:
            points += 5
        elif 50 <= age <= 59:
            points += 3
        elif 60 <= age <= 79:
            points += 1

    # hdl

    if hdl >= 60:
        points += -1
    elif 40 <= hdl <= 49:
        points += 1
    elif hdl < 40:
        points += 2

# blood pressure, with or without medication

    if bp_med == "N":
        if 0 <= sys_bp <= 129:
            points += 0
        elif 130 <= sys_bp <= 139:
            points += 1
        elif 140 <= sys_bp <= 159:
            points += 1
        elif sys_bp >= 160:
            points += 2
        else:
            print("Invalid input for systolic blood pressure")
    elif bp_med == "Y":
        if 0 <= sys_bp < 120:
            points += 0
        elif 120 <= sys_bp <= 129:
            points += 1
        elif 130 <= sys_bp <= 139:
            points += 2
        elif 140 <= sys_bp <= 159:
            points += 2
        elif sys_bp >= 160:
            points += 3
        else:
            print("Invalid input for systolic blood pressure")
    else:
        print("Invalid input for blood pressure medication")

# male risk

    if points < 0:
        risk = '<1%'
    elif 0 <= points <= 4:
        risk = '1%'
    elif points == 5 or points == 6:
        risk = '2%'
    elif points == 7:
        risk = '3%'
    elif points == 8:
        risk = '4%'
    elif points == 9:
        risk = '5%'
    elif points == 10:
        risk = '6%'
    elif points == 11:
        risk = '8%'
    elif points == 12:
        risk = '10%'
    elif points == 13:
        risk = '12%'
    elif points == 14:
        risk = '16%'
    elif points == 15:
        risk = '20%'
    elif points == 16:
        risk = '25%'
    elif points >= 17:
        risk = '>= 30%'
    print('Your 10-year risk of heart attack is ' + risk)
else:  # Female

    # age and cholesterol

    # 20-34

    if 20 <= age <= 34:
        points += -7
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 4
        elif 200 <= cholesterol <= 239:
            points += 8
        elif 240 <= cholesterol <= 279:
            points += 11
        elif cholesterol >= 280:
            points += 13
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 35-39

    elif 35 <= age <= 39:
        points += -3
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 4
        elif 200 <= cholesterol <= 239:
            points += 8
        elif 240 <= cholesterol <= 279:
            points += 11
        elif cholesterol >= 280:
            points += 13
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 40-44

    elif 40 <= age <= 44:
        points += 0
        if 0 <= cholesterol < 160:
            points += 0
        elif 160 <= cholesterol <= 199:
            points += 3
        elif 200 <= cholesterol <= 239:
            points += 6
        elif 240 <= cholesterol <= 279:
            points += 8
        elif cholesterol >= 280:
            points += 10
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 45-49

    elif 45 <= age <= 49:
        points += 3
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 3
        elif 200 <= cholesterol <= 239:
            points += 6
        elif 240 <= cholesterol <= 279:
            points += 8
        elif cholesterol >= 280:
            points += 10
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 50-54

    elif 50 <= age <= 54:
        points += 6
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 2
        elif 200 <= cholesterol <= 239:
            points += 4
        elif 240 <= cholesterol <= 279:
            points += 5
        elif cholesterol >= 280:
            points += 7
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 55-59

    elif 55 <= age <= 59:
        points += 8
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 2
        elif 200 <= cholesterol <= 239:
            points += 4
        elif 240 <= cholesterol <= 279:
            points += 5
        elif cholesterol >= 280:
            points += 7
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 60-64

    elif 60 <= age <= 64:
        points += 10
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 1
        elif 200 <= cholesterol <= 239:
            points += 2
        elif 240 <= cholesterol <= 279:
            points += 3
        elif cholesterol >= 280:
            points += 4
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 65-69

    elif 65 <= age <= 69:
        points += 12
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 1
        elif 200 <= cholesterol <= 239:
            points += 2
        elif 240 <= cholesterol <= 279:
            points += 3
        elif cholesterol >= 280:
            points += 4
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 70-74

    elif 70 <= age <= 74:
        points += 14
        if 0 <= cholesterol < 160:
            points += 0
        elif 0 <= cholesterol <= 199:
            points += 1
        elif 200 <= cholesterol <= 239:
            points += 1
        elif 240 <= cholesterol <= 279:
            points += 2
        elif cholesterol >= 280:
            points += 2
        else:  # invalid input
            print("Invalid input for cholesterol.")

    # 75-79

    elif 75 <= age <= 79:
        points += 16
        if 0 <= cholesterol < 160:
            points += 0
        elif 160 <= cholesterol <= 199:
            points += 1
        elif 200 <= cholesterol <= 239:
            points += 1
        elif 240 <= cholesterol <= 279:
            points += 2
        elif cholesterol >= 280:
            points += 2
        else:  # invalid input
            print("Invalid input for cholesterol.")

    else:  # invalid input
        print("Invalid input for age")

    # Smoker/non-smoker

    if smoker == 'Y':
        if 20 <= age <= 39:
            points += 9
        elif 40 <= age <= 49:
            points += 7
        elif 50 <= age <= 59:
            points += 4
        elif 60 <= age <= 69:
            points += 2
        elif 70 <= age <= 79:
            points += 1

    # hdl

    if hdl >= 60:
        points += -1
    elif 40 <= hdl <= 49:
        points += 1
    elif hdl < 40:
        points += 2

# blood pressure, with or without medication

    if bp_med == "N":
        if 0 <= sys_bp < 120:
            points += 0
        elif 120 <= sys_bp <= 129:
            points += 1
        elif 130 <= sys_bp <= 139:
            points += 2
        elif 140 <= sys_bp <= 159:
            points += 3
        elif sys_bp >= 160:
            points += 4
        else:
            print("Invalid input for systolic blood pressure")
    elif bp_med == "Y":
        if 0 <= sys_bp < 120:
            points += 0
        elif 120 <= sys_bp <= 129:
            points += 3
        elif 130 <= sys_bp <= 139:
            points += 4
        elif 140 <= sys_bp <= 159:
            points += 5
        elif sys_bp >= 160:
            points += 6
        else:
            print("Invalid input for systolic blood pressure")
    else:
        print("Invalid input for blood pressure medication")

# female risk

    if points < 9:
        risk = '<1%'
    elif 9 <= points <= 12:
        risk = '1%'
    elif points == 13 or points == 14:
        risk = '2'
    elif points == 15:
        risk = '3%'
    elif points == 16:
        risk = '4%'
    elif points == 17:
        risk = '5%'
    elif points == 18:
        risk = '6%'
    elif points == 19:
        risk = '8%'
    elif points == 20:
        risk = '11%'
    elif points == 21:
        risk = '14%'
    elif points == 22:
        risk = '17%'
    elif points == 23:
        risk = '22%'
    elif points == 24:
        risk = '27%'
    elif points >= 25:
        risk = '>= 30%'
    print('Your 10-year risk of heart attack is ' + risk)

print()
