from model.project import Project
import random


def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name='Project_for_del'))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete(project)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)

    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)
