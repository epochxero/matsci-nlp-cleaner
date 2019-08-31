import pandas as pd
import langdetect
import json

initial_df = pd.read_csv('data_to_clean/initial_data.csv', encoding="ISO-8859-1")
texts = initial_df['Text'].head(100)

text_list = []

for text in texts:
    text_list.append(text)

for i in text_list:
    print(langdetect.detect(i))
