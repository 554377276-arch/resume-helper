from sentence_transformers import SentenceTransformer
import numpy as np

# =========================
# ① 加载向量模型（embedding模型）
# =========================
model = SentenceTransformer("all-MiniLM-L6-v2")


# =========================
# ② 用户问题（Query）
# =========================
query = "什么是FastAPI"


# =========================
# ③ 知识库（chunks）
# =========================
chunks = [
    "FastAPI是一个用于构建Web API的Python框架",
    "RAG是一种结合检索和生成的AI技术",
    "Embedding可以把文本转换成向量"
]


# =========================
# ④ 文字 → 向量（embedding）
# =========================
query_vec = model.encode(query)
chunk_vecs = model.encode(chunks)


# =========================
# ⑤ 相似度函数（cosine similarity）
# =========================
def cosine_similarity(a, b):
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    return dot / (norm_a * norm_b)


# =========================
# ⑥ 计算每个chunk的相似度
# =========================
scores = []

for vec in chunk_vecs:
    score = cosine_similarity(query_vec, vec)
    scores.append(score)


# =========================
# ⑦ 找最大值（最相似）
# =========================
best_index = np.argmax(scores)


# =========================
# ⑧ 输出结果
# =========================
print("用户问题:", query)
print("最相关chunk:", chunks[best_index])
print("相似度分数:", scores)