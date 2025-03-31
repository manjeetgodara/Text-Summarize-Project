
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.entity import ModelEvaluationConfig
from textSummarizer.logging import logger

class DataModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.evaluate()
        except Exception as e:
            raise e