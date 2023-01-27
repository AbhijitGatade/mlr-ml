from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
@app.route("/")
def fr():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/mlr")
def mlr():
    return render_template("mlr.html")

@app.route("/mlrpred", methods=["POST"])
def mlrpred():
    model = pickle.load(open("MLR.pkl","rb"))
    rds = float(request.form.get("rds"))
    admin = float(request.form.get("admin"))
    ms = float(request.form.get("ms"))
    state = request.form.get("state")
    #"R&D Spend","Administration","Marketing Spend","State"
    print(rds)
    print(admin)
    print(ms)
    print(state)

    Profit = model.predict(pd.DataFrame(columns=["RnD","Administration","MarketingSpend","State"], 
                                    data=np.array([rds, admin, ms, state]).reshape(1, 4)))
    #print(Profit)
    return render_template("mlrpred.html", Profit = int(Profit))
app.run(debug = True)