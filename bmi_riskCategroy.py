class BmiCategroy:
    def __init__(self):
        pass

    def bmi_category(self, bmi):
        if bmi < 18.4:
            print('Malnutrition Risk')
        elif bmi > 18.5 and bmi < 24.9:
            print('Low risk')
        elif bmi > 25.0 and bmi < 29.9 :
            print('Enhanced risk')
        elif bmi > 30.0 and bmi < 34.9:
            print('Medium Risk')
        elif bmi > 35.0 and bmi < 39.9:
            print('High Risk')
        elif bmi > 40:
            print('Very High Risk')
