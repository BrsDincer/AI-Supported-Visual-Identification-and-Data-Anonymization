from utils_general import CLASSINIT,ERROR,NULL,DOCUMENTATION,PROJECTFILEPATH,ERRORMODULE
import yaml

class ReadProjectYAML(object):
    def __init__(self)->CLASSINIT:
        self.directory = PROJECTFILEPATH
    def __str__(self)->str:
        return "Reading Project YAML File - Pre/Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return ReadProjectYAML.__doc__
    def GetAPI(self)->str:
        readLoad = yaml.safe_load(open(self.directory,
                                       "r",
                                       errors="ignore",
                                       encoding="utf-8"))
        return readLoad["apikey"]["OPENAI_API_KEY"]