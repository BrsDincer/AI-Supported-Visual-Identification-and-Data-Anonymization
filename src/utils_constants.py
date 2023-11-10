from utils_class import PROCESS
from utils_nlp import DEFINELANGUAGE
from presidio_analyzer.context_aware_enhancers import LemmaContextAwareEnhancer
from presidio_analyzer.nlp_engine import NlpEngineProvider


VISIONMODEL = "gpt-4-vision-preview"
CONTEXTAWARE:PROCESS = LemmaContextAwareEnhancer(context_similarity_factor=0.2,
                                                 min_score_with_context_similarity=0.2)

def RETURNNLPPROVIDER(initLanguage:str)->PROCESS:
    configurationNLP = DEFINELANGUAGE(initLanguage)
    NLPPROVIDER = NlpEngineProvider(nlp_configuration=configurationNLP)
    return NLPPROVIDER
