"""
Этот модуль содержит реализованную предварительно обученную модель машинного
перевода и краткого изложения русскоязычного текста.
"""

from transformers import pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from transformers import MBartTokenizer
import torch

article_ent = """
Scientists used the term Anthropocene to describe the epoch where humans began to have a significant impact on Earth’s ecosystem and geology. The planet is about 4.5 billion years old, and modern humans have only been around for 200,000 years. In that short amount of time, Homo sapiens have significantly altered Earth’s biological, chemical, and physical systems. 

The beginning of the Anthropocene Epoch is still being debated and has a large range. Some suggest it began thousands of years ago. Others pinpoint 1950, when plutonium isotopes from nuclear weapons tests were found at the bottom of a relatively pristine lake in Canada. Emissions of carbon dioxide and other greenhouse gasses accelerating global warming, ocean acidification, increased species extinction, habitat destruction, and natural resource extraction are additional signs that humans have dramatically modified our planet.

The idea is much the same as the discussion of the Anthropocene on Earth—the exploration of how much humans have impacted our planet, study co-author and Kansas University archaeologist Justin Holcomb said in a statement. Similarly, on the moon, we argue the Lunar Anthropocene already has commenced, but we want to prevent massive damage or a delay of its recognition until we can measure a significant lunar halo caused by human activities, which would be too late.

On September 13, 1950, the USSR’s uncrewed spacecraft Luna 2 first descended onto the lunar surface. In the decades since, over 100 other spacecraft have touched the moon. NASA’s Apollo Lunar Modules followed in the 1960s and 1970s and China got the first seedling to sprout on the moon in 2019. The Indian Space Research Organization (ISRO) successfully landed on the moon with the Chandrayaan-3 mission in August. 

All of this activity has displaced more of the moon’s surface than natural meteroid impacts and other natural processes. 

In Nature Geoscience, the team argues that upcoming lunar missions and projects will change the face of the moon in more extreme ways. They believe that the concept of the Lunar Anthropocene may help correct a myth that the moon is barely impacted by human activity and is an unchanging environment.

“Cultural processes are starting to outstrip the natural background of geological processes on the moon,” Holcomb said. “These processes involve moving sediments, which we refer to as ‘regolith,’ on the moon. Typically, these processes include meteoroid impacts and mass movement events, among others. However, when we consider the impact of rovers, landers and human movement, they significantly disturb the regolith.”

They believe that the lunar landscape will look entirely different in only half a century, with multiple countries having some presence on the surface of the moon. 

University College London astrophysicist Ingo Waldmann told New Scientist that the moon has entered its version of the Anthropocene. He said that lunar geology isn’t very dramatic. The moon might see an asteroid impact every couple of million years, but there aren’t too many other big events. “Just us walking on it has a bigger environmental impact than anything that would happen to the moon in hundreds of thousands of years,” said Waldmann.

The moon is currently in a geological division called the Copernican Period. It dates over one billion years ago. In that time, Earth has gone through roughly 15 geological periods.
"""

def trans_module(text, source_language, target_language, piece_len=256, max_batch =8):
    '''
    piece_len: max length of input
    max_batch: num sample of translation per time
    '''
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    torch.cuda.is_available()

    model_path = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_path)
    ml2en_tokenizer = MBart50TokenizerFast.from_pretrained(model_path)
    ml2en_model = MBartForConditionalGeneration.from_pretrained(model_path).to(device)
    ml2en_tokenizer.src_lang = source_language
    
    input_id = ml2en_tokenizer.encode(text)
    
    # special inputid for different language
    start_id=[input_id[0]]
    end_id=[input_id[-1]]
    input_id = input_id[1:-1]
    
    #save translated result
    res_text=''
    
    input_id_list= []
    attention_mask_list=[]
    
    # create batch samples
    for i in range(0,len(input_id),piece_len):
        tmp_id = start_id+input_id[i:i+piece_len]+end_id
        if len(input_id)<piece_len:
            #only one sample
            input_id_list.append(tmp_id)
            attention_mask_list.append([1]*len(tmp_id))
            break
        else:
            input_id_list.append(tmp_id+((piece_len+2)-len(tmp_id))*[1])#padding
            attention_mask_list.append([1]*len(tmp_id)+((piece_len+2)-len(tmp_id))*[0])
    
    # translation
    for i in range(0, len(input_id_list),max_batch):
        input_id_list_batch = input_id_list[i:i+max_batch]
        attention_mask_list_batch= attention_mask_list[i:i+max_batch]
        input_dict = {'input_ids':torch.LongTensor(input_id_list_batch).to(device),"attention_mask":torch.LongTensor(attention_mask_list_batch).to(device)}
        generated_tokens = ml2en_model.generate(
            **input_dict,
            forced_bos_token_id=ml2en_tokenizer.lang_code_to_id[target_language]
        )
        res_tmp =ml2en_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        
        # concate
        res_text+=' '.join(res_tmp)
        print(res_text)
    return res_text

def translator(article_en: str) -> str:
    article_en = article_en.replace('\n', '')
    print()
    print(article_en)

    return trans_module(article_en, source_language="en_XX", target_language="ru_RU", piece_len=256, max_batch =8)
    '''
    Функция реализует модель многоязычного машинного перевода
    mbart-large-50-many-to-many-mmt на целевой язык - Русский
    :param article_en: строка содержащая текст на английском языке.
    :return: строка содержащая переведенный на русский язык исходный текст.
    '''
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBartTokenizer.from_pretrained("facebook/mbart-large-50-many-to-many-mmt", src_lang="en_XX", tgt_lang="ru_RU")

    tokenizer.src_lang = "en_XX"
    encoded_en = tokenizer(article_en, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_en,
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
