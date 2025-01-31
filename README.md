# [기업과제3] 텍스트 유사도(STS)를 알려주는 API
* 본 API는 원티드 프리온보딩 코스의 기업과제 3번 수행을 위해 제작되었습니다.
* model : [KoELECTRA](https://github.com/monologg/KoELECTRA)중 koelectra-base-v3-discriminator(pre-trained model)을 fine-tuning한 모델입니다. 
* fine-tuning에는 [KLUE-STS](https://klue-benchmark.com/tasks/67/overview/description) 의 train data를 사용하였습니다.

## Updates
**March 30, 2022**
* second commit(changed from flask to fastapi) 

## How to run
(Ubuntu 20.04) 기준 
```bash
$ git clone https://github.com/crosstar1228/Semantic-Textual-Similarity-API.git
$ sudo apt-get install git-lfs
$ git lfs install
$ git lfs pull
$ pip install -r requirements.txt
$ (sudo) python main.py
```

실행 후, http://127.0.0.1:5000/ (혹은 localhost)로 접속   
<img src="images/input_image.png">
박스안에 문장 두개를 입력하고 submit 해줍니다.
<img src="images/result_image.png">

## Directory structure
```bash
├── images
├── running_model
│   ├── best_model
│   │   ├── config.json
│   │   └── pytorch_model.bin
│   ├── data_preprocessing.py
│   └── models.py
├── templates
│   ├── index.html
│   └── result.html
├── main.py
├── basemodel.py
├── README.md
└── requirements.txt
``` 
* running_model : fine-tuning된 best_model과 model을 실행하는데 필요한 모듈을 포함합니다. 
* models.py : model함수로 모델을 실행하여 두개의 문장에 대해 유사도를 구합니다. 
* data_preprocessing.py : 받은 두개의 문장에 대해 전처리를 진행하는 모듈입니다. 
* basemodel.py : `pydantic`을 활용하여 api post/get 명령어로 주고 받을 자료형 및 예시가 class 형태로 정의되어 있습니다.


## Requirements
```
fastapi==0.75.0
huggingface-hub==0.4.0
tokenizers==0.11.6
torch==1.11.0
transformers==4.17.0
pydantic==1.9.0
uvicorn==0.17.6
```

## HTTP POST(유사도 json 반환) (endpoint : '/sentences')
### At terminal
```
$ curl -X 'POST' \
  'http://127.0.0.1:8000/sentences' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sentence1": "그 해 여름은 유난히도 더웠다",
  "sentence2": "그 해 여름은 유난히 도 습하고 더웠어, 그치?"
}'
```

### Swagger UI
- url : `127.0.0.1/docs`
- Try it out -> execute 
    ![](https://images.velog.io/images/crosstar1228/post/b9e1750e-248a-40cc-b58a-c6c76fcf014a/image.png)
- 결과 확인
    ![](https://images.velog.io/images/crosstar1228/post/67fadd21-73fd-434e-980d-574a9887d39c/image.png)


## Score (at [KLUE sts dev set](https://klue-benchmark.com/tasks/67/data/description))
- Pearson's r (0~5 continuous similarity): 0.933
- F1 Score(for binary classification): 0.867

## Our team
| <img src="https://avatars.githubusercontent.com/u/85736494?v=4" width="150"> | <img src="https://avatars.githubusercontent.com/u/86637320?v=4" width="150"> | <img src="https://avatars.githubusercontent.com/u/78654687?v=4" width="150"> |
|:--------:|:---------:|:---------:|
| [류제성](https://github.com/crosstar1228) | [원재성](https://github.com/Woodywarhol9) | [장진희](https://github.com/zzhenxi) |
| 모델 조사 및 데이터 전처리| 모델 조사 및 구현, fine-tuning | 모델 조사 및 구현, rest api 구현
