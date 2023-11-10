from utils_class import PATH
import os
BASEPATH:PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATAPATH:PATH = os.path.join(BASEPATH,"data")
CONTENTPATH:PATH = os.path.join(BASEPATH,"content")
OUTPUTSPATH:PATH = os.path.join(BASEPATH,"outputs")
PROJECTFILEPATH:PATH = os.path.join(CONTENTPATH,"project.yaml")
