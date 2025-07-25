import pandas as pd

mcdonalds = pd.read_csv("menu.csv")
mcdonalds = mcdonalds[mcdonalds['Category'] != 'Coffee & Tea']
mcdonalds = mcdonalds[mcdonalds['Category'] != 'Beverages']

filtered = mcdonalds[['Item','Calories','Protein']]



import numpy as np

filtered['proteinRatio'] = np.where(
    filtered['Calories'] != 0,
    filtered['Protein'] / filtered['Calories'],
    0
)


sortedFilter = filtered.sort_values('proteinRatio', ascending= False)

def get_top_protein_items():
    return sortedFilter.head(5)