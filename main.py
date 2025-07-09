from fastapi import FastAPI
from dataclasses import dataclass
# from typing import 

app = FastAPI()

@dataclass
class User:
    name: str
    age: int

# User_name: str = input("Enter your name: ")
# User_age:int = input("Enter your age: ")
# Detail = User(User_name, User_age)

Detail = User("M_Anas", 20)
 
@app.get("/Greet_with_Name")
def Greet_to_all():
    """This is a greeting function that returns a message with the user's name and age."""
    Message = input(f"Hy {Detail.name} What is your hobby in world: ")   
    return {"message": f"Assalamualaikum, {Detail.name}! Your age is {Detail.age} and your hobby is {Message}!"}

@app.get("/Simple_Greeting")
def Knowledge():
    '''This Is a simple greeting function that returns a message with the user's favorite personality.'''
    Message = input("What is your favorite personality in world : ")   
    return {"message": f"Assalamualaikum, {Message}!"}