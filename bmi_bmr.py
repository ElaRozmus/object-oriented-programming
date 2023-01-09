# -*- coding: utf-8 -*-


import sys

class BmiBmr:
    
    def __init__(self, weight, height, age, gender):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        
    
    def user_data(self):
        """
        This function print all information about user which was input in program
        """
        print("Your parameter is:")
        print(f'Weight: {self.weight} kg')
        print(f'Height: {self.height} cm')
        print(f'Age: {self.age}')
        print(f'Gender:{self.gender}')

    
    def bmi_calculator(self):
        """
        This function count BMI for user
        
        Input: 
            self.weight = weight # int
            self.height = height # int
        
        Output:
            bmi = int
            Information about on ehich level is user's bmi   
        """
        bmi = round(self.weight / (self.height / 100)**2)
        print(f'Your BMI is: {bmi}')
        if bmi <= 16.0 and bmi <= 18.49:
            print("You have underweight")
        elif bmi >= 18.5 and bmi <= 24.99:
            print("Your weight is allright")
        elif bmi >= 25.0 and bmi <= 29.99:
            print("You have obesity")
        elif bmi >= 30.0:
            print("you have obesity")
        
    def bmr_calculator(self):
        """
        This function count BMR value. Counter bmr is different for woman and 
        man.
        
        Input:
            self.weight = weight # int
            self.height = height # int
            self.age = age
            self.gender = gender
        
        Output:
            bmr = int 
        """
        if self.gender == "m":
            menBmr = round(66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age))
            print(f'Your caloric needs is: {menBmr}')
        elif self.gender == "w":
            womenBmr = round(655 + (9.6 * self.weight) + (1.7 * self.height) - (4.7 * self.age))
            print(f'Your caloric needs is: {womenBmr}')


     
    def cpm_calculator(self):
        """
        This function count cpm value. 
        
        Input:
            choose = int
        
        Output:
            cpm = int

        """
        choose = int(input("""please choose yuor activity: 
1 = sedentary lifestyle (you do not show any physical activity)
2 = very little activity (office job, no exercise, some walking)
3 = little activity (no exercise, your work need some light physical effort)
4 = middle activity (regular training)
5 = hight activity (everyday training, you have phisical job or activity lifestyle)
6 = Very high activity (training twice a day, very highly physical job)
Place for you decision: """))
        if self.gender == "m":
            menBmr = round(66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age))
            if choose == 1:
                cpm = menBmr * 1.0
                print(f'Your CPM is: {cpm}')
            elif choose == 2:
                cpm = menBmr * 1.2
                print(f'Your CPM is: {cpm}')
            elif choose == 3:
                cpm = menBmr * 1.4
                print(f'Your CPM is: {cpm}')
            elif choose == 4:
                cpm = menBmr * 1.6
                print(f'Your CPM is: {cpm}')
            elif choose == 5:
                cpm = menBmr * 1.8
                print(f'Your CPM is: {cpm}')
            elif choose == 6:
                cpm = menBmr * 2.0
                print(f'Your CPM is: {cpm}')
        elif self.gender == "w":
            womenBmr = round(655 + (9.6 * self.weight) + (1.7 * self.height) - (4.7 * self.age))
            if choose == 1:
                cpm = womenBmr * 1.0
                print(f'Your CPM is: {cpm}')
            elif choose == 2:
                cpm = womenBmr * 1.2
                print(f'Your CPM is: {cpm}')
            elif choose == 3:
                cpm = womenBmr * 1.4
                print(f'Your CPM is: {cpm}')
            elif choose == 4:
                cpm = womenBmr * 1.6
                print(f'Your CPM is: {cpm}')
            elif choose == 5:
                cpm = womenBmr * 1.8
                print(f'Your CPM is: {cpm}')
            elif choose == 6:
                cpm = womenBmr * 2.0
                print(f'Your CPM is: {cpm}')
                


gender = input("""choose m for a man
w for a woman: >>> """).lower()

weight = int(input("Please enter your weight: >>>"))
height = int(input("Please enter you height: >>>"))
age = int(input("Please enter you age: >>>"))

user = BmiBmr(weight, height, age, gender)

while True:
    print("Enter 1 to display your details")
    print("Enter 2 to calculate BMI calculator")
    print("Enter 3 to calculate your BMR")
    print("Enter 4 to calculate cpm")
    print("Enter 5 to exit the program")
    
    user_choose = int(input(" >>> "))
    if user_choose == 1:
        user.user_data()
    elif user_choose == 2:
        user.bmi_calculator()
    elif user_choose == 3:
        user.bmr_calculator()
    elif user_choose == 4:
        user.cpm_calculator()
    elif user_choose == 5:
        print("Goodbye")
        sys.exit()
# %%

