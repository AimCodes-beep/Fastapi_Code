from fastapi import FastAPI,Request,Form 
from pydantic import BaseModel
from typing import Annotated
from fastapi.responses import HTMLResponse
app=FastAPI()
@app.get("/",response_class=HTMLResponse)
async def get_data():
    return """
    <html>
    <body>
    <h1>HobNob App</h1>
    <h2>Login Form </h2>
    <form action="/login/" method="post">
    <label for="username">Name : </label><br>
    <input type="text" id="username" name="username"> <br> <br>
    <label for="email">Email :</label><br>
    <input type="text" id="email" name="email"><br>
    <label for="pwd">Password :</label><br>
    <input type="text" id="pwd" name="pwd"><br>
    <input type="submit" value="Submit">
    <p>Thanks!</p>
    </form>
    <form action="/feedback/" method="post">
    <label for="feedback"> ENTER YOUR FEEDBACK HERE </label>
    <input type="text" id="feedback" name="feedback">
    <input type="submit" value="Submit">
    </form>
    </body>
    </html> """
@app.post("/login/")
async def get_data(username:Annotated[str,Form()],email:Annotated[str,Form()],pwd:Annotated[str,Form()]):
    if username=="admin" and pwd=="admin1234":
        return {"Message":"WELCOME! ADMIN","username":username,"email":email,"password":pwd}
    return {"Message":"Login Successfully ","username":username,"email":email,"password":pwd}
@app.post("/feedback/")
async def get_feedback(feedback:Annotated[str,Form()]):
    return {"Message":"THANKYOU FOR SUBMITTING YOUR FEEDBACK","feedback":feedback}