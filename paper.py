from typing import Optional

import PyPDF2


class Paper:
    def __init__(
            self,
            name: str,
            author: str,
            year: str,
            content: str,
    ):
        self.name = name
        self.author = author
        self.year = year
        self.content = content

    @classmethod
    def from_pdf(
            cls,
            path: str,
            name: str,
            author: str,
            year: str,
            number_of_pages: Optional[int] = None,
    ):
        content = str()
        with open(path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_length = len(pdf_reader.pages)
            if not number_of_pages:
                number_of_pages = pdf_length
            number_of_pages = number_of_pages if number_of_pages <= pdf_length else pdf_length
            for page_index in range(number_of_pages):
                content += pdf_reader.pages[page_index].extract_text()

        return Paper(
            name=name,
            author=author,
            year=year,
            content=content,
        )

    def study_paper_message(self) -> dict:
        prompt = f"Here is the {self.year} paper \"{self.name}\" by {self.author}"
        return {
            "role": "system",
            "content": f"{prompt}:\n{self.content}",
        }
