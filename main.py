from paper import Paper
from solver import Solver

PAPER_NAME = "Virtue Theory and Abortion"
PAPER_PDF_PATH = "virtue_theory_and_abortion.pdf"
AUTHOR_NAME = "Rosalind Hursthouse"
PAPER_YEAR = "1991"
ASSIGNMENT_14_QUESTION = """
In the first part of her paper, Hursthouse responds to some criticisms against virtue ethics (9 criticisms in total).
Pick 2 of them. For each criticism, (a) explain the criticism in your own words in a clear way, and (b) explain 
Hursthouse's response to the criticism, in the most convincing and clear way possible.
Respond in 700 words.
"""

if __name__ == '__main__':
    solver = Solver(
        paper=Paper.from_pdf(
            path=PAPER_PDF_PATH,
            name=PAPER_NAME,
            author=AUTHOR_NAME,
            year=PAPER_YEAR,
            number_of_pages=12,
        ),
        question=ASSIGNMENT_14_QUESTION,
    )

    solution = solver.solve()
    print(solution)
