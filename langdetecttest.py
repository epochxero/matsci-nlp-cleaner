import pandas as pd
import langdetect
import json

initial_df = pd.read_csv('cleaned.csv', encoding="ISO-8859-1")
texts = initial_df['Processed Text'].head(100)

text_list = []

for text in texts:
    text_list.append(text)

for i in text_list:
    print(langdetect.detect(i))
