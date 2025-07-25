import pdfplumber
import pandas as pd
import numpy as np

pdf_path = "Chilis.pdf"

rows = []


with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages[2:]:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                rows.append(row)



chilisDF = pd.DataFrame(rows)
#chilisDF = chilisDF[~chilisDF[0].str.lower().str.contains("add", na=False)]
#chilisDF = chilisDF[~chilisDF[0].str.lower().str.contains("portion", na=False)]
#chilisDF = chilisDF[~chilisDF[0].str.lower().str.contains("choice", na=False)]

#add shrimp to all steaks
#sizzingthe table chicken
#seared shrimp
#add all combos



chilisDF[1] = pd.to_numeric(chilisDF[1], errors='coerce')
chilisDF[10] = pd.to_numeric(chilisDF[10], errors='coerce')
chilisDF = chilisDF.dropna(subset=[1, 10])
chilisDF = chilisDF.dropna(how = 'all').drop_duplicates()
chilisDF['proteinRatio'] = chilisDF[10]/chilisDF[1]
sortedDF = chilisDF.sort_values(by='proteinRatio', ascending=False)
#print(sortedDF[[0, 1, 10, 'proteinRatio']].head(20))

ribeye_row = chilisDF[chilisDF[0] == "Classic Ribeye"].iloc[0]
ribeye_cals = ribeye_row[1]
ribeye_protein = ribeye_row[10]

shrimp_cals = 60
shrimp_protein = 11

combined_cals = ribeye_cals + shrimp_cals
combined_protein = ribeye_protein + shrimp_protein
combined_ratio = combined_protein / combined_cals

new_row = ribeye_row.copy()
new_row[0] = "Classic Ribeye w/ Seared Shrimp (Full)"
new_row[1] = combined_cals
new_row[10] = combined_protein
new_row['proteinRatio'] = combined_ratio

chilisDF = pd.concat([chilisDF, pd.DataFrame([new_row])], ignore_index=True)
#print(chilisDF[chilisDF[0] == "Classic Ribeye w/ Seared Shrimp (Full)"][[0,1,10,'proteinRatio']])
Sirloin_row = chilisDF[chilisDF[0] == "Classic Sirloin 10 oz"].iloc[0]
Sirloin_cals = Sirloin_row[1]
Sirloin_protein = Sirloin_row[10]

combined_calsS = Sirloin_cals + shrimp_cals
combined_proteinS = Sirloin_protein + shrimp_protein
combined_ratioS = combined_proteinS / combined_calsS

new_rowS = Sirloin_row.copy()
new_rowS[0] = "Classic Sirloin 10 oz w/ Seared Shrimp (Full)"
new_rowS[1] = combined_calsS
new_rowS[10] = combined_proteinS
new_rowS['proteinRatio'] = combined_ratioS

chilisDF = pd.concat([chilisDF, pd.DataFrame([new_rowS])], ignore_index=True)
#print(chilisDF[chilisDF[0] == "Classic Sirloin 10 oz w/ Seared Shrimp (Full)"][[0,1,10,'proteinRatio']])

Sirloin6_row = chilisDF[chilisDF[0] == "Classic Sirloin 6 oz"].iloc[0]
Sirloin6_cals = Sirloin6_row[1]
Sirloin6_protein = Sirloin6_row[10]

combined_calsS6 = Sirloin6_cals + shrimp_cals
combined_proteinS6 = Sirloin6_protein + shrimp_protein
combined_ratioS6 = combined_proteinS6 / combined_calsS6

new_rowS6 = Sirloin6_row.copy()
new_rowS6[0] = "Classic Sirloin 6 oz w/ Seared Shrimp (Full)"
new_rowS6[1] = combined_calsS6
new_rowS6[10] = combined_proteinS6
new_rowS6['proteinRatio'] = combined_ratioS6

chilisDF = pd.concat([chilisDF, pd.DataFrame([new_rowS6])], ignore_index=True)
#print(chilisDF[chilisDF[0] == "Classic Sirloin 6 oz w/ Seared Shrimp (Full)"][[0,1,10,'proteinRatio']])


SurfRibeye_row = chilisDF[chilisDF[0] == "Surf & Turf Ribeye"].iloc[0]
SurfRibeye_cals = SurfRibeye_row[1]
SurfRibeye_protein = SurfRibeye_row[10]

