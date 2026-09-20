from pathlib import Path
import yaml

class Config:

    def __init__(self,environment):
        self.environment=environment

        project_root=Path(__file__).resolve().parents[2]
        #here __file__ is current file , ressolve method resolves
        #the current path, then parents take you like 0,1,2 directory abobe which is pwpy

        config_file= (project_root
                      /"config"
                      /f"config.{environment}.yaml")

        with open(config_file,'r') as file:
            self.config=yaml.safe_load(file) #This Function Converts YAML file into Dictionary.

    def get_base_url(self):
        return self.config["application"]["base_url"]

    def get_browser_name(self):
        return self.config["browser"]["name"]

    def get_headless(self):
        return self.config["browser"]["headless"]

    def get_default_timeout(self):
        return self.config["timeouts"]["default"]

    def get_navigation_timeout(self):
        return self.config["timeouts"]["navigation"]

    def get_expect_timeout(self):
        return self.config["timeouts"]["expect"]
    