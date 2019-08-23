from mat2vec.processing import MaterialsTextProcessor
import pandas as pd

initial_df = pd.read_csv('data_to_clean/initial_data.csv', encoding="ISO-8859-1")
initial_abstracts = (initial_df['Abstract'].head(104))
#print(initial_abstracts)
text_processor = MaterialsTextProcessor()
abstracts = []
for abstract in initial_abstracts:
    abstracts.append(abstract)

print(abstracts[19])

papers = []

for paper in papers:

    with open("%s.txt" % paper, "r", encoding="utf8") as text, open("CleanedText%s.txt" % paper, "w+", encoding="utf8") as CleanText, open("NormalisedMaterials%s.txt" % paper, "w+", encoding="utf8") as NormalisedMaterials:

        text_string = text.read()
        processed_text = text_processor.process(text_string, exclude_punct = True, make_phrases = True)

        CleanText.write("Processed Text:\n\n")
        count = 0

        for count, word in enumerate(processed_text[0]):

            CleanText.write("%s, " % word)

            if count % 100 == 0:
                print("\n")

        NormalisedMaterials.write("Materials:\n\n")

        for count, word in enumerate(processed_text[1]):

            NormalisedMaterials.write("(%s, %s), " % (word[0], word[1]))

            if count % 100 == 0:
                print("\n")
