from mat2vec.processing import MaterialsTextProcessor

text_processor = MaterialsTextProcessor()
papers = []

for Paper in papers:
    
    with open("Paper.txt", "r", encoding="utf8") as text, open("CleanedTextPaper.txt", "w+", encoding="utf8") as CleanText, open("NormalisedMaterialsPaper.txt", "w+", encoding="utf8") as NormalisedMaterials:

        text_string = text.read()
        processed_text = text_processor.process(text_string, exclude_punct = True, make_phrases = True)

        CleanTextPaper.write("Processed Text:\n\n")
        count = 0

        for count, word in enumerate(processed_text[0]):

            CleanText.write("%s, " % word)

            if count % 100 == 0:
                print("\n")

        NormalisedMaterialsPaper.write("Materials:\n\n")         

        for count, word in enumerate(processed_text[1]):

            NormalisedMaterialsPaper.write("(%s, %s), " % (word[0], word[1]))

            if count % 100 == 0:
                print("\n")        
            

        

    
