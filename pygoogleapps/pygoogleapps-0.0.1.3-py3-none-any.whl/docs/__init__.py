from .document import Document


def get(document_id, suggestions_view_mode=None):
    doc = Document(document_id=document_id)
    doc.load()
    return(doc)
