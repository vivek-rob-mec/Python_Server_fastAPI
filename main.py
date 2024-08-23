# from fastapi import FastAPI
# from pydantic import BaseModel

# class custom(BaseModel):
#     name: str
#     age: int

# app = FastAPI() # create an instance of FastAPI class
# # The app instance is the main component of our FastAPI application. It is used to configure the application

# @app.get('/ping')
# # /ping is the path of the endpoint
# # the endpoint is a URL that our application will listen to
# # 'get' is the http method
# # The @app.get() decorator is used to define endpoint. The first argument of the decorator is the path of the endpoint
# async def root():
#     return {"Message": "Hello World"}

# @app.get('/')
# async def root():
#     return {"Message": 'Welcome brother!'}

# @app.post('/blog/{blog_id}')  # in url we have to give value to blog_id for eg. /blog/12, Note wrap variable inside a curly braces {}
# async def read_blog(blog_id,request_body: custom,q: str = None): # variable path will come as parameter to this function
#     print(request_body)
#     print(q)
#     return {'blog_id': blog_id} # this will return as {'blog_id':12}

# # q: str = None is query params used for filtering, sorting, etc


## Another Program
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from dotenv import load_dotenv
from models import TodoModel
from database import metadata,engine,sessionloacl
from sqlalchemy.orm import Session
import os

load_dotenv()

print(os.getenv('FOO'))
app = FastAPI()

TodoModel.metadata.create_all(bind = engine)


class Todosbase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    

class Todocreate(Todosbase):
    pass

class Todoupdate(Todosbase):
    pass

class Todoresponse(Todosbase):
    id: int
    
    class Config():
        orm_mode = True

def get_db():
    db = sessionloacl()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos",response_model=List[Todoresponse])
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos

@app.get("/todos/{todo_id}")
def get_todos(todo_id:int):
        for todo in todos:
            if todo['id'] == todo_id:
                return todo
        return {"error":"todo not found"}
        

@app.post("/todos")
def create_todos(todo: Todosbase):
        todos.append(todo.model_dump()) # append todo to the list
        return todos[-1] # return the last todo

@app.delete('todos/{todo_id}')
def delete_todo(todo_id:int):
        for todo in todos:
            if todo['id'] == todo_id:
                todos.remove(todo)
                return {"Message":"Todo deleted successfully"}
        return {"error":"todo id not matched"}
