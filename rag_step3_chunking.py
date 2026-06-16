# ===== ① 读取知识库 =====
with open("knowledge.txt", "r", encoding="utf-8") as f:
    text = f.read()   # 把整个文件读成一个大字符串

# ===== ② 按句子切块函数 =====
def split_by_sentence(text):
    """
    按句子切分文本（更适合RAG）
    """

    # 中文和英文句号一起处理
    text = text.replace("\n", "")  # 去掉换行，避免干扰

    # 用句号切分（。和.都支持）
    sentences = text.replace("。", "。|").replace(".", ".|").split("|")

    # 清理空内容
    chunks = []
    for s in sentences:
        s = s.strip()  # 去掉前后空格

        if s:  # 如果不是空字符串
            chunks.append(s)

    return chunks


# ===== ③ 执行切块 =====
chunks = split_by_sentence(text)


# ===== ④ 输出结果 =====
for i, c in enumerate(chunks):
    print(f"\n--- chunk {i} ---")
    print(c)

# 练习
# # ① 读取知识库文件
# text = open("knowledge.txt", "r", encoding="utf-8").read()
#
#
# # ② 定义函数：做“按句子切块”
# def split_by_sentence(text):
#
#     # ③ 准备容器（用来存结果）
#     chunks = []
#
#     # ④ 第一步：把 text 变成“句子列表”
#     # 提示：用 .replace() 或 split() 把句子切开
#     sentences = text.replace("。","|"), text.split(".", "|")   # ← 你来填
#
#     # ⑤ 遍历每一个句子
#     for s in sentences:
#
#         # 提示：清理空格
#         s = s.split()       # ← 你来填
#
#         # ⑥ 判断不是空字符串
#         if s:       # ← 你来填
#
#             # 加入结果
#             s = chunks.append(s)       # ← 你来填
#
#     # ⑦ 返回结果
#     return  chunks# ← 你来填
#
#
# # ⑧ 调用函数
# chunks = split_by_sentence(text)
#
#
# # ⑨ 输出结果
# for i, c in enumerate(chunks):
#     print(f"\n--- chunk {i} ---")
#     print(c)

















