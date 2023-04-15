from flask import Flask,render_template
app = Flask(__name__)
#TODO htkml console DOCUMENT.body.contenteditble=true


@app.route("/")
def hello_world():

    return render_template("index3.html")
        #"<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)