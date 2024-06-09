import weaviate.classes as wvc
from weaviate.classes.config import Property, DataType

from weaviate.connect import ConnectionParams
from weaviate.config import ConnectionConfig
from weaviate.classes.init import AdditionalConfig
from weaviate import WeaviateClient

wclient = WeaviateClient(
    connection_params=ConnectionParams.from_params(
        http_host="localhost",
        http_port="8080",
        http_secure=False,
        grpc_host="localhost",
        grpc_port="50051",
        grpc_secure=False,
    ),
    additional_config=AdditionalConfig(
        connection=ConnectionConfig(
            session_pool_connections=30,
            session_pool_maxsize=200,
            session_pool_max_retries=3,
        ),
        timeout=(60, 180),
    ),
)

issue = {
    "name": "Issue",
    "generative_config": wvc.config.Configure.Generative.ollama(
        api_endpoint="http://ollama:11434", model="llama3"
    ),
    "vectorizer_config": [
        wvc.config.Configure.NamedVectors.text2vec_transformers(
            name="title", source_properties=["title"]
        ),
        wvc.config.Configure.NamedVectors.text2vec_transformers(
            name="body", source_properties=["title"]
        ),
        wvc.config.Configure.NamedVectors.text2vec_transformers(
            name="body_title", source_properties=["body", "title"]
        ),
    ],
    "properties": [
        Property(name="public_id", data_type=DataType.TEXT, skip_vectorization=True),
        Property(name="repository", data_type=DataType.INT, skip_vectorization=True),
        Property(name="title", data_type=DataType.TEXT),
        Property(name="body", data_type=DataType.TEXT),
        Property(name="number", data_type=DataType.INT, skip_vectorization=True),
        Property(name="state", data_type=DataType.TEXT, skip_vectorization=True),
        Property(name="html_url", data_type=DataType.TEXT, skip_vectorization=True),
    ],
}


def create_collections():
    if not wclient.collections.exists("Issue"):
        wclient.collections.create(**issue)
