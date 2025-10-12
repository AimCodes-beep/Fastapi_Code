from fastapi import FastAPI,Path,Query,Cookie,Header
from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,List
app=FastAPI()
users=[
    {"id":"U1001","name":"Areeba Zulfiqar","course":"QA"},
    {"id":"U1002","name":"Laiba Jabbar","course":"DS"},
    {"id":"U1003","name":"Alfaid","course":"CS"},
    {"id":"U1004","name":"Adnan","course":"SWE"}
]
@app.get("/users/{user_id}")
async def retrive_user(user_id:str):
      for u in users:
        if u["id"]==user_id:
            return {"Message":"User Retrieved","user":u}
      return {"Message":"User don't exist"}
#QUERY QUESTION
@app.get("/user")
async def search_by_name(name:Annotated[str,Query(min_length=3)]):
      name_lower=name.lower()
      for u in users:
        if name_lower==u["name"].lower():
            return {"Message":"User_found","user":u}
      return {"Message":"USER DON;T EXISTS"}
#PYDANTIC MODEL AND VALIDATIONS
class Product(BaseModel):
      id:int=Field(ge=100,le=1000)
      name:str=Field(min_length=3,title="Product Name")
      price:float=Field(ge=1.0)
products=[]
@app.post("/products")
async def create_product(product:Product):
      products.append(product.dict())
      return {"Message":"PRODUCT CREATED SUCCESSFULLY","product":product}
#COOKIES
@app.get("/Profile")
async def login_in(session_id:Annotated[str|None,Cookie()]=None):
      if session_id:
        return {"Message":"COOKIE SET","cookie":session_id}
      return {"Messsage":"PLZ PROVIDE A COOKIE 🍪"}
"""@app.get("/login")
async def login(response: Response):
    # Normally, you would validate username/password here
    session_id = "ABC123XYZ"   # Fake session_id (can be JWT or random string)
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    return {"message": "Login successful! Cookie has been set."} """
@app.get("/secure_data")
async def security(x_api_key:Annotated[str,Header()]):
      if x_api_key=="SECRET123":
        return {"Message":"ACCESSS GRANTED"}
      return {"Message":"ACCESS DENIED!"}
#RESPONSE MODEL
class Student(BaseModel):
     id:int=Field(gt=1000)
     name:str=Field(min_length=3,title="NAME OF STUDENT")
     age:int=Field(le=18,ge=30)
     email:EmailStr
@app.post("/students",response_model=Student)
async def create_student(student:Student):
    return student
#RETURN TYPE WITH PYDANTIC MODEL
employees=[]
class Employee(BaseModel):
    id:int
    name:str=Field(min_length=3)
    salary:float
@app.post("/employees")
async def create_employees(employee:Employee) -> Employee:
      employees.append(employee.dict())
      return employee
@app.get("/employeess")
async def get_employees()->List[Employee]:
    return employees
#FILTERING OUT 
class Car(BaseModel):
    id:int
    brand:str
    price:float
    engine_number:str
class Carout(BaseModel):
    brand:str
    engine_number:str
@app.post("/Cars")
async def create_car(car:Car)->Carout:
    return car
#MINI SMALL CHALLENGE
class Orders(BaseModel):
    order_id:int
    product:str
    quantity:int=Field(ge=1)
    price:float=Field(gt=100.0)
class OrderOut(BaseModel):
    order_id:int
    total_price:float
@app.post("/orders")
async def take_order(order:Orders) -> OrderOut:
    total=order.quantity*order.price
    return {"order_id":order.order_id,"name":order.product,"total_price":total}