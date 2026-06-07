from settings import Settings
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

def extract_text_blob(client: DocumentIntelligenceClient ,blob_sas_url: str):
    """Extract text from a blob
    
    Keyword arguments:
    client(DocumentIntelligenceClient) -- Document Intelligence client
    blob_sas_url(str) -- sas url of a blob
    Return: 
    list - list of pages
    """

    try:
        print("starting text extraction")
        poller = client.begin_analyze_document(
            "prebuilt-layout",
            AnalyzeDocumentRequest(
                url_source=blob_sas_url
            )
        )
        result = poller.result()
        text_list = list()
        if result.pages:
            for idx, page in enumerate(result.pages):
                text_list.append(
                    {
                        "page_number": idx + 1,
                        "text": " ".join(
                            line.content.strip()
                            for line in page.lines # type: ignore
                            if line.content.strip()
                        ),
                        "source_blob": blob_sas_url.lstrip('?')[0]
                    }
                )


        return text_list
    except Exception as e:
        print(f"failed to extract text from sas_url - {e}")
        raise