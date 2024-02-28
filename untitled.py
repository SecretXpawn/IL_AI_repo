from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModel


classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
classifier("Having three long haired, heavy shedding dogs at home, I was pretty skeptical that this could hold up to all the hair and dirt they trek in, but this wonderful piece of tech has been nothing short of a godsend for me! ")