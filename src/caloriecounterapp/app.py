from string import ascii_lowercase, ascii_uppercase, digits

import toga
from toga.constants import COLUMN, ROW
from toga.style import Pack


food_headings = ['Food Name','Calories Per Serving','Food Group']

athlete_headings = ['Name','Sex','Exercise Level','Age','Height(cm)','Weight(kg','Calorie Target']

athletes = [()]

food_groups = [
    'Select','Breads', 'Cereals', 'Rice', 'Pasta', 'Vegtables', 
    'Fruit', 'Milk', 'Cheese', 'Meat', 'Fish', 'Poultry', 'Eggs'
]
food_items = [()]


class Athlete:
    
    def __init__(self, name, sex, exerciselevel, age, height, weight):
        self.name = name
        self.sex = sex
        self.exerciselevel = exerciselevel
        self.age = age
        self.height = height
        self.weight = weight
    

    #https://www.integrativepro.com/en/articles/how-to-determine-caloric-intake-needs
    def get_exerciselevel(self,exerciselevel):
        if exerciselevel=="Little-to-None":
            return 1.2
        elif exerciselevel=="Light":
            return 1.375
        elif exerciselevel=="Moderate":
            return 1.55
        elif exerciselevel=="Heavy":
            return 1.725
        else:
            return 1.725


    def get_BMR(self,sex,age,height,weight):
        if sex=="Male":
            return (10.0 * float(weight)) + (6.25 * float(height)) - (5.0 * float(age)) + 5.0
        elif sex == "Female":
            return (10.0 * float(weight)) + (6.25 * float(height)) - (5.0 * float(age)) - 161
        else:
            return "error"

    def get_daily_cal_target(self,bmr,exercise_level):
        return bmr * exercise_level

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
        

        #trying new table approach with table source example.
        self.table1 = toga.Table(
            headings = athlete_headings,
            data = athletes,
            style =Pack(flex=1),
            
        )

        self.table2 = toga.Table(
            headings = food_headings,
            data = food_items,
            style =Pack(flex=1),
        
        )
        
                
        self.nameinput = toga.TextInput(
                            on_change=self.name_select,

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
                            "Athlete's name:",
                            style=label_style,
                        ),
                        self.nameinput
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
                        #toga.Table(athlete_headings,data=athletes),
                        self.table1,
                    ],
                ),
                   
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
                        #toga.Table(food_headings,data=food_items),
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
        #everything is above this
        self.main_window.show()
#added a way to accept the name
    def name_select(self, selection):
        athlete_name = selection.value       
    
    def sex_select(self, selection):
        #global sex
        sex = selection.value
        
    def exercise_level_select(self, selection):
        #global exercise_level
        exercise_level = selection.value     

    def age_select(self, selection):
        #global age
        age = selection.value

    def height_select(self, selection):
        #global height
        height = selection.value

    def weight_select(self, selection):
        #global weight
        weight = selection.value

    def food_name_select(self, selection):
        #global food_name
        food_name = selection.value

    def calories_per_serving_select(self, selection):
        #global calories_per_serving
        calories_per_serving = selection.value
    
    def food_category_select(self, selection):
        #global food_category
        food_category = selection.value


    # creating a new athlete  -- I think this goes in Athlete class, but cannot see how

    def add_new_athlete(self, selection):
        #name = self.nameinput.value
        #sex  = self.sexinput.value
        #exerciselevel = self.exerciselevel.value
        #age = self.ageinput.value
        #height = self.heightinput.value
        #weight = self.weightinput.value
        #athlete = Athlete(name,sex,exerciselevel,age,height,weight)
        athlete = Athlete(self.nameinput.value,self.sexinput.value,self.exerciselevel.value,self.ageinput.value, self.heightinput.value,self.weightinput.value)
        exercise_factor = athlete.get_exerciselevel(athlete.exerciselevel)
        bmr = athlete.get_BMR(athlete.sex, athlete.age, athlete.height, athlete.weight)
        athlete.daily_cal_target = athlete.get_daily_cal_target(bmr,exercise_factor)

        self.table1.data.insert(1,athlete.name, athlete.sex, int(athlete.age), int(athlete.height),int(athlete.weight),athlete.exerciselevel,athlete.daily_cal_target)
        print(athletes)

    def add_new_food(self, selection):  
        #food = self.newfoodinput.value
        #cal = self.calperserv.value
        #foodcat = self.foodcat.value
        food = Food(self.newfoodinput.value, self.calperserv.value, self.foodcat.value)
        #print(foodcat)
        #print(cal)
        #print(newfood)
        self.table2.data.insert(1,food.food_name, int(food.cal_per_serving), food.food_category)
        print(food_items)
        food_items.append((food.food_name, int(food.cal_per_serving), food.food_category))
        print(food_items)
        
def main():
    # App name and namespace
    return CalorieCounterApp("Selection", "org.beeware.selection")