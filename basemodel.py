from pydantic import BaseModel

class SentenceInfo(BaseModel):
    """
    문장 유사도 측정 가즈아!
    """


    sentence1 : str
    sentence2 : str
    class Config:
         schema_extra = {
            "example": {
                "sentence1": "그 해 여름은 유난히도 더웠다",
                "sentence2": "그 해 여름은 유난히 도 습하고 더웠어, 그치?",
            },
        }