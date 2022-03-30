from ruamel.yaml import YAML
import os
import sys

#Configuration File Setup
yaml = YAML()
config_file = str(os.path.join(sys.path[0]))+"/config_loader/conf.yaml"
configuration = {}

#Configuration Loader Class
class config_loader:
  def __init__(self):
    for key, value in yaml.load(open(config_file)).items():
      configuration[key] = value
    self.__configuration = configuration

  #Getter
  def get_configuration(self):
    return self.__configuration