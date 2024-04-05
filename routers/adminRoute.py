import sys

sys.path.append('../routers')

from fastapi import FastAPI, Request
from controllers.adminController import add_new_problem
api = FastAPI()


@api.put("/problem/",status_code=201)
async def add_new_problem_route(request:Request):
    jsonBody = request.state.jsonBody
    name = jsonBody["name"]
    description = jsonBody["description"]
    tags = jsonBody["tags"]

    add_new_problem(name, description, tags)
    return {"message": "New Problem was successfully added"}
