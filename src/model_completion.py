from utils_general import CLASSINIT,ERROR,DOCUMENTATION,IMAGE,NULL,MODEL,ERRORMODULE,RESULT,VISIONMODEL
from openai import OpenAI
from create_model_message import CreateModelMessage
from read_yaml import ReadProjectYAML
import os

class ModelCompletionOperation(object):
    def __init__(self)->CLASSINIT:
        self.openaiapikey = ReadProjectYAML().GetAPI()
        os.environ["OPENAI_API_KEY"] = self.openaiapikey
        self.defaultMaxToken = 500
        self.defaultTimeout = 700
        self.temperature = 0.1
        self.frequency_penalty = 1.0
        self.presence_penalty = 2.0
    def __str__(self)->str:
        return "Model Completion Process - Pro/Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return ModelCompletionOperation.__doc__
    def GetModel(self)->MODEL:
        client = OpenAI()
        return client
    def GetMessageParameter(self,targetPrompt:str,targetImage:IMAGE)->dict:
        message = CreateModelMessage().Get(initPrompt=targetPrompt,
                                           imageCodecPath=targetImage)
        return message
    def RunVision(self,initModel:MODEL,targetPrompt:str,targetImage:IMAGE)->RESULT:
        message = self.GetMessageParameter(targetPrompt=targetPrompt,
                                           targetImage=targetImage)
        result = initModel.chat.completions.create(model=VISIONMODEL,
                                                   max_tokens=self.defaultMaxToken,
                                                   temperature=self.temperature,
                                                   presence_penalty=self.presence_penalty,
                                                   frequency_penalty=self.frequency_penalty,
                                                   timeout=self.defaultTimeout,
                                                   messages=[message])
        if result.choices[0].finish_details["type"].lower() == "stop":
            output = result.choices[0].message.content
            return output
        else:
            return "[MODEL - CONFUSE] - Try again"
        
