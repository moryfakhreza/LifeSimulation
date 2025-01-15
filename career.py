import random

class Career:
    def __init__(self):
        self.job = None
        self.salary = 0

    def choose_career(self, age):
        if age < 17:
            print("You are too young to start a career.")
            return
        jobs = ["Software Developer", "Doctor", "Artist", "Engineer", "Teacher"]
        self.job = random.choice(jobs)
        self.salary = random.randint(30000, 100000)
        print(f"You got a job as a {self.job} with a salary of ${self.salary} per year.")