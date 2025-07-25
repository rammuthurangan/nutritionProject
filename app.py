from flask import Flask, render_template, request
import pandas as pd
import chilis
import wendys
import popeyes
import mcdonalds

app = Flask(__name__)

def get_top_df(df):
    return df.sort_values(by="proteinRatio", ascending=False).head(5)

@app.route("/", methods=["GET", "POST"])
def index():
    table_html = ""
    name = ""

    if request.method == "POST":
        chain = request.form.get("chain")
        try:
            if chain == "Chili's":
                df = chilis.get_top_protein_items()
            elif chain == "Wendy's":
                df = wendys.get_top_protein_items()
            elif chain == "Popeyes":
                df = popeyes.get_top_protein_items()
            elif chain == "McDonald's":
                df = mcdonalds.get_top_protein_items()
            else:
                raise ValueError("Unknown chain selected.")

            name = chain
            table_html = get_top_df(df).to_html(classes="table", index=False, border=1)

        except Exception as e:
            table_html = f"<p>Error: {e}</p>"

    return render_template("index.html", name=name, table=table_html)

if __name__ == "__main__":
    app.run(debug=True)

