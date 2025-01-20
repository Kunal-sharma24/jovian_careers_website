from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Software Engineer",
        "company": "ABC Corporation",
        "location": "New York",
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "company": "XYZ Inc.",
        "location": "San Francisco",
    },
    {
        "id": 3,
        "title": "Product Manager",
        "company": "PQR Ventures",
        "location": "Chicago",
    }
]


@app.route("/")
def hello_world():
    return render_template('index.html',jobs=JOBS)

@app.route("/jobs")
def get_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)