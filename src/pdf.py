import fitz


class PDF:
    def read_pdf(self, file_path: str):
        """Read the first page of the specified PDF and return its text content

        Args:
        - file_path (str): The path to the PDF file
        """
        with fitz.open(file_path) as doc:
            text = doc[0].get_text()
        return text
