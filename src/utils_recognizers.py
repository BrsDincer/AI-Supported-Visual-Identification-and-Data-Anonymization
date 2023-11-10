from typing import List
from presidio_analyzer import EntityRecognizer,RecognizerResult,PatternRecognizer
from presidio_analyzer.nlp_engine import NlpArtifacts

PERSONNAMERECOGNIZER = PatternRecognizer(supported_entity="PERSON",
                                         deny_list=["Mr.","Mrs.","Miss"])

class NUMBERRECOGNIZER(EntityRecognizer):
    expected_confidence_level = 0.2
    def load(self)->None:
        pass
    def analyze(self,
                text:str,
                entities:List[str],
                nlp_artifacts:NlpArtifacts)->List[RecognizerResult]:
        results = []
        for tk in nlp_artifacts.tokens:
            if tk.like_num:
                result = RecognizerResult(entity_type="NUMBER",
                                          start=tk.idx,
                                          end=tk.idx+len(tk),
                                          score=self.expected_confidence_level)
                results.append(result)
            else:
                pass
        return results
    
class PHONENUMBERRECOGNIZER(EntityRecognizer):
    expected_confidence_level = 0.2
    def load(self)->None:
        pass
    def analyze(self,
                text:str,
                entities:List[str],
                nlp_artifacts:NlpArtifacts)->List[RecognizerResult]:
        results = []
        for tk in nlp_artifacts.tokens:
            if tk.like_num:
                result = RecognizerResult(entity_type="PHONE_NUMBER",
                                          start=tk.idx,
                                          end=tk.idx+len(tk),
                                          score=self.expected_confidence_level)
                results.append(result)
            else:
                pass
        return results
    
class CREDITCARDRECOGNIZER(EntityRecognizer):
    expected_confidence_level = 0.2
    def load(self)->None:
        pass
    def analyze(self,
                text:str,
                entities:List[str],
                nlp_artifacts:NlpArtifacts)->List[RecognizerResult]:
        results = []
        for tk in nlp_artifacts.tokens:
            if tk.like_num:
                result = RecognizerResult(entity_type="CREDIT_CARD",
                                          start=tk.idx,
                                          end=tk.idx+len(tk),
                                          score=self.expected_confidence_level)
                results.append(result)
            else:
                pass
        return results

class EMAILRECOGNIZER(EntityRecognizer):
    expected_confidence_level = 0.2
    def load(self)->None:
        pass
    def analyze(self,
                text:str,
                entities:List[str],
                nlp_artifacts:NlpArtifacts)->List[RecognizerResult]:
        results = []
        for tk in nlp_artifacts.tokens:
            if tk.like_email:
                result = RecognizerResult(entity_type="EMAIL_ADDRESS",
                                          start=tk.idx,
                                          end=tk.idx+len(tk),
                                          score=self.expected_confidence_level)
                results.append(result)
            else:
                pass
        return results
    
class URLRECOGNIZER(EntityRecognizer):
    expected_confidence_level = 0.2
    def load(self)->None:
        pass
    def analyze(self,
                text:str,
                entities:List[str],
                nlp_artifacts:NlpArtifacts)->List[RecognizerResult]:
        results = []
        for tk in nlp_artifacts.tokens:
            if tk.like_url:
                result = RecognizerResult(entity_type="URL",
                                          start=tk.idx,
                                          end=tk.idx+len(tk),
                                          score=self.expected_confidence_level)
                results.append(result)
            else:
                pass
        return results
    