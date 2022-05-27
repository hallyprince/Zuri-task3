from ast import Return


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        print("The student new name is" , change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print("The student new age is" , change_age)

    def add_tracks(self, add_tracks):
        self.change_tracks = add_tracks
        print("The student new tracks is" , add_tracks)

    def get_score(self):
        print(f"Bob scored, {self.score} marks" )
        
        

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.99)
        
# Expected methods
Bob.change_name("Paul")
Bob.change_age(40)
Bob.add_tracks("frontend design")
Bob.get_score()

