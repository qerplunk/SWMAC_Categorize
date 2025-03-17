from flask import Flask, jsonify, request, render_template
from src import LLM_Model, CTAs_SubCTAs


app = Flask(__name__)


""" Static file routes """

@app.route("/")
def serve_root():
    return render_template("index.html")


@app.route("/url", methods=["GET"])
def serve_url():
    return render_template("url.html")


@app.route("/description", methods=["GET"])
def serve_description():
    return render_template("description.html")


""" POST endpoints """

# Takes in a description and returns categories
@app.route("/categorize", methods=["POST"])
def generate_from_description():
    data = request.json
    if data is None:
        return jsonify({"error": "No description provided"})

    model = LLM_Model.LLM_Model()
    description = data.get("description")
    categories = model.create_sub_ctas(description)
    if categories is None:
        categories = "None"

    ctas = set()

    for category in categories.split(";"):
        category = category.strip()

        if category not in CTAs_SubCTAs.SUBCTA_TO_CTA.keys():
            print(f"{category} not valid")
            continue

        cta = CTAs_SubCTAs.SUBCTA_TO_CTA[category]
        ctas.add(cta)

    output = ""
    for cta in ctas:
        if len(output) > 0:
            output += "; "
        output += cta

    response = {"categories": output}
    return jsonify(response)


# Uses the URL param to generate a description
@app.route("/webscrape", methods=["POST"])
def description_from_url():
    data = request.json
    if data is None:
        return jsonify({"error": "No URL provided"})

    model = LLM_Model.LLM_Model()
    url = data.get("url")
    sentence_count = data.get("sentences")
    summary = model.summarize_website(url, sentence_count)

    if summary is None:
        summary = "NONE"

    response = {"description": summary}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="localhost", port=3000)
