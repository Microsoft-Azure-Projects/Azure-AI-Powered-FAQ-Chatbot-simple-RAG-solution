from openai import AzureOpenAI
from azure_config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT

def refine_with_openai(query: str, context: str) -> str:
    """
    Takes user query + retrieved FAQ context, and refines the answer using Azure OpenAI.
    """
    client = AzureOpenAI(
        api_key=AZURE_OPENAI_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version="2024-05-01-preview"
    )

    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,   # e.g., "gpt-35-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful support assistant. Use the provided context to answer."},
                {"role": "user", "content": f"Question: {query}\n\nContext:\n{context}\n\nAnswer clearly:"}
            ],
            max_tokens=300,
            temperature=0.3,   # lower = more factual, higher = more creative
            top_p=0.95
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Error with OpenAI API: {str(e)}"
