import sys

sys.path.append('../routers')

from fastapi import FastAPI, Request
from controllers.userController import set_problem_as_solved
api = FastAPI()


@api.get("/account/problems")
async def get_all_solved_problem():

    return {"message" : "got problems"}

@api.get("/account/")
async def get_account():
    return {"message": "test"}



@api.put("/problem/{problem_id}")
async def set_problem_as_solved_route(request: Request, problem_id: int):
    login = request.state.user["login"]
    set_problem_as_solved(problem_id, login)
    return {"message": "problem was successfully marked as solved"}
