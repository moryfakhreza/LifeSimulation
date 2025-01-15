import random

class Education:
    def __init__(self):
        self.level = "Toddler"
        self.major = None

    def choose_school(self, age):
        if age < 6:
            print("You are too young for school.")
            return
        levels = ["Elementary School", "Middle School", "High School", "University"]
        if self.level in levels:
            next_level_index = levels.index(self.level) + 1
            if next_level_index < len(levels):
                self.level = levels[next_level_index]
                print(f"You are now in {self.level}")
            else:
                print("You have completed your education.")
        else:
            self.level = levels[0]
            print(f"You are now in {self.level}")

    def choose_major(self):
        if self.level == "University":
            majors = ["Law", "Medicine", "Arts", "Engineering", "Business"]
            self.major = random.choice(majors)
            print(f"You chose to major in {self.major}")
        else:
            print("You need to be in University to choose a major.")