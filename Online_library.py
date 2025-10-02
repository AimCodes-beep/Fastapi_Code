from fastapi import FastAPI,Header,Cookie,Form,Query,Path,HTTPException
from pydantic import BaseModel,Field
from typing import Annotated
from fastapi.responses import HTMLResponse

app=FastAPI()
@app.get("/",response_class=HTMLResponse)
async def get_form():
    return """
    <html>
    <body>
    <h1>ONLINE BOOKSTORE </h1>
    <hr>
    <form action="/register/" method="post">
    <label for="book_id">BookID : </label><br>
    <input type="text" id="book_id" name="book_id"><br>
    <label for="book_name">Name : </label><br>
    <input type="text" id="book_name" name="book_name"><br>
    <label for="category">Category : </label><br>
    <input type="text" id="category" name="category"><br>
    <label for="author">Author : </label><br>
    <input type="text" id="author" name="author"><br>
    <label for="price">Price: </label><br>
    <input type="number" id="price" name="price"><br>
    <input type="submit" value="Submit">
    </form>
    </body>
    </html> """

#DEFINING PYDANTIC MODEL FOR FORM DATA
class Book(BaseModel):
    book_id:str
    book_name:str=Field(min_length=4)
    category:str=Field(min_length=4)
    author:str=Field(min_length=4)
    price:int=Field(gt=200)


#CREATING FAKE DB FOR STORING BOOKS DATA
library_data=[]

@app.post("/register/")
async def get_data(book_id:Annotated[str,Form()],book_name:Annotated[str,Form()],category:Annotated[str,Form()],
author:Annotated[str,Form()],price:Annotated[int,Form()]):
    book=Book(book_id=book_id,book_name=book_name,category=category,author=author,price=price)
    library_data.append(book.dict())
    return book

#RETRIVEING BOOK FROM FAKE DATABASE
@app.get("/books")
async def get_books():
    return library_data
#RETRIEVIBG BOOKS BY THEIR ID
@app.get("/get_books/{book_id}")
async def get_single_book(book_id:str):
    if not book_id:
        raise HTTPException(status_code=404,detail="Book not found")
    for bd in library_data:
        if bd["book_id"]==book_id:
         return {"Message":"BOOK RETRIVED","book":bd}
    return {"Message":"Book is not available"}
#SEARCH BOOK BY CATEGORY USING QUERY PARAMETERS
@app.get("/search")
async def get_category(category:Annotated[str,Query(min_length=4,title="Search BY name")]):
      category_name=category.lower()
      for bd in library_data:
          if category_name==bd["category"].lower():
             return {"Message":"BOOK RETREIVED","book":bd}
      return {"Message":"BOOK DOESN'T FOUND"}

#UPDATING BOOK PRICE AFTER EVERY 3 MONTHS
@app.put("/books/{book_id}")
async def update_price(book_id:str,new_price:Annotated[int,Query(gt=100)]):
      for bd in library_data:
        if bd["book_id"]==book_id:
            bd["price"]=new_price
            return {"Message":"BOOK PRICE UPDATED","book":bd,"new_price":new_price}
      return {"Message":"Book don't found!"}

#COOKIE FOR ADMIN LOGIN
@app.get("/cookiyaan")
async def get_cookie(session_id:Annotated[str,Cookie()]):
    if session_id=="aimanm2005":
        return {"Message":"WELCOME ADMIN! YOUR COOKIES ARE READY!🍪🍪🍪"}
    return {"Message":"AUTHENCIATION FAILED YOU WILL NOT GET COOKIES 🍪🍪🍪"}
