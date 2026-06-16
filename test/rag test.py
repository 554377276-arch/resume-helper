import sys
import os

# 👉 当前文件：test/rag test.py
# 👉 test文件夹路径
test_dir = os.path.dirname(__file__)

# 👉 项目根目录（关键！！！）
project_root = os.path.dirname(test_dir)

# 👉 加入Python搜索路径
sys.path.append(project_root)

from rag.core import SimpleRAG

rag = SimpleRAG()

query = "什么是RAG"
result = rag.search(query)

print(result)