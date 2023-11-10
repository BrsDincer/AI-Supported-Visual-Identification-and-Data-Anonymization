from utils_class import CONFIGURATION

def DEFINELANGUAGE(initLanguage:str)->CONFIGURATION:
    if initLanguage.lower() == "es":
        modelType = "es_core_news_md"
    elif initLanguage.lower() == "en":
        modelType = "en_core_web_lg"
    elif initLanguage.lower() == "fr":
        modelType = "fr_core_news_sm"
    elif initLanguage.lower() == "de":
        modelType = "de_core_news_sm"
    elif initLanguage.lower() == "ru":
        modelType = "ru_core_news_sm"
    elif initLanguage.lower() == "nl":
        modelType = "nl_core_news_sm"
    else:
        modelType = "xx_sent_ud_sm"
    NLPENGINECONFIGURATION = {"nlp_engine_name":"spacy",
                              "models":[
                                  {"lang_code":initLanguage.lower(),
                                   "model_name":modelType}]}
    return NLPENGINECONFIGURATION