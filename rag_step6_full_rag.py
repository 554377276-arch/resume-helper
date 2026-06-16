from sentence_transformers import SentenceTransformer
import numpy as np

# 模型（向量化工具）
model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------
# ① 知识库
# -----------------------
chunks = [
    "FastAPI是一个用于构建Web API的Python框架",
    "RAG是一种结合检索和生成的AI技术",
    "Embedding可以把文本转换成向量"
]


# -----------------------
# ② 向量化知识库
# -----------------------
chunk_vecs = model.encode(chunks)


# -----------------------
# ③ 相似度函数
# -----------------------
def cosine_similarity(a, b):
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot / (norm_a * norm_b)


# -----------------------
# ④ 检索函数（核心）
# -----------------------
def search(query):

    # 1. 问题向量化
    query_vec = model.encode(query)

    # 2. 计算相似度
    scores = []
    for vec in chunk_vecs:
        score = cosine_similarity(query_vec, vec)
        scores.append(score)

    # 3. 找最相似
    best_index = np.argmax(scores)

    return chunks[best_index]


# -----------------------
# ⑤ 模拟LLM回答
# -----------------------
def llm_answer(context, question):
    return f"""
根据资料：{context}

回答问题：{question}

简单解释：这是RAG检索后的结果。
"""


# -----------------------
# ⑥ RAG主流程
# -----------------------
def rag(query):

    # 1. 检索
    context = search(query)

    # 2. 生成回答
    answer = llm_answer(context, query)

    return answer


# -----------------------
# ⑦ 测试
# -----------------------
query = "什么是FastAPI"

result = rag(query)

print(result)