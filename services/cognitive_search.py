from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from azure_config import COGNITIVE_SEARCH_ENDPOINT, COGNITIVE_SEARCH_KEY, COGNITIVE_SEARCH_INDEX

def search_faq(query: str):
    client = SearchClient(
        endpoint=COGNITIVE_SEARCH_ENDPOINT,
        index_name=COGNITIVE_SEARCH_INDEX,
        credential=AzureKeyCredential(COGNITIVE_SEARCH_KEY)
    )
    
    results = client.search(
        search_text=query,
        top=3,
        query_type="simple",   # You can also try "semantic" if enabled
        select=["question", "answer"],  # Fetch only needed fields
    )
    
    answers = []
    for result in results:
        # Use "answer" field if available, else fallback
        ans = result.get("answer") or result.get("content") or "No answer found"
        answers.append(ans)
    
    return answers
