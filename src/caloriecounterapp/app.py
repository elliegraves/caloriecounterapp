from string import ascii_lowercase, ascii_uppercase, digits

import toga
from toga.constants import COLUMN, ROW
from toga.style import Pack


food_headings = ['Food Name','Calories Per Serving','Food Group']

athlete_headings = ['First Name', 'Last Name', 'Sex','Exercise Level','Age','Height(cm)','Weight(kg','Calorie Target',]

food_groups = [
    'Select','Breads', 'Cereals', 'Rice', 'Pasta', 'Vegtables', 
    'Fruit', 'Milk', 'Cheese', 'Meat', 'Fish', 'Poultry', 'Eggs'
]

class Athlete:
    
    def __init__(self, first_name, last_name, sex, exerciselevel, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.exerciselevel = exerciselevel
        self.age = age
        self.height = height
        self.weight = weight

    

    @property
    def magic(self):
       return self.age * self.height

    @property
    def fullname(self):
        return'{} {}'.format(self.first_name, self.last_name)

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name
    @property
    def exercisefactor(self):
        if self.exerciselevel=="Little-to-None":
            return 1.2
        elif self.exerciselevel=="Light":
            return 1.375
        elif self.exerciselevel=="Moderate":
            return 1.55
        elif self.exerciselevel=="Heavy":
            return 1.725
        else:
            return 1.725

    @property
    def BMR(self):
        if self.sex=="Male":
            return (10.0 * float(self.weight)) + (6.25 * float(self.height)) - (5.0 * float(self.age)) + 5.0
        elif self.sex == "Female":
            return (10.0 * float(self.weight)) + (6.25 * float(self.height)) - (5.0 * float(self.age)) - 161
        else:
            return "error"
    @property
    def daily_cal_target(self):
        return self.bmr * self.exercisefactor

class Food:
    
    def __init__(self, food_name, cal_per_serving, food_category):
        self.food_name = food_name
        self.cal_per_serving = cal_per_serving
        self.food_category = food_category

class CalorieCounterApp(toga.App):
    
    def startup(self):
        
       
        # Main window of the application with title and size
        self.main_window = toga.MainWindow(title=self.name, size=(640, 400))

        # set up common styles
        label_style = Pack(flex=1, padding_right=24)
        box_style_1 = Pack(direction=ROW, padding=10)
        box_style_2 = Pack(direction=COLUMN, padding=10)
        

        #creatig the tables 
        self.table1 = toga.Table(
            headings = ['First Name', 'Last Name', 'Sex','Exercise Level','Age','Height(cm)','Weight(kg','Calorie Target',],
            accessors = ["first_name", "last_name", "sex", 'exerciselevel', 'age', 'height','weight', 'daily_cal_target',],
            style =Pack(flex=1)
        )

        self.table2 = toga.Table(
            headings = food_headings,
            style =Pack(flex=1),
        
        )
        
                

        self.first_name_input = toga.TextInput(
                            on_change=self.first_name_select,

                        )
        self.last_name_input = toga.TextInput(
                            on_change=self.last_name_select,

                        )   
        self.sexinput = toga.Selection(
                            on_select=self.sex_select,
                            items=["Select", "Female", "Male"],
                        )   
        self.exerciselevel = toga.Selection(
                            on_select=self.exercise_level_select,
                            items=["Select", "Little-to-None","Light","Moderate","Heavy","Very Heavy"],
                        )       
        self.ageinput = toga.NumberInput(
                            min_value = 1,
                            max_value = 110,
                            on_change = self.age_select
                        )
        self.heightinput = toga.NumberInput(
                            min_value = 90,
                            max_value = 500,
                            on_change = self.height_select,
                        )
        self.weightinput = toga.NumberInput(
                            min_value = 90,
                            max_value = 500,
                            on_change = self.weight_select,
                        )
        self.newfoodinput = toga.TextInput(
                            on_change = self.food_name_select,
                        )
        self.calperserv = toga.NumberInput(
                            min_value = 1,
                            max_value = 110,
                            on_change = self.calories_per_serving_select,
                        )
        self.foodcat = toga.Selection(
                            on_select=self.food_category_select,
                            items = food_groups
                        )

        self.box = toga.Box(
            children=[
                #Welcome message
                toga.Box(
                    style=box_style_2,
                    children=[
                        toga.Label(
                            "Hello! Welcome to the Calorie Counter",
                            style=label_style,
                        ),
                        toga.Divider(style=Pack(direction=COLUMN, flex=1, padding=20)),
                    ],
                ),
                #athlete information
                toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Athlete's first name:",
                            style=label_style,
                        ),
                        self.first_name_input
                    ],
                ),
                toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Athlete's last name:",
                            style=label_style,
                        ),
                        self.last_name_input
                    ],
                ),
               
                toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Athlete's sex:",
                            style=label_style,
                        ),
                        self.sexinput  
                    ],
                ),

                toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Athlete's exercise level:",
                            style=label_style,
                        ),
                        self.exerciselevel
                    ],
                ),

                toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Athlete's age:",
                            style = label_style,
                            
                        ),
                        self.ageinput

                    ],
                ),

                toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Athlete's height(cm):",
                            style = label_style,
                            
                        ),
                        self.heightinput
                    ],
                ),

                toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Athlete's weight(kg):",
                            style = label_style,
                            
                        ),
                        self.weightinput

                    ],
                ),

                toga.Button(
                    "Add Athlete",
                    on_press=self.add_new_athlete,
                ),

                toga.Box(
                    style=box_style_2,
                    children=[
                        toga.Divider(style=Pack(direction=COLUMN, flex=1, padding=20)),
                        self.table1,
                    ],
                ),
               # Food section    
                toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Enter new food :",
                            style = label_style,
                            
                        ),
                    self.newfoodinput
                        
                    ],
                ),

                toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Enter calories per serving of food:",
                            style = label_style,    
                        ),
                    self.calperserv

                    ],
                ),

                 toga.Box(
                    style=box_style_1,
                    children=[
                        toga.Label(
                            "Please select a food category",
                            style=label_style,
                        ),
                    self.foodcat    
                    ],
                ),
                
                toga.Button(
                    "Add Food",
                    on_press=self.add_new_food,
        
                ),

                toga.Box(
                    style=box_style_2,
                    children=[
                        toga.Divider(style=Pack(direction=COLUMN, flex=1, padding=20)),
                        self.table2
                    ],
                ),
                toga.Box(
                    style=box_style_2,
                    children=[
                        toga.Label(
                            "Let's build a food",
                            style=label_style,
                        ),
                        toga.Divider(style=Pack(direction=COLUMN, flex=1, padding=20)),
                    ],
                ),

                
            ],
            style=Pack(direction=COLUMN, padding=24),
        )
