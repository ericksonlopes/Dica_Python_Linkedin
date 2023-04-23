import logging
from dataclasses import dataclass
from datetime import datetime

# pip install elasticsearch
from elasticsearch import Elasticsearch


@dataclass
class ElasticsearchConfig:
    host: str = "localhost"
    port: int = 9200
    scheme: str = "http"
    index_name: str = "logs"


class ElasticSearchLogger(logging.Logger, ElasticsearchConfig):
    def __init__(self):
        super().__init__(self.index_name)

        self.__es = Elasticsearch(
            hosts=[{'host': self.host, 'port': self.port, 'scheme': self.scheme}]
        )

        if not self.__es.indices.exists(index=self.index_name):
            self.__es.indices.create(index=self.index_name)

    def log(self, level, message, *args, **kwargs):
        message['level'] = level
        message["timestamp"] = datetime.now()

        self.__es.index(index=self.index_name, document=message)
        super().log(level, message)

    def info(self, message, *args, **kwargs):
        self.log(logging.INFO, message)

    def error(self, message, *args, **kwargs):
        self.log(logging.ERROR, message)

    def warning(self, message, *args, **kwargs):
        self.log(logging.WARNING, message)

    def critical(self, message, *args, **kwargs):
        self.log(logging.CRITICAL, message)

    def debug(self, message, *args, **kwargs):
        self.log(logging.DEBUG, message)


class Test(ElasticSearchLogger):
    def __init__(self):
        super().__init__()

    def test(self):
        self.info({'message': 'Info'})
        self.error({'message': 'Error'})
        self.warning({'message': 'Warning'})
        self.critical({'message': 'Critical'})
        self.debug({'message': 'Debug'})


if __name__ == '__main__':
    Test().test()
