"""
Этот модуль содержит реализованную предварительно обученную модель машинного
перевода и краткого изложения русскоязычного текста.
"""

from transformers import pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from transformers import MBartTokenizer


def translator(article_en: str) -> str:
    '''
    Функция реализует модель многоязычного машинного перевода
    mbart-large-50-many-to-many-mmt на целевой язык - Русский
    :param article_en: строка содержащая текст на английском языке.
    :return: строка содержащая переведенный на русский язык исходный текст.
    '''
    model = (MBartForConditionalGeneration.
             from_pretrained("facebook/mbart-large-50-many-to-many-mmt"))
    tokenizer = (MBart50TokenizerFast.
                 from_pretrained("facebook/mbart-large-50-many-to-many-mmt"))

    tokenizer.src_lang = "en_XX"
    encoded_ar = tokenizer(article_en, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_ar,
        early_stopping=False,
        forced_bos_token_id=tokenizer.lang_code_to_id["ru_RU"]
    )
    transleted = (tokenizer.
                  batch_decode(generated_tokens, skip_special_tokens=True))

    print(transleted)
    transleted = transleted[0]
    return transleted


def summarizer(article_text: str) -> str:
    '''
    Реализует модель mbart_ru_sum_gazeta генераци резюме на
    основе исходного текста

    :param article_text: строка содержащая полный текст на русском языке.
    :return: строка содержащая краткое тезисное изложение исходного текста.
    '''
    model_name = "IlyaGusev/mbart_ru_sum_gazeta"
    tokenizer = MBartTokenizer.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)

    input_ids = tokenizer(
        [article_text],
        min_length=50,
        max_length=600,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    print(summary)
    return summary
