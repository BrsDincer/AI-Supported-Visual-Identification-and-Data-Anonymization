from utils_general import CLASSINIT,NULL,ERROR,DOCUMENTATION,IMAGE,ERRORMODULE,TRANSFORMBASE64,CREATEINPUTTEXT,CREATEINPUTURL

class CreateModelMessage(object):
    def __init__(self)->CLASSINIT:
        self.promptDict = dict()
        self.promptDict["role"] = "user"
        self.promptDict["content"] = []
        self.defaultPromptIDX = (
            "Give very clear answers to each question. "
            "Do not add your comment. "
            "Question asked to you:\n"
            )
    def __str__(self)->str:
        return "Creating Model Message - Pre/Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default()
    def __repr__(self)->DOCUMENTATION:
        return CreateModelMessage.__doc__
    def Get(self,initPrompt:str,imageCodecPath:IMAGE | str)->dict:
        codecImage = TRANSFORMBASE64(imageCodecPath)
        self.defaultPromptIDX += str(initPrompt)
        self.promptDict["content"].append(CREATEINPUTURL(codecImage))
        self.promptDict["content"].append(CREATEINPUTTEXT(self.defaultPromptIDX))
        return self.promptDict