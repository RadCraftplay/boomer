
import re
from typing import Callable

from adapters.Adapter import Adapter
from adapters.AdapterAdapter import AdapterAdapter
from adapters.RegexAdapter import RegexAdapter
from adapters.TfidfAdapter import TfidfAdapter


class AdapterBuilder():
    def __init__(self, threshold):
        self.threshold = threshold
        self.regexes_to_funcs : dict[str, Callable[[re.Match], Callable[[], str]]] = {}
        self.questions_to_funcs : list[tuple[str, Callable[[], str]]] = []

    def get(self) -> Adapter:
        adapter = AdapterAdapter([])

        if self.regexes_to_funcs.__len__() > 0:
            adapter.adapters.append(RegexAdapter(self.regexes_to_funcs))
        
        if self.questions_to_funcs.__len__() > 0:
            adapter.adapters.append(TfidfAdapter(self.questions_to_funcs, self.threshold))
        
        return adapter
    
    def with_question(self, question: str, answer_func: Callable[[], str]):
        self.questions_to_funcs.append((question, answer_func))
        return self
    
    def with_questions(self, questions_and_answers: list[tuple[str, Callable[[], str]]]):
        self.questions_to_funcs.extend(questions_and_answers)
        return self
    
    def with_questions_single_answer(self, questions: list[str], answer_func: Callable[[], str]):
        for question in questions:
            self.questions_to_funcs.append((question, answer_func))
        return self
    
    def with_regex(self, question: str, answer_func: Callable[[re.Match], Callable[[], str]]):
        self.regexes_to_funcs[question] = answer_func
        return self
    
    def with_regexes(self, regexes_and_answers: dict[str, Callable[[re.Match], Callable[[], str]]]):
        self.regexes_to_funcs.update(regexes_and_answers)
        return self
    
    def with_regexes_single_answer(self, regexes: list[str], answer_func: Callable[[re.Match], Callable[[], str]]):
        for question in regexes:
            self.regexes_to_funcs[question] = answer_func
        return self