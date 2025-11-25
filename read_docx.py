import docx


def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)
    except Exception as e:
        return str(e)


content = read_docx("COMP 370 2024 Final Project with Details.docx")
print(content)
