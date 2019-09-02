from mat2vec.processing import MaterialsTextProcessor
import pandas as pd

#Function to split references from texts, remove trivial/empty entries, and process texts.
#Args: filename: Name of .csv file, e.g. "FullTexts.csv"
#      output_path: Path of the output file as a raw string literal: e.g. r"C:\Users\...\small_dataframe_100_cleaned.csv"

def processFile(filename, output_path):

    #Preliminary cleaning of the data set; splits references based on length, removes empty/trivial rows.
    #Code for data frame columns: 0- DOI, 1- Title, 2- Abstract, 3- Date, 4- Text, 5- References
    #Cols: ['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'DOI', 'Title', 'Abstract', 'Publication Date', 'Text', 'References']

    initial_df = pd.read_csv(filename, encoding="utf8")
    initial_df = initial_df[~pd.isna(initial_df["Unnamed: 0.1.1"]) & ~pd.isna(initial_df["Title"])]

    #Iterate through the rows of the data frame; if references are absent, and the text/abstract is trivial, then remove the row.
    #If references are absent, and the text is non-trivial, scan for references in the text and split it. Reference sections are not updated.

    ref_synonyms = ["references:", "references", "reference:", "reference:", "bibliography", "bibliography:", "bibliographies:", "bibliographies",
                    "reference list:", "reference list", "citations:", "citations"]


    for row in initial_df.itertuples():

        if pd.isna(row[6]) and (not pd.isna(row[5]) or not pd.isna(row[3])):
              
            if not pd.isna(row[5]):
                
                if len(row[5]) <= 100 and pd.isna(row[3]):

                    initial_df.drop(row[0], inplace = True)

                elif len(row[5]) <= 100 and not pd.isna(row[3]):

                    initial_df.at[row[0], "Title"] = " "
            
                else:
                                                         
                    text = row[5].lower()
                    ref_found = False

                    for synonym in ref_synonyms:

                       if synonym in text and not ref_found:
        
                           syn_indices = [match.start() for match in regex.finditer(synonym, text)]

                           for syn_index in syn_indices:

                               subtext = text[syn_index:]

                               if len(subtext.split()) <= 300:

                                   ref_found = not ref_found
                                   new_text = text[:syn_index]
                                   initial_df.at[row[0], "Title"] = new_text
                          
                                   break

                       elif ref_found:

                           break
                                
                                                                                                        
    #Extracts relevant material from .csv file

    row_count = len(initial_df.index)
    titles = (initial_df['Unnamed: 0.1'].head(row_count))
    abstracts, full_texts, references = (initial_df['Unnamed: 0.1.1'].head(row_count), initial_df['Title'].head(row_count), initial_df["Abstract"].head(row_count))
    DOIs, pub_dates = (initial_df['Unnamed: 0'].head(row_count)), (initial_df['DOI'].head(row_count))


    #Adds full papers into an array; converts titles, DOIs, pub_dates to lists
    abstracts, full_texts, references = list(abstracts), list(full_texts), list(references) 
    titles, DOIs, pub_dates = list(titles), list(DOIs), list(pub_dates)
    papers = [abstracts[i] + " " + full_texts[i] for i in range(0, row_count)]

    #Processes full papers and adds the processed text and normalised materials into a new .csv file
    text_processor = MaterialsTextProcessor()
    processed_texts, norm_mats = [], []

    for paper in papers:

        processed_paper = text_processor.process(paper, exclude_punct = True, make_phrases = True)
        processed_texts += [" ".join(processed_paper[0])]
        norm_mats += [" ".join([material[1] for material in processed_paper[1]])]
           

    #Output final data frame
    processed_data = {"DOIs": DOIs, "Publication Dates": pub_dates, "Titles": titles, "Processed Text": processed_texts, "Normalised Materials": norm_mats}
    final_df = pd.DataFrame(processed_data, columns = ["DOIs", "Publication Dates", "Titles", "Processed Text", "Normalised Materials"])
    final_df.to_csv(output_path, index = False)

#processFile('small_dataframe_100.csv', r'C:\Users\...\small_dataframe_100_cleaned.csv')
