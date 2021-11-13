from application import app
from flask import render_template, request
from application.forms import RestaurantForm
from application.chooser import restaurantChooser
import os


# @app.route("/")
# def index():
#     return render_template("index.html", index=True)




# Restaurant Chooser Route

@app.route("/", methods=['GET', 'POST'])
@app.route("/restaurants", methods=['GET', 'POST'])
def restaurants():
    showMap = False
    choice = ""
    form = RestaurantForm()
    
    if request.method == "POST":
        choiceHolder=""
        choiceHolder = restaurantChooser(form.searchLocation.data, form.searchKeyWord.data, form.searchRadius.data)
        choiceHolder.run()
        choice = choiceHolder.chosen
        showMap = True

    return render_template("restaurants.html", title="Restaurant Chooser", restaurants = True, form=form, choice=choice, apiKey = os.environ.get('API_KEY'), showMap = showMap)