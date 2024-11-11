from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        project_data = toml.loads(content)
        #print(project_data)
        name = project_data["tool"]["poetry"]["name"]
        description = project_data["tool"]["poetry"]["description"]
        license = project_data["tool"]["poetry"]["license"]
        authors = project_data["tool"]["poetry"]["authors"]
        dependencies = project_data["tool"]["poetry"]["dependencies"]
        dev_dependencies = project_data["tool"]["poetry"]["group"]["dev"]["dependencies"]


        return Project(name, description, license, authors, dependencies, dev_dependencies)
