from fastapi import APIRouter
from rag.core import SimpleRAG

router = APIRouter()

rag = SimpleRAG()

@router.get("/rag-search")
def rag_search(query: str):
    return rag.search(query)