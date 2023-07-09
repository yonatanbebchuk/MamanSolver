import os

from langchain.chat_models import ChatOpenAI
from llama_index import PromptHelper, LLMPredictor, SimpleDirectoryReader, GPTVectorStoreIndex, StorageContext, \
    load_index_from_storage


class Student:
    def __init__(
            self,
            model_name: str = "gpt-3.5-turbo",
            course_material_path: str = "course_material",
            brain_path: str = "brain",
    ):
        self.model_name = model_name
        self.course_material_path = course_material_path
        self.brain_path = brain_path

    def study(self):
        prompt_helper = PromptHelper()
        llm = ChatOpenAI(temperature=0.7, model_name=self.model_name, max_tokens=512)
        llm_predictor = LLMPredictor(llm=llm)

        course_material = list()
        for directory in os.listdir(self.course_material_path):
            directory_path = f"{self.course_material_path}/{directory}"
            course_material.extend(SimpleDirectoryReader(input_dir=directory_path).load_data())

        index = GPTVectorStoreIndex(course_material, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
        index.storage_context.persist(persist_dir=self.brain_path)

    def solve(self, question: str):
        storage_context = StorageContext.from_defaults(persist_dir=self.brain_path)
        index = load_index_from_storage(storage_context)
        query_engine = index.as_query_engine()
        return query_engine.query(question)
