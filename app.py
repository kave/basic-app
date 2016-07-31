from flask import Flask, render_template

app = Flask('interview')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
