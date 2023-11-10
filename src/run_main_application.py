from utils_general import IMAGE,PROCESS,DATAPATH,OPERATORGENERAL,CREATEDIRECTORY,OUTPUTSPATH
from model_completion import ModelCompletionOperation
from main_process_selection import GetAnalyzer,GetAnonymizer
import gradio as gr
import cv2 as cv
import numpy as np
import uuid,os

CREATEDIRECTORY(DATAPATH)
CREATEDIRECTORY(OUTPUTSPATH)

visionModelOps = ModelCompletionOperation()
visionModel = visionModelOps.GetModel()
analyzerMain = GetAnalyzer()
anonymizerMain = GetAnonymizer()
anonymizerEngine = anonymizerMain.Run()
analyzer = analyzerMain.Run(initLanguage="en")
operatorType = OPERATORGENERAL



def DriveSaving(initImage:IMAGE)->str:
    imageFile = f"{uuid.uuid4()}.jpeg"
    imagePath = os.path.join(DATAPATH,imageFile)
    cv.imwrite(imagePath,initImage)
    return imagePath

def RespondForImage(initImage:IMAGE,initPrompt:str,chatHistory:list)->PROCESS:
    image = np.fliplr(initImage)
    image = cv.cvtColor(image,cv.COLOR_RGB2BGR)
    imagePath = DriveSaving(initImage=image)
    responseOut = visionModelOps.RunVision(initModel=visionModel,
                                           targetPrompt=initPrompt,
                                           targetImage=image)
    analyzerResult = analyzer.analyze(text=responseOut,
                                      language="en")
    anonymizerResult = anonymizerEngine.anonymize(text=responseOut,
                                                  analyzer_results=analyzerResult,
                                                  operators=operatorType)
    
    chatHistory.append(((imagePath,),None))
    chatHistory.append((str(initPrompt),str(anonymizerResult.text)))
    return "",chatHistory

with gr.Blocks() as mainApp:
    with gr.Row():
        webCamera = gr.Image(sources=["webcam"],
                             streaming=True)
        with gr.Column():
            chatbot = gr.Chatbot(height=500)
            message = gr.Textbox(lines=5,
                                 label="Chat Input",
                                 placeholder="Waiting...")
            clearButton = gr.ClearButton([message,chatbot])
    message.submit(RespondForImage,[webCamera,message,chatbot],[message,chatbot])

mainApp.launch(debug=False,
               show_error=True,
               inbrowser=True,
               server_name="127.0.0.1",
               server_port=8800,
               share=True,
               max_threads=10,
               show_api=False)