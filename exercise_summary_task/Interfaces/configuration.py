from abc import ABC,abstractmethod

class Configuration(ABC):
    "Class holds configuration for the process in form of properties"
    
    @abstractmethod
    def setup_environment(self,config_file):
        """Function is used to initialize environment variables
        specific for the process from a configuration file"""