combined_calsSurfRibeye = SurfRibeye_cals + shrimp_cals
combined_proteinSurfRibeye = SurfRibeye_protein  + shrimp_protein
combined_ratioSurfRibeye = combined_proteinSurfRibeye / combined_calsSurfRibeye

new_rowSurfRibeye = SurfRibeye_row.copy()
new_rowSurfRibeye[0] = "Surf & Turf Ribeye w/ Seared Shrimp (Full)"
new_rowSurfRibeye[1] = combined_calsSurfRibeye
new_rowSurfRibeye[10] = combined_proteinSurfRibeye
new_rowSurfRibeye['proteinRatio'] = combined_ratioSurfRibeye

chilisDF = pd.concat([chilisDF, pd.DataFrame([new_rowSurfRibeye])], ignore_index=True)
#print(chilisDF[chilisDF[0] == "Surf & Turf Ribeye w/ Seared Shrimp (Full)"][[0,1,10,'proteinRatio']])


SurfSir_row = chilisDF[chilisDF[0] == "Surf & Turf Sirloin 10 oz"].iloc[0]
SurfSir_cals = SurfSir_row[1]
SurfSir_protein = SurfSir_row[10]

combined_calsSurfSir = SurfSir_cals  + shrimp_cals
combined_proteinSurfSir = SurfSir_protein  + shrimp_protein
combined_ratioSurfSir = combined_proteinSurfSir /combined_calsSurfSir

new_rowSurfSir = SurfSir_row.copy()
new_rowSurfSir[0] = "Surf & Turf Sirloin 10 oz w/ Seared Shrimp (Full)"
new_rowSurfSir[1] = combined_calsSurfSir
new_rowSurfSir[10] = combined_proteinSurfSir
new_rowSurfSir['proteinRatio'] = combined_ratioSurfSir

chilisDF = pd.concat([chilisDF, pd.DataFrame([new_rowSurfSir])], ignore_index=True)
#print(chilisDF[chilisDF[0] == "Surf & Turf Sirloin 10 oz w/ Seared Shrimp (Full)"][[0,1,10,'proteinRatio']])
fajita = chilisDF[chilisDF[0] == "Fajita Peppers & Onions"].iloc[0]
GrilledChicken = chilisDF[chilisDF[0] == "Grilled Chicken (1 portion)"].iloc[0]
GrilledSteak = chilisDF[chilisDF[0] == "Grilled Steak (1 portion)"].iloc[0]
SearedShrimp = chilisDF[chilisDF[0] == "Seared Shrimp (1 portion)"].iloc[0]
fajitaChickenSteak = fajita.copy()
fajitaChickenSteak[1] = fajita[1] + GrilledChicken[1] + GrilledSteak[1]
fajitaChickenSteak[10] = fajita[10] + GrilledChicken[10] + GrilledSteak[10]
fajitaChickenSteak[0] = "Sizzling Fajita + Chicken + Steak"

# fajita with chicken + shrimp
fajitaChickenShrimp = fajita.copy()
fajitaChickenShrimp[1] = fajita[1] + GrilledChicken[1] + SearedShrimp[1]
fajitaChickenShrimp[10] = fajita[10] + GrilledChicken[10] + SearedShrimp[10]
fajitaChickenShrimp[0] = "Sizzling Fajita + Chicken + Shrimp"

# fajita with shrimp + steak
fajitaShrimpSteak = fajita.copy()
fajitaShrimpSteak[1] = fajita[1] + SearedShrimp[1] + GrilledSteak[1]
fajitaShrimpSteak[10] = fajita[10] + SearedShrimp[10] + GrilledSteak[10]
fajitaChickenSteak['proteinRatio'] = fajitaChickenSteak[10] / fajitaChickenSteak[1]
fajitaChickenShrimp['proteinRatio'] = fajitaChickenShrimp[10] / fajitaChickenShrimp[1]
fajitaShrimpSteak['proteinRatio'] = fajitaShrimpSteak[10] / fajitaShrimpSteak[1]
fajitaShrimpSteak[0] = "Sizzling Fajita + Shrimp + Steak"

combo_df = pd.DataFrame([fajitaChickenSteak, fajitaChickenShrimp, fajitaShrimpSteak])
chilisDF = pd.concat([chilisDF, combo_df], ignore_index=True)
chilisDF = chilisDF[chilisDF[0] != "Grilled Chicken (1 portion)"].reset_index(drop=True)
chilisDF = chilisDF[chilisDF[0] != "Add Seared Shrimp - Half Order"].reset_index(drop=True)



