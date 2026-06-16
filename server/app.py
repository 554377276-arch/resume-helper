from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from llm import ask_ai
from prompt import SYSTEM_PROMPT
from rag.core import SimpleRAG

app = FastAPI()

# 静态文件（CSS）
app.mount("/static", StaticFiles(directory="static"), name="static")

# 模板
templates = Jinja2Templates(directory="templates")

# 初始化RAG（只加载一次）
rag = SimpleRAG()


# 首页
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": ""
        }
    )


# 测试LLM
@app.get("/test")
def test_ai():
    result = ask_ai(SYSTEM_PROMPT, "我学Python三个月了")
    return {"result": result}


# =========================
# 核心：简历优化 + RAG
# =========================
@app.post("/resume")
def optimize_resume(
    request: Request,
    target: str = Form(...),
    resume: str = Form(...)
):

    # 1️⃣ 用RAG从简历内容里检索相关知识
    search_results = rag.search(resume, top_k=2)

    # 2️⃣ 提取文本（不要分数）
    knowledge = "\n".join([item[0] for item in search_results])

    # 3️⃣ 构造Prompt（RAG核心步骤）
    user_input = f"""
【RAG检索知识】
{knowledge}

【求职目标】
{target}

【简历内容】
{resume}

请基于以上信息优化简历，并给出建议。
"""

    # 4️⃣ 调用大模型
    result = ask_ai(SYSTEM_PROMPT, user_input)

    # 5️⃣ 返回网页
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )