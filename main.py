from fastapi import FastAPI
from pydantic import BaseModel
import yaml

app = FastAPI()


class ProjectList(BaseModel):
    id: int
    name: str
    description: str | None = None
    link: str


@app.get("/projects/getProjectList")
def get_project_list() -> list[ProjectList]:
    project_file = open("res/projects.yml", "r", encoding="utf-8")
    project_list = yaml.load(project_file, yaml.CFullLoader)
    project_file.close()
    return project_list