fajita2 = chilisDF[chilisDF[0] == "Fajita Peppers & Onions"].iloc[1]
GrilledChicken2 = chilisDF[chilisDF[0] == "Grilled Chicken (1 choice)"].iloc[0]
GrilledSteak2 = chilisDF[chilisDF[0] == "Grilled Steak (1 choice)"].iloc[0]
SearedShrimp2 = chilisDF[chilisDF[0] == "Seared Shrimp (1 choice)"].iloc[0]

fajitaChickenSteak2 = fajita2.copy()
fajitaChickenSteak2[1] = fajita2[1] + GrilledChicken2[1] + GrilledSteak2[1]
fajitaChickenSteak2[10] = fajita2[10] + GrilledChicken2[10] + GrilledSteak2[10]
fajitaChickenSteak2[0] = "PP Fajita + Chicken + Steak"

# fajita with chicken + shrimp
fajitaChickenShrimp2 = fajita2.copy()
fajitaChickenShrimp2[1] = fajita2[1] + GrilledChicken2[1] + SearedShrimp2[1]
fajitaChickenShrimp2[10] = fajita2[10] + GrilledChicken2[10] + SearedShrimp2[10]
fajitaChickenShrimp2[0] = "PP Fajita + Chicken + Shrimp"

# fajita with shrimp + steak
fajitaShrimpSteak2 = fajita2.copy()
fajitaShrimpSteak2[1] = fajita2[1] + SearedShrimp2[1] + GrilledSteak2[1]
fajitaShrimpSteak2[10] = fajita2[10] + SearedShrimp2[10] + GrilledSteak2[10]
fajitaShrimpSteak2[0] = "PP Fajita + Shrimp + Steak"

fajitaChickenSteak2['proteinRatio'] = fajitaChickenSteak2[10] / fajitaChickenSteak2[1]
fajitaChickenShrimp2['proteinRatio'] = fajitaChickenShrimp2[10] / fajitaChickenShrimp2[1]
fajitaShrimpSteak2['proteinRatio'] = fajitaShrimpSteak2[10] / fajitaShrimpSteak2[1]

fajitaallthree = fajita2.copy()
fajitaallthree[1] = fajita2[1] + SearedShrimp2[1] + GrilledSteak2[1] + GrilledChicken2[1]
fajitaallthree[10] = fajita2[10] + SearedShrimp2[10] + GrilledSteak2[10] + GrilledChicken2[10]
fajitaallthree[0] = "PP Fajita + Shrimp + Steak + Chicken"

fajitaallthree['proteinRatio'] = fajitaallthree[10] / fajitaallthree[1]

combo_df = pd.DataFrame([fajitaChickenSteak2, fajitaChickenShrimp2, fajitaShrimpSteak2,fajitaallthree ])
chilisDF = pd.concat([chilisDF, combo_df], ignore_index=True)





chilisDF = chilisDF[chilisDF[0] != "Grilled Chicken (1 choice)"].reset_index(drop=True)
chilisDF = chilisDF[chilisDF[0] != "Add Seared Shrimp - Half Order"].reset_index(drop=True)
chilisDF = chilisDF[chilisDF[0] != "Add Shrimp"].reset_index(drop=True)
chilisDF = chilisDF[chilisDF[0] != "Add Seared Shrimp - Full Order"].reset_index(drop=True)
chilisDF = chilisDF[chilisDF[0] != "Seared Shrimp (1 portion)"].reset_index(drop=True)
chilisDF = chilisDF[chilisDF[0] != "Seared Shrimp (1 choice)"].reset_index(drop=True)
chilisDF = chilisDF[chilisDF[0] != "Add Ancho Salmon"].reset_index(drop=True)


chilisDF.loc[chilisDF[0] == "Grilled Chicken", 0] = "Sizzling Fajitas w/o Topping Chicken"
chilisDF.rename(columns={0: "Item", 1: "Calories", 10: "Protein"}, inplace=True)
chilisDF = chilisDF[["Item", "Calories", "Protein", "proteinRatio"]]
sortedDF = chilisDF.sort_values(by='proteinRatio', ascending=False)


def get_top_protein_items():
    return chilisDF.sort_values("proteinRatio", ascending=False).head(5)

