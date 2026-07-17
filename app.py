from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result=""
    found=[]
    score=0
    links=[]

    suspicious_words=[
        "urgent",
        "click here",
        "verify",
        "password",
        "bank",
        "winner",
        "free",
        "account suspended"
    ]

    if request.method=="POST":

        email=request.form["email"].lower()

        # suspicious keywords check

        for word in suspicious_words:

            if word in email:

                found.append(word)
                score += 15


        # links detect

        links = re.findall(
            r'https?://\S+',
            email
        )

        if len(links)>0:

            score += 30


        # score limit

        if score>100:
            score=100


        # risk result

        if score<=30:
            result="Low Risk"

        elif score<=70:
            result="Medium Risk"

        else:
            result="High Risk"



    return render_template(

        "phishing.html",

        result=result,
        found=found,
        score=score,
        links=links
    )



if __name__ == "__main__":
    app.run(debug=True)