#Placing the box in a scroller
        scroller = toga.ScrollContainer(horizontal=False)
        scroller.content = self.box
        self.main_window.content = scroller
        self.main_window.show()

#Functions to get the users selections and assign to variables.        
    def first_name_select(self, selection):
        first_name = selection.value   

    def last_name_select(self, selection):
        last_name = selection.value

    def sex_select(self, selection):
        sex = selection.value
        
    def exercise_level_select(self, selection):
        exercise_level = selection.value     

    def age_select(self, selection):
        age = selection.value

    def height_select(self, selection):
        height = selection.value

    def weight_select(self, selection):
        weight = selection.value

    def food_name_select(self, selection):
        food_name = selection.value

    def calories_per_serving_select(self, selection):
        calories_per_serving = selection.value
    
    def food_category_select(self, selection):
        food_category = selection.value

    def add_new_athlete(self, selection):
#creating an athlete instance using the staging stuff we've collected.
        athlete = Athlete(self.first_name_input.value, self.last_name_input.value,self.sexinput.value,self.exerciselevel.value,self.ageinput.value, self.heightinput.value,self.weightinput.value)
        '''bmr = athlete.get_BMR(athlete.sex, athlete.age, athlete.height, athlete.weight)
        athlete.daily_cal_target = athlete.get_daily_cal_target(bmr,exercise_factor)
    '''
        self.table1.data.insert(0,athlete)

    def add_new_food(self, selection):  
        food = Food(self.newfoodinput.value, self.calperserv.value, self.foodcat.value)

        self.table2.data.insert(0,food.food_name, int(food.cal_per_serving), food.food_category)

        
    e = Athlete("Ellie", "Graves", "Female", "Heavy", 16, 68, 100)
    print(e.magic)
    print(e.fullname)
    e.fullname = 'Mickey Mouse'
    print(e.first_name)
def main():
    # App name and namespace
    return CalorieCounterApp("Selection", "org.beeware.selection")