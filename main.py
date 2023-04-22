from flask import Flask, render_template
from datetime import date
import requests

# TODO html console DOCUMENT.body.contenteditble=true,shift+reload button for new changes
genderize = requests.get("https://api.genderize.io/?name=jhon")
agify = requests.get("https://api.agify.io?name=david")
mike_age = agify.json()['age']
peter_name = genderize.json()['name']
person_gender=genderize.json()['gender']
print(mike_age)
print(peter_name)

# formatedtime = (sunset_api.json()['results']['sunset'])
app = Flask(__name__)


@app.route("/")
def hello_world():
    today = date.today()

    return render_template("jinga.html", jinga_updated=today.strftime("%A %d %B %Y"), name=peter_name, age=mike_age,
                           gender=person_gender)
    # "<p>Hello, World!</p>"


@app.route("/<name>")
def age_name(name):
    Gender_name = requests.get(f"https://api.genderize.io/?name={name}")
    Age_name=requests.get(f"https://api.agify.io?name={name}")
    json_gender = Gender_name.json()['gender']
    json_name=Gender_name.json()['name']
    json_age=Age_name.json()['age']

    return render_template("jinga.html", gender_2=json_gender,age_2=json_age,name_2=json_name)


# def guss_number(number):
#     a = random.randrange(0, 9)
#     if number > a:
#         return f"<h1 style='text-align: center'>TO HIGH {a}</h1>" \
#                  " <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
#     elif a > number:
#          return \
#              f"<h1 style='text-align: center'>TO LOW {a}</h1>"\
#             "<img src=' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
#
#
#     else:
#         return\
#              f"<h1 style='text-align: center'>WELL DONE {a}</h1>"\
#               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
#         # return f'Post {number}'\
#         #        f"<h1 style='text-align: center'>Your guess  is {number}</h1>"\
#         #          f"<h1 style='text-align: center'>,My random number is  {a}</h1>"
#
#

if __name__ == "__main__":
    app.run(debug=True)
