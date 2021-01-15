import sys
from bmi_calculation import Bmi
from user_input import UserInput
from bmi_category import BmiCategroy


class BmiEngine:
    def __init__(self):
        pass

    input = UserInput()
    category = BmiCategroy()


    def start_bmi(self):

        gender = self.getGender()

    

        height, height_unit = self.getHeight()

        weight = self.getWeight()

        bmi_ = self.bmi.calculate_bmi(height, height_unit, weight)
        print("Your BMI: %s" % bmi_)


        bfp_category = self.bmi.body_fat_category(_bfp=bfp, _gender=gender)
        print("Boby Fat Percentage Category: %s" % bfp_category)


bmi_engine = BmiEngine()
bmi_engine.start_bmi()
