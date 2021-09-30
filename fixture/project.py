from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_proj_page(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-2.25.2/manage_proj_page.php')

    def open_proj_create_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("proj_create_page.php"):
            self.open_manage_proj_page()
            wd.find_element_by_css_selector('form[action="manage_proj_create_page.php"]').click()

    def create(self, project):
        wd = self.app.wd
        self.open_proj_create_page()
        self.fill_proj_fields(project)
        wd.find_element_by_css_selector('input[type="submit"]').click()
        self.open_manage_proj_page()

    def fill_proj_fields(self, project):
        wd = self.app.wd
        wd.find_element_by_name('name').click()
        wd.find_element_by_name('name').clear()
        wd.find_element_by_name('name').send_keys(project.name)
        if project.status:
            Select(wd.find_element_by_name('status')).select_by_visible_text(project.status)
        if project.inherit_global:
            wd.find_element_by_name('inherit_global').click()
        if project.view_state:
            Select(wd.find_element_by_name('view_state')).select_by_visible_text(project.view_state)
        if project.description:
            wd.find_element_by_name('description').click()
            wd.find_element_by_name('description').clear()
            wd.find_element_by_name('description').send_keys(project.description)

    def count(self):
        wd = self.app.wd
        self.open_manage_proj_page()
        projects = wd.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')
        return len(projects)

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_proj_page()
        projects = wd.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')
        project_list = []
        for proj in projects:
            cells = proj.find_elements_by_tag_name('td')
            name = cells[0].find_element_by_tag_name('a').text
            status = cells[1].text
            is_active = cells[2].text
            view_state = cells[3].text
            description = cells[4].text
            project_list.append(Project(name, status, is_active, view_state, description))
        return project_list

    def delete(self, project):
        wd = self.app.wd
        self.open_manage_proj_page()
        wd.find_element_by_xpath(f'//td/a[text()="{project.name}"]').click()
        wd.find_element_by_id('project-delete-form').click()
        wd.find_element_by_css_selector('input[type="submit"]').click()
        self.open_manage_proj_page()
