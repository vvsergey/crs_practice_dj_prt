from transformers import pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from transformers import MBartTokenizer


article_en = """
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


def translator(article_en):
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

    tokenizer.src_lang = "en_XX"
    encoded_ar = tokenizer(article_en, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_ar,
        early_stopping=False,
        forced_bos_token_id=tokenizer.lang_code_to_id["ru_RU"]
    )
    transleted = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    print(transleted)
    transleted = transleted[0]
    return transleted

def summarizer(article_text):
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

