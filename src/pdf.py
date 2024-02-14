import fitz
import re

class PDF:
    def read_pdf(self, file_path: str):
        """Read the first page of the specified PDF, trim all the leading and 
        trailing whitespaces, and return its text content

        Args:
        - file_path (str): The path to the PDF file
        """
        with fitz.open(file_path) as doc:
            text = doc[0].get_text()
        trimmed_text = re.sub(r'^\s+|\s+$', '', text, flags=re.MULTILINE)
        print(trimmed_text)
