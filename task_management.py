from fastapi import FastAPI,Form,Path,Query,Cookie,Response,File,UploadFile,BackgroundTasks,HTTPException,Depends ,Header #ESSENTIALS REQUIREMENTS
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
app=FastAPI()
#DEPENDENCY TO GET TASKS DATA
def token_header(admin_name:Annotated[str,Header()]):
    if admin_name!="aimcodes4":
        raise HTTPException(status_code=404,detail="Acesss can't granted to others")

#1ST BACKGROUND TASKS TO SAVE THE DATA
def save_data(task_name:str,Description:str,Category:str):
    content=f"Taskname:{task_name},Description:{Description},Category:{Category}"
    with open("Task_details.txt",'a') as f:
        f.write(content)

#2ND BACKGROUND TASKS TO SAVE THE USERS FILE
def save_file(filename:str,file_content:bytes):
    os.makedirs("tasks_files",exist_ok=True) #MAKING DIRECTORIES
    with open(f"tasks_files/{filename}","wb") as f: #SAVE CONTENT UPLOADED BY USER
        f.write(file_content)
#ROUTE TO RELOCATE THE FORM
@app.get("/",response_class=HTMLResponse)
async def get_data():
    return """
     <html>
    <body style="background-color:black;color:white;text-align:center;font-size:16px;">
    <h1>TASK UPLOADER API </h1> <hr>
    <p>Welcome to Task Management </p>
    <hr>
    <form style="display:flex; flex-direction:column; justify-content:center; flex-wrap:wrap;" action="/upload/"  method="post" enctype="multipart/form-data">
    <label for="name"> Task Name: </label><br>
    <input style="padding:2px; margin:2px auto;" type="text" id="name" name="name"><br>
    <label for="Description">Task Description </label><br>
    <input style="padding:2px; margin:2px auto;" type="text" id="Description" name="Description"><br>
    <label for="Category">Category </label><br>
    <input style="padding:2px; margin:2px auto;" type="text" id="Category" name="Category"><br>
    <label for="Status">Status </label><br>
    <input style="padding:2px; margin:2px auto;" type="text" id="Status" name="Status"><br>
    <label for="email">Email</label><br>
    <input style="padding:2px; margin:2px auto;" type="text" id="email" name="email"><br>
    <label for="file">Upload Task Image/File: </label> <br>
    <input style="padding:2px; margin:2px auto;" type="file" id="file" name="file"> <br>
    <input style="padding:2px; margin:2px auto;" type="submit" value="Submit"> 
    </form>
    </body>


"""
tasks=[] #FAKE DB TO STORE THE DATA


@app.post("/upload/")
async def get_task_data(name:Annotated[str,Form()],Description:Annotated[str,Form()],Category:Annotated[str,Form()],Status:Annotated[str,Form()],email:Annotated[str,Form()],file:Annotated[UploadFile,File()],background_tasks:BackgroundTasks):
    file_content=await file.read()
    tasks.append({"name":name,"Description":Description,"Category":Category,"Status":Status,"Email":email})
    background_tasks.add_task(save_data,name,Description,Category)
    background_tasks.add_task(save_file,file.filename,file_content)
    return {"Message":"TASKS DATA","name":name,"Description":Description,"Category":Category,"Status":Status,"Email":email,"file":file.filename}

#ONLY ADMIN CAN SEE ALL TASKS
@app.get("/all_tasks")
async def get_all_data(token: Annotated[str, Depends(token_header)]):
    return tasks

#SEARCH BY TASKS NAMES
@app.get("/tasks")
async def get_task_by_name(name:Annotated[str,Query(min_length=3)]):
    name_lower=name.lower()
    for t in tasks:
        if name_lower==t["name"].lower():
            return {"Message":"Task Retreived","task":t}
    return {"Message":"Tasks not found"}

#SEARCH BY CATEGORY
@app.get("/taskss")
async def get_task_by_name(Category:Annotated[str,Query(min_length=3)]):
    category_lower=Category.lower()
    for t in tasks:
        if category_lower==t["Category"].lower():
            return {"Message":"Task Retreived","task":t}
    return {"Message":"Tasks not found"}

#COOKIES SET
@app.get("/set_cookie")
async def set_cookies(name:str,response:Response):
    response.set_cookie(
        key="username",
        value=name,
        httponly=True,
        max_age=3600

    )
    return {"Message":f"{name} Cookie save successfully 🍪🍪🍪🍪"}

@app.get("/whoima")
async def get_cookie(username:Annotated[str|None,Cookie()]=None):
    if username:
        return {"Message":f"{username} your cookies are ready !🍪🍪🍪🍪 "}
    return {"Message":"PLz provide a username to get cookies 🍪🍪🍪🍪"}
