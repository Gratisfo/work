#pip install pdfminer

import pdfminer.high_level                       
text_from_pdf = open("text_from_pdf.txt", "wb") 
with open("doc.pdf", 'rb') as file:   
    pdfminer.high_level.extract_text_to_fp(file, file_result_text_from_pdf) 
print("Распознавание завершено")                 
text_from_pdf.close()                            

with open("text_from_pdf.txt", "r", encoding="utf8") as file:  
    file = file.read()                          
    print(file)     
