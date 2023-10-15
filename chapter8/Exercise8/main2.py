import os
from PyPDF2 import PdfReader

# list of all pdf files
lst = os.listdir("Exercise8\pdfs");
print(lst);

# read text
for pdf in lst:
    with open(f"Exercise8\pdfs\{pdf}","rb") as f:
        reader = PdfReader(f);
        print(reader.pages[0].extract_text(0,90));

# pip install PyPDF2[image]
count=0;
for pdf in lst:
    with open(f"Exercise8\pdfs\{pdf}","rb") as f:
        reader = PdfReader(f);
        pages = reader.pages[0];

        for imgs in pages.images:
            with open(str(0)+imgs.name,"wb") as f:
                f.write(imgs.data);
                count+=1;
