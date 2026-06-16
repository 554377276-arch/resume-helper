# rag/utils.py

import numpy as np

# 1. 简单文本向量化（字符级）
def text_to_vector(text):
    vec = np.zeros(1000)  # 固定长度向量
    for char in text:
        index = ord(char) % 1000
        vec[index] += 1
    return vec


# 2. 计算余弦相似度
def cosine_similarity(a, b):
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot / (norm_a * norm_b)