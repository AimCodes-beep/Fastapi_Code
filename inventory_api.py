#IMPORTING THE FUNCTIONS WE NEED
from fastapi import FastAPI,Path,Query,Depends,Form,File,UploadFile,BackgroundTasks,HTTPException
from pydantic import BaseModel,EmailStr,Field
from enum import Enum
from typing import Annotated,List
from fastapi.responses import HTMLResponse
#CREATING FASTAPI INSTANCE
app=FastAPI()
#fake db
products=[
    {"id":1111,"name":"Novella","price":888.00,"stock":100},
    {"id":1112,"name":"Chocolato","price":88.00,"stock":100},
    {"id":1113,"name":"Youandme","price":100.00,"stock":100},
    {"id":1114,"name":"Smarties","price":188.00,"stock":100},
    {"id":1115,"name":"Hobie","price":18.00,"stock":10},
    {"id":1116,"name":"Kurkure","price":70.00,"stock":60},
    {"id":1117,"name":"Twich","price":99.99,"stock":6},
    {"id":1118,"name":"Lays","price":66.00,"stock":20},
    {"id":1119,"name":"Nutella","price":1000.00,"stock":35},
    {"id":1110,"name":"Buttons","price":29.99,"stock":77}
]
#PYDANTIC MODEL FOR POST REQUESTS
class Product(BaseModel):
    id:int=Field(gt=1000) #ADDING VALIDATIONS
    name:str
    price:float
    stock:int=Field(gt=0)
class Orders(BaseModel):
    id:int
    products:List[Product]
#FORM FOR TAKING INPUT FROM WEBSITE WHICH PRODUCT SHOULD WE ADD IN OUR CATALOG,CUSTOMER SUGGESTION
@app.get('/',response_class=HTMLResponse)
async def get_data():
    return """
    <html>
    <head>
    <title>INVENTORY API </title>
    <style>
    body{
    background-color:black;
    color:white;
    display:grid;
    align-items:center;
    }
    </style>
    </head>
    <body>
    <h1>INVENTORY API </h1>
    <p>Enter your Product sugggestion below </p>
    <form action='/submit' method="post">
    <label for="cname"> Customer name:</label> <br> <br>
    <input type="text" id="cname" name="cname"> <br> <br>
    <label for="name">Product Name:</label> <br> <br>
    <input type="text" id="name" name="name"> <br> <br>
    <label for="price">Your Desired Price:</label> <br> <br>
    <input type="text" id="price" name="price"> <br> <br>
    <input type="submit" value="Submit">
    </form>
    </body>
    </html>
"""
#BACKGROUND TASK FOR SAVING THE PRODUCT DATA,SUGGESTED BY CUSTOMER
def save_data(cname:str,name:str):
    content=f'Customer {cname} gave this Product suggestion {name}\n'
    with open('CS_suggestion.txt','a') as f:
        f.write(content)
    
#POSTING FORM DATA
@app.post('/submit')
async def do(cname:Annotated[str,Form()],name:Annotated[str,Form()],price:Annotated[float,Form()],b1:BackgroundTasks):
    b1.add_task(save_data,cname,name)
    return {"M4sssage":"THANKYOU FOR YOUR VALUABLE SUGGESTION","Customer_name":cname,"Product_Name":name,"Price":price}

#CRUD
#ADMIN
def adminn(name:str):
    if name != "Aiman":
        raise HTTPException(status_code=401, detail="Access not granted")
    return name
@app.get('/get_all_products')
async def show_inventory(name:str=Depends(adminn)):
    return products

@app.get('/single/{id}')
async def get_pp(id:int):
    for p in products:
        if p["id"]==id:
            return {"Message":"Product Found!!!","p":p}
    return {"Messsage":"Product not found!"}
@app.post('/create_pp')
async def create_product(pro:Product):
    #appending into db
    products.append({"id":pro.id,"name":pro.name,"price":pro.price,"stock":pro.stock})
    return {"Message":"Product created succesfy=ully"}
#create orders
@app.post('/create_order')
async def create_order(oi:Orders):
    return oi
#GET APIS
@app.get('/check_stock/{id}')
async def check_stock(id:int):
    for p in products:
        if p["id"]==id:
            if p["stock"]<20:
                return {"message":"STOCK NEED TO BE UPDATED"}
            else:
                return {"Message":"SUFFICIENT STOCK IS AVAILABLE"}
    return {"mESSAGE":"pp not found"}
@app.get('/check_price/{id}')
async def check_price(id:int):
    for p in products:
        if p["id"]==id:
            if p["price"]>600.00:
                return {"message":"COSTLY PRODUCT"}
            elif p["price"]>200.00:
                return {"message":"Reasonabel PRODUCT"}
            else:
                return {"message":"SASTAAA HY"}
    return {"Message":"PRODUCT NHI MILAA YRR"}
#UPDATE
@app.put('/update_price/{id}')
async def up_pp(id:int,new_pp:float):
     for p in products:
        if p["id"]==id:
            p["price"]=new_pp
        return {"message":"Price updated","pro":p}
     return {"Message":"Product not found"}
#DEL
#TEMPORARY REMOVE PRODUCTS WHICH ARE OUT OF STOCK
@app.delete('/del/{id}')
async def delete(id:int):
      for p in products:
        if p["id"]==id:
            if p["stock"]<0:
                return {"Message":"Product out of stock"}
      return {"Messafe":"PP NOT found"}