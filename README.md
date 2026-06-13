# AI简历优化助手（resume-helper）

## 📌 项目介绍
这是一个基于 FastAPI + DeepSeek API 开发的 AI 简历优化系统，用户可以输入简历内容和求职目标，系统会自动生成优化建议。

---

## 🚀 技术栈
- Python
- FastAPI
- DeepSeek API
- Jinja2
- HTML + CSS

---

## 💡 功能说明
- 简历内容输入
- 求职目标输入
- AI智能优化简历
- 网页实时展示结果
- 静态页面美化

---

## 📂 项目结构
resume-helper/
├── app.py
├── llm.py
├── prompt.py
├── fastapi/
├── templates/
├── static/
└── README.md

---

## ▶️ 运行方式
```bash
pip install -r requirements.txt
uvicorn app:app --reload
##访问
http://127.0.0.1:8000
