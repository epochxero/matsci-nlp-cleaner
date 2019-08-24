from mat2vec.processing import MaterialsTextProcessor
import pandas as pd

#Extracts relevant material from .csv file
initial_df = pd.read_csv('DataSet.csv', encoding="ISO-8859-1")
titles = (initial_df['Unnamed: 0.1'].head(100))
abstracts, full_texts = (initial_df['Unnamed: 0.1.1'].head(100)), (initial_df['Title'].head(100))
DOIs, pub_dates = (initial_df['Unnamed: 0'].head(100)), (initial_df['DOI'].head(100))


#Adds full papers into an array; converts titles, DOIs, pub_dates to lists
papers = [ abstracts[i] + " " + full_texts[i] for i in range(0,100)]
titles, DOIs, pub_dates = list(titles), list(DOIs), list(pub_dates)


#Processes full papers and adds the processed text and normalised materials into a new .csv file
text_processor = MaterialsTextProcessor()
processed_texts, norm_mats = [], []

for paper in papers:

    processed_paper = text_processor.process(paper, exclude_punct = True, make_phrases = True)
    processed_texts += [" ".join(processed_paper[0])]
    norm_mats += [" ".join([material[1] for material in processed_paper[1]])]
       

#Output final data frame
location = ""
processed_data = {"DOIs": DOIs, "Publication Dates": pub_dates, "Titles": titles, "Processed Text": processed_texts, "Normalised Materials": norm_mats}
final_df = pd.DataFrame(processed_data, columns = ["DOIs", "Publication Dates", "Titles", "Processed Text", "Normalised Materials"])
final_df.to_csv(r"%s" % location, index = False)

