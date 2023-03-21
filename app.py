from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    lst = []
    if request.method == "POST":
        target = request.form.get("target")
        regex = request.form.get("regex")
        lst = re.findall(regex, target)
    return render_template("regex2_index.html", lst=lst)

if __name__ == '__main__':
    app.run(debug=True)
