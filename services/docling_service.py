from docling.document_converter import DocumentConverter


def process_document(file_path: str) -> dict:
    try:
        converter = DocumentConverter()

        result = converter.convert(file_path)

        # Extract text (Docling returns structured output)
        text = result.document.export_to_text()

        return {
            "text": text,
            "length": len(text)
        }

    except Exception as e:
        raise Exception(f"Docling failed: {str(e)}")