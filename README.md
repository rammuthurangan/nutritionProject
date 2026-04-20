# Fast Food Protein Tracker

A Python Flask application that analyzes nutrition data from popular fast food chains to find menu items with the best protein-to-calorie ratios.

## Features

- Parses nutrition PDFs from multiple fast food chains (Chili's, Wendy's, Popeyes, McDonald's)
- Calculates protein-to-calorie ratios for each menu item
- Web interface to browse top high-protein items by restaurant
- Generates static HTML reports for offline viewing

## Supported Chains

- Chili's
- Wendy's
- Popeyes
- McDonald's

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install flask pandas pdfplumber
```

## Usage

### Web App
```bash
python app.py
```
Visit `http://localhost:5000` to select a chain and view top protein items.

### Generate Static Report
```bash
python main.py
```
Creates `top_fast_food_items.html` with all chains' top items.

## How It Works

1. Nutrition PDFs are parsed using `pdfplumber` to extract menu data
2. Protein ratio is calculated as `protein (g) / calories`
3. Items are ranked by this ratio to find the most protein-dense options
4. Results display the top 5 items per chain

## Project Structure

```
├── app.py           # Flask web application
├── main.py          # Static HTML report generator
├── chilis.py        # Chili's PDF parser
├── wendys.py        # Wendy's PDF parser
├── popeyes.py       # Popeyes PDF parser
├── mcdonalds.py     # McDonald's data handler
├── menu.csv         # McDonald's nutrition data
├── templates/       # Flask HTML templates
└── static/          # Static assets
```
