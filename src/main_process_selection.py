from utils_general import CLASSINIT,NULL,DOCUMENTATION,ERROR,ERRORMODULE,PROCESS
from utils_general import PHONENUMBERRECOGNIZER,NUMBERRECOGNIZER,CREDITCARDRECOGNIZER,EMAILRECOGNIZER,URLRECOGNIZER
from utils_general import PERSONNAMERECOGNIZER,RETURNNLPPROVIDER,ANALYZER,ANONYMIZER,CONTEXTAWARE
from presidio_analyzer.recognizer_registry import RecognizerRegistry
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

class GetRecognizers(object):
    def __init__(self)->CLASSINIT:
        self.supportedLanguage = ["en",
                                  "es",
                                  "fr",
                                  "de",
                                  "ru",
                                  "nl",
                                  "xx"]
        self.numberRecognizer = NUMBERRECOGNIZER(supported_entities=["NUMBER"],
                                                 supported_language=self.supportedLanguage)
        self.creditcardRecognizer = CREDITCARDRECOGNIZER(supported_entities=["CREDIT_CARD"],
                                                         supported_language=self.supportedLanguage)
        self.emailRecognizer = EMAILRECOGNIZER(supported_entities=["EMAIL_ADDRESS"],
                                               supported_language=self.supportedLanguage)
        self.urlRecognizer = URLRECOGNIZER(supported_entities=["URL"],
                                           supported_language=self.supportedLanguage)
        self.phoneRecognizer = PHONENUMBERRECOGNIZER(supported_entities=["PHONE_NUMBER"],
                                                     supported_language=self.supportedLanguage)
    def __str__(self)->str:
        return "Main Process Selection - Pre/Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return GetRecognizers.__doc__
    
class GetRegistry(object):
    def __init__(self)->CLASSINIT:
        self.recognizers = GetRecognizers()
        self.registry = RecognizerRegistry()
    def __str__(self)->str:
        return "Registry - Pre/Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return GetRegistry().__doc__
    def Run(self)->PROCESS:
        self.registry.add_recognizer(recognizer=self.recognizers.numberRecognizer)
        self.registry.add_recognizer(recognizer=self.recognizers.creditcardRecognizer)
        self.registry.add_recognizer(recognizer=self.recognizers.emailRecognizer)
        self.registry.add_recognizer(recognizer=self.recognizers.urlRecognizer)
        self.registry.add_recognizer(recognizer=self.recognizers.phoneRecognizer)
        self.registry.add_recognizer(recognizer=PERSONNAMERECOGNIZER)
        
class GetAnalyzer(object):
    def __init__(self)->CLASSINIT:
        self.recognizers = GetRecognizers()
        self.supportedLanguage = ["en",
                                  "es",
                                  "fr",
                                  "de",
                                  "ru",
                                  "nl",
                                  "xx"]
    def __str__(self)->str:
        return "Analyzer - Pre/Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return GetAnalyzer.__doc__
    def GetNLPEngine(self,initLanguage:str)->PROCESS:
        nlpEngine = RETURNNLPPROVIDER(initLanguage)
        return nlpEngine.create_engine()
    def Run(self,initLanguage:str)->ANALYZER:
        nlpEngine = self.GetNLPEngine(initLanguage=initLanguage)
        analyzer = AnalyzerEngine(nlp_engine=nlpEngine,
                                  context_aware_enhancer=CONTEXTAWARE,
                                  supported_languages=self.supportedLanguage)
        analyzer.registry.add_recognizer(self.recognizers.numberRecognizer)
        analyzer.registry.add_recognizer(self.recognizers.creditcardRecognizer)
        analyzer.registry.add_recognizer(self.recognizers.emailRecognizer)
        analyzer.registry.add_recognizer(self.recognizers.urlRecognizer)
        analyzer.registry.add_recognizer(self.recognizers.phoneRecognizer)
        analyzer.registry.add_recognizer(PERSONNAMERECOGNIZER)
        return analyzer

class GetAnonymizer(object):
    def __init__(self)->CLASSINIT:
        pass
    def __str__(self)->str:
        return "Anonymizer - Pre/Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return GetAnonymizer.__doc__
    def Run(self)->ANONYMIZER:
        anonymizerEngine = AnonymizerEngine()
        return anonymizerEngine
        