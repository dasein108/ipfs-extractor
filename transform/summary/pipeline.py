from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import pipeline
from .utils import glue_summary_text
from data.utils.text import remove_links, remove_markdown

SUMMARIZATION_MODEL_NAME = 'google-t5/t5-small'



def summarize_text(summary_pipeline, text, splitter_kwargs: dict, summarization_kwargs: dict):
    plain_text = remove_markdown(text)
    text_splitter = RecursiveCharacterTextSplitter(**splitter_kwargs)
    chunks = text_splitter.split_text(plain_text)
    all_entities = []
    for chunk in chunks:
        summary_text = summary_pipeline(chunk, **summarization_kwargs)[0]['summary_text']
        processed_summary = glue_summary_text(summary_text)

        all_entities.append(processed_summary)

    return "\r\n".join(all_entities)


def create_summary(text: str):
    summary_pipeline = pipeline(task="summarization", model=SUMMARIZATION_MODEL_NAME)

    long_result = summarize_text(summary_pipeline, text,
                                 splitter_kwargs=dict(chunk_size=2500, chunk_overlap=500),
                                 summarization_kwargs=dict(max_length=150, min_length=50))

    short_result = summarize_text(summary_pipeline, long_result,
                                  splitter_kwargs=dict(chunk_size=1000, chunk_overlap=200),
                                  summarization_kwargs=dict(max_length=125, min_length=30))

    return long_result, short_result
