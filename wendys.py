from pdfquery import PDFQuery
import pandas as pd

pdf = PDFQuery("wendys (1).pdf")
pdf.load()
text_elements = pdf.pq('LTTextLineHorizontal')
text_list = [el.text.strip() for el in text_elements if el.text and el.text.strip()]

hamburgers = []
for i in range(23):
    base = i
    name = text_list[base]
    calories = text_list[base + 23]
    protein = text_list[base + 161]
    hamburgers.append((name, calories, protein))
hamburgers = [item for item in hamburgers if item[0] != "4 Pc Chicken Nuggets"]

salads = []
for k in range(229, 231):
    base = k
    name = text_list[base]
    calories = text_list[base + 2]
    protein = text_list[base + 14]
    salads.append((name, calories, protein))

sides = []
for l in range(269, 280):
    base = l
    name = text_list[base]
    calories = text_list[base + 11]
    protein = text_list[base + 77]
    sides.append((name, calories, protein))

kids = []
for j in range(374, 377):
    base = j
    name = text_list[base]
    calories = text_list[base + 3]
    protein = text_list[base + 21]
    kids.append((name, calories, protein))

breakfast = []
for b in range(418, 433):
    base = b
    name = text_list[base]
    calories = text_list[base + 28]
    protein = text_list[base + 209]
    breakfast.append((name, calories, protein))

# Final calculations
menuItems = hamburgers + kids + sides + breakfast + salads
ratios = []
for name, cal, prot in menuItems:
    try:
        cal_float = float(cal)
        prot_float = float(prot)
        ratio = prot_float / cal_float if cal_float > 0 else 0
        ratios.append((name, cal_float, prot_float, ratio))
    except ValueError:
        continue

ratios_sorted = sorted(ratios, key=lambda x: x[3], reverse=True)
wendyssortedDF = pd.DataFrame(ratios_sorted, columns=["Item", "Calories", "Protein", "proteinRatio"])
print(wendyssortedDF.head(5))
def get_top_protein_items():
    return wendyssortedDF.head(5)
