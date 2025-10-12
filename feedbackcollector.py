from fastapi import FastAPI,Path,Query,Cookie,Header,Form,File,UploadFile
from pydantic import BaseModel,Field
from typing import Annotated
from fastapi.responses import HTMLResponse

app=FastAPI()
@app.get("/",response_class=HTMLResponse)
async def show_feedback():
    return """<html>
       <body>
       <h1>User Feedback Form</h1>
       <p>Collecting user feedback to improve our services</p>
       <form action="/feedback/"  enctype="multipart/form-data" method="post">
       <label for="name">Name :</label><br> <br>
       <input type="text" id="name" name="name"><br> <br>
       <label for="email">Email: </label><br> <br>
       <input type="text" id="email" name="email"><br> <br>
       <label for="message">Message :</label><br> <br>
       <input type="text" id="message" name="message"><br> <br>
       <label for="pfp">Profile Pic:</label><br> <br>
       <input type="file" id="pfp" name="pfp" accept="image/*"><br> <br>
       <input type="submit" value="Submit feedback">
       </form>
       </body>
       </html> """

#CREATING FAKE DB FOR STORING FEEDBACKS AND DATA
fd=[]
@app.post("/feedback/")
async def get_feedback(name:Annotated[str,Form()],email:Annotated[str,Form()],message:Annotated[str,Form()],pfp:Annotated[UploadFile,File()]):
    fd.append({"name":name,"email":email,"message":message,"pfp":pfp.filename})
    return {"Message":"Feedback Submitted","name":name,"email":email,"message":message,"pfp":pfp.filename}

#RETRIVING ALL FEEDBACKS
@app.get("/all_feedback")
async def feedbacks():
    return fd
#RETRIVING FEEDBACKS ON SEARCHED EMAILS
@app.get("/email")
async def searched(email:Annotated[str,Query()]):
    for f in fd:
        if email==f["email"]:
            return {"User_Email":f}
    return {"Message":"Email don't found"}