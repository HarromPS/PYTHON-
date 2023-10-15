# Merge PDF files using pyPdf merger library into a single pdf file,
# extra functionality is also welcome

import os
from PyPDF2 import PdfMerger

# list of all pdf files
lst = os.listdir("Exercise8\pdfs");
print(lst);

# merger
merger = PdfMerger();
print(type(merger));

for pdf in lst:
    with open(f"Exercise8\pdfs/{pdf}","rb") as f:
        merger.append(f);

with open("Exercise8\pdfs\Merged_result.pdf","wb") as f:
    merger.write(f);

merger.close();


