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
        return trimmed_text

    def find_letter_number(self, file_path: str):
        """Find the office letter number in the specified PDF

        Args:
        - file_path (str): The path to the PDF file
        """
        text = self.read_pdf(file_path=file_path)
        pattern = r'(?i)Nomor\s*:\s*(\S.*?)\s+\b\w+\b'
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return None
