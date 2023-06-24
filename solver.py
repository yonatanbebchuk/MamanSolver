import openai

from paper import Paper


class Solver:
    def __init__(
            self,
            paper: Paper,
            question: str,
    ):
        self.paper = paper
        self.question = question

    def solve(self) -> str:
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=[
                self.purpose_message(),
                self.paper.study_paper_message(),
                self.question_message(),
            ]
        )
        return chat.choices[0].message.content

    def question_message(self):
        return {
            "role": "user",
            "content": self.question,
        }

    @staticmethod
    def purpose_message():
        return {
            "role": "system",
            "content": "You are a university student who wants to get an A on their assignment.",
        }
