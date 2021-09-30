

class Project:
    def __init__(self, name, status='в разработке', inherit_global=None, view_state='публичный', description=None, is_active=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
        self.is_active = is_active

    def __repr__(self):
        return f'{self.name}:{self.status}:{self.is_active}:{self.view_state}:{self.description}'

    def __eq__(self, other):
        return self.name == other.name and self.status == other.status and self.is_active == other.is_active \
               and self.view_state == other.view_state and self.description == other.description

    def name(self):
        return self.name.lower()
