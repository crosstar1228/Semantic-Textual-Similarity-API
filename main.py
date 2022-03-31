
from running_model.models import model # import model 
from basemodel import SentenceInfo
# from flask import Flask, render_template, request
from fastapi import FastAPI, APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Optional


import uvicorn
import math

# app = Flask(__name__)
app = FastAPI()
router = APIRouter()

templates = Jinja2Templates(directory="templates") # directory 명시

@router.get('/', tags = ["UI"], status_code = 200, response_class = HTMLResponse) # response type 정의
async def index(request: Request): # Request module을 인자로 받음
    return templates.TemplateResponse('index.html', {'request' : request}) #( 문서명, context)

# return 
@router.get('/result',tags=["RESULT"],status_code = 200,  response_class = HTMLResponse)
async def result(request : Request, sentence1:str, sentence2 :str):
    if sentence1 and sentence2:
        output = model(sentence1, sentence2)
        # 퍼센트로 나타내기
        output = math.trunc(output*20)

        return templates.TemplateResponse('result.html', {'request' : request, 'sentence1' : sentence1, 'sentence2': sentence2, 'output':output})
    raise HTTPException(status_code = 404, detail = "either of them does not exist")

@router.post('/sentences', status_code = 201, tags=['RESULT'] )
async def postsen(sentence: SentenceInfo):
    print(sentence)
    sentence = sentence.dict()
    
    sentence1, sentence2 = sentence.values()
    output = model(sentence1, sentence2)
    if output>=3:
        binary_output = 1
    else:
        binary_output = 0
    return {"label" : f"{output:.1f}","real label": output, "binary label" : binary_output}





app.include_router(router)

## 해당 모듈의 __name__이 __main__ 일경우, 즉 모듈의 시작점 일경우에, app을 실행
if __name__ == '__main__' :
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload=True)
