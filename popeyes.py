import pdfplumber
import pandas as pd
import numpy as np

pdf_path = "PLK_Nutrition.pdf"
rows = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                rows.append(row)

#2 is calories
#12 is protein
popeyesDF = pd.DataFrame(rows)
popeyesDF = popeyesDF.iloc[3:]
pd.set_option('display.max_columns', None)


popeyesDF = popeyesDF.dropna()
popeyesDF[2] = pd.to_numeric(popeyesDF[2], errors='coerce')
popeyesDF[12] = pd.to_numeric(popeyesDF[12], errors='coerce')
popeyesDF[0] = popeyesDF[0].astype(str).str.strip() + " (" + popeyesDF[1].astype(str).str.strip() + ")"
popeyesDF['proteinRatio'] = popeyesDF[12] / popeyesDF[2]

sortedDF = popeyesDF[[0, 1, 2, 12, 'proteinRatio']].sort_values(by='proteinRatio', ascending=False)
popeyesDF.rename(columns={0: "Item", 1: "Serving", 2: "Calories", 12: "Protein"}, inplace=True)
popeyesDF = popeyesDF[["Item", "Calories", "Protein", "proteinRatio"]]
print(popeyesDF.sort_values("proteinRatio", ascending=False).head(5))
def get_top_protein_items():
    return popeyesDF.sort_values("proteinRatio", ascending=False).head(5)

import os

print(os.getcwd())