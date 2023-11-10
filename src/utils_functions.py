from utils_class import PROCESS,IMAGE
import os,shutil,cv2 as cv,base64
CREATEDIRECTORY:PROCESS = lambda x: os.mkdir(x) if not os.path.exists(x) else None
DELETEDIRECTORY:PROCESS = lambda x: shutil.rmtree(x) if len(os.listdir(x)) > 1 else None
DELETEFILE:PROCESS = lambda x: os.remove(x) if os.path.exists(x) else None
SORTDIRECTORY:PROCESS = lambda x: int(x.rsplit("_",1)[-1].split(".")[0])
CREATEINPUTURL:PROCESS = lambda x:{"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{str(x)}"}}
CREATEINPUTTEXT:PROCESS = lambda x:{"type":"text","text":str(x)}

def TRANSFORMBASE64(initImage:IMAGE)->PROCESS:
    success,buffer = cv.imencode(".jpg",initImage)
    if not success:
        raise ValueError("COULD NOT ENCODE - ERROR JPEG FORMAT")
    encodedImage = base64.b64encode(buffer).decode("utf-8")
    return encodedImage
        