from sentence_transformers import SentenceTransformer

# ① 加载本地模型（第一次会下载）
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    # ② 把文本转成向量
    vector = model.encode(text)

    return vector


# ③ 测试
text = "FastAPI是一个Web框架"

vector = get_embedding(text)

print("向量长度:", len(vector))
print("前5个数字:", vector[:5])