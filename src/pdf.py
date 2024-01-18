import fitz


class PDF:
    def read_pdf(self, file_path: str):
        """Read the specified PDF and return its text content

        Args:
        - file_path (str): The path to the PDF file
        """
        with fitz.open(file_path) as doc:
            text = doc[0].get_text()
        return text

    def extract_text(self, file_path: str, output_path: str):
        """Extract text from the specified PDF and store it
        in '.txt' file

        Args:
        - file_path (str): The path to the PDF file
        - output_path (str): The path to the output '.txt' file
        """
        text = self.read_pdf(file_path=file_path)
        with open(output_path, "w") as f:
            f.write(text)
