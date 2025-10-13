from fastapi import FastAPI,BackgroundTasks,Form,File,UploadFile,Cookie,Path,Query,Response
from pydantic import BaseModel,Field,EmailStr
from fastapi.responses import HTMLResponse
from typing import Annotated
from app.users.router import router as user_router
import os
app=FastAPI()

users=[]
class User(BaseModel): #DEFINING THE STRUCTURE OF DATA
    name:str=Field(min_length=4)
    age:int=Field(gte=18,lte=60)
    city:str=Field(min_length=4)
    email:EmailStr
    password:str=Field(min_length=8)


#BACKGROUND TASKS
def write_info(email:str):
    with open('usersss.txt','a') as f: #SAVE USER EMAIL FOR FUTURE USES
        content=f"Email of user {email}\n"
        f.write(content)

#2ND BACKGROUND TASKS
def save_file(filename:str,file_content:bytes):
    os.makedirs("uploads",exist_ok=True) #MAKING DIRECTORIES
    with open(f"uploads/{filename}","wb") as f: #SAVE CONTENT UPLOADED BY USER
        f.write(file_content)

#THE MAIN PART GETTING INFORMATION FROM CLIENT
@app.get("/",response_class=HTMLResponse)
async def get_data():
    return """
    <html>
    <body style="background-color:black;color:white;text-align:center;font-size:16px;">
    <h1>User Registration Form </h1> <hr>
    <p>Welcome to Express Flights </p>
    <hr>
    <form style="display:flex; flex-direction:column; justify-content:center; flex-wrap:wrap;" action="/register/"  method="post" enctype="multipart/form-data">
    <label for="name">Name: </label><br>
    <input style="padding:2px; margin:2px auto;" type="text" id="name" name="name"><br>
    <label for="age">Age: </label><br>
    <input style="padding:2px; margin:2px auto;" type="number" id="age" name="age"><br>
    <label for="city">City: </label><br>
    <input style="padding:2px; margin:2px auto;" type="text" id="city" name="city"><br>
    <label for="email">Email: </label><br>
    <input style="padding:2px; margin:2px auto;" type="text" id="email" name="email"><br>
    <label for="password">Password: </label><br>
    <input style="padding:2px; margin:2px auto;" type="text" id="password" name="password"><br>
    <label for="file">Upload Image: </label> <br>
    <input style="padding:2px; margin:2px auto;" type="file" id="file" name="file"> <br>
    <input style="padding:2px; margin:2px auto;" type="submit" value="Submit"> 
    </form>
    </body>
    </html> """



@app.post("/register/")
async def create_user(name:Annotated[str,Form(min_length=3)],age:Annotated[int,Form(gte=18,lte=60)],city:Annotated[str,Form(min_length=4)],email:Annotated[str,Form()],password:Annotated[str,Form(min_length=8)],file:Annotated[UploadFile,File()],background_tasks:BackgroundTasks):
    file_content = await file.read()
    users.append({"name":name,"age":age,"city":city,"email":email,"password":password})
    background_tasks.add_task(write_info,email)#saving email info
    background_tasks.add_task(save_file,file.filename,file_content) #saving files uploaded by user
    return {"Message":"User created","name":name,"asge":age,"city":city,"email":email,"password":password,"filename":file.filename}
#ROUTERS
app.include_router(user_router,tags=["User_data"])
@app.get("/set_cookie")
async def set_cookies(name:Annotated[str,Query()],response:Response):
    response.set_cookie(
        key="User",
        value=name,
        httponly=True,
        max_age=3600 #Exists for hour
    )
    return {"Messafe":"Cookie are ready 🍪🍪🍪🍪 !!!"}


    

