from fastapi import FastAPI,Path,Query,Form 
from fastapi.responses import HTMLResponse
from pydantic import BaseModel,Field,EmailStr
from typing import Annotated
app=FastAPI()
@app.get("/",response_class=HTMLResponse)
async def get_form():
    return """
      <html>
      <body>
      <h1>SIGN UP FORM </h1>
      <form action="/login/" method="post">
      <label for="name">Name: </label> <br>
      <input type="text" id="name" name="name"> <br>
      <label for="age">Age : </label> <br>
      <input type="text" id="age" name="age"> <br>
      <label for="Email">Email : </label> <br>
      <input type="text" id="Email" name="Email"> <br>
      <label for="password">Password : </label> <br>
      <input type="text" id="password" name="password"> <br>
      <input type="submit" value="Submit">
      </form>
      </body>
      </html>
      """
class User_SignUp(BaseModel):
    name:str=Field(min_length=3)
    age:str
    email:str
    password:str


@app.post("/login/")
async def create_enrolments(data:Annotated[User_SignUp,Form()]):
    return data
