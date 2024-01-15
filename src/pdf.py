from pypdf import PdfReader


class PDF:
    def read_pdf(self, file_path: str):
        reader = PdfReader(file_path)
        page = reader.pages[0]
        print(page.extract_text())
