from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from llm import ask_ai
from prompt import SYSTEM_PROMPT
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
class ResumeRequest(BaseModel):
    resume: str
    target: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": ""
        }
    )

@app.get("/test")
def test_ai():
    result = ask_ai(SYSTEM_PROMPT,"我学Python三个月了")
    return {"result": result}

#优化简历
@app.post("/resume")
def optimize_resume(request: Request,target: str = Form(...),resume: str = Form(...)):
    user_input = f"""
求职目标：
{target}
简历内容：
{resume}
"""
    result = ask_ai(SYSTEM_PROMPT,user_input)

    return templates.TemplateResponse(request=request,name="index.html",context={"result": result})
#整个流程
# 用户输入
#     ↓
# HTML Form
#     ↓
# POST /resume
#     ↓
# FastAPI
#     ↓
# Form(...)
#     ↓
# target
# resume
#     ↓
# ask_ai()
#     ↓
# DeepSeek
#     ↓
# 返回结果
#     ↓
# context
#     ↓
# {{ result }}
#     ↓
# 浏览器显示

print("hello from main + hello from feature")


