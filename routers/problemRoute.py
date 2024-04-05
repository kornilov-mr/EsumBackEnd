import sys

sys.path.append('../routers')

from fastapi import FastAPI

api = FastAPI()


@api.get("/get_problem/{problem_id}", status_code=201)
async def get_problems(problem_id: int):
    pass


