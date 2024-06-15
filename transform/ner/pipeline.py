from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import pipeline
from .utils import tokens_to_entities, get_unique_entities
from data.utils.text import remove_links, remove_markdown

NER_MODEL_NAME = 'dslim/bert-base-NER'


def get_ner_entities(ner_pipeline, text: str):
    plain_text = remove_markdown(text)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2500, chunk_overlap=250)

    chunks = text_splitter.split_text(plain_text)

    all_entities = []

    for chunk in chunks:
        entities = ner_pipeline(chunk)
        all_entities.extend(entities)

    return all_entities


def extract_scored_keywords(text: str):
    ner_pipeline = pipeline("ner", NER_MODEL_NAME)

    ner_entities = get_ner_entities(ner_pipeline, text)
    plain_entities = tokens_to_entities(ner_entities)
    entities = get_unique_entities(plain_entities)
    return entities
