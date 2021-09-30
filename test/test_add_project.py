from model.project import Project
import random


def test_add_project(app):
    old_projects = app.project.get_project_list()
    project = Project(name='MyCoolProject!', description='descr of proj')
    if project.name not in [proj.name for proj in old_projects]:
        app.project.create(project)
    else:
        project.name = f'{project.name} NEW!' + random.choice(project.name)
        app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)

    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)
