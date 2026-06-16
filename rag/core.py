# rag/core.py

from rag.data import documents
from rag.utils import text_to_vector, cosine_similarity


class SimpleRAG:
    def __init__(self):
        # 1. 预计算所有文档向量（相当于“知识库索引”）
        self.doc_vectors = [text_to_vector(doc) for doc in documents]

    # 2. 检索最相关文档
    def search(self, query, top_k=1):
        query_vec = text_to_vector(query)

        scores = []

        # 3. 逐个计算相似度
        for i, doc_vec in enumerate(self.doc_vectors):
            score = cosine_similarity(query_vec, doc_vec)
            scores.append((documents[i], score))

        # 4. 按相似度排序
        scores.sort(key=lambda x: x[1], reverse=True)

        return scores[:top_k]