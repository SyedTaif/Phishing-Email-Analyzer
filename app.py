from flask import Flask, render_template, request, make_response
import re
from io import BytesIO

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

# Store latest analysis for PDF
latest_report = {}


@app.route("/", methods=["GET", "POST"])
def home():

    global latest_report

    result = None
    risk_score = 0
    threat_level = "Low"
    recommendations = []

    if request.method == "POST":

        email_content = request.form.get("email_content", "")

        email = email_content.lower()

        # --------------------------------
        # Phishing Keywords
        # --------------------------------

        phishing_keywords = [

            "urgent",
            "verify",
            "login",
            "click here",
            "password",
            "bank",
            "account suspended",
            "confirm",
            "security alert",
            "limited time",
            "winner",
            "claim",
            "gift",
            "invoice",
            "payment",
            "immediately"

        ]

        for keyword in phishing_keywords:

            if keyword in email:

                risk_score += 8

        if risk_score > 0:

            recommendations.append(
                "Suspicious phishing-related keywords detected."
            )

        # --------------------------------
        # URL Detection
        # --------------------------------

        urls = re.findall(
            r'https?://[^\s]+',
            email
        )

        if urls:

            risk_score += 20

            recommendations.append(
                "Email contains one or more URLs."
            )

        # --------------------------------
        # Suspicious Domains
        # --------------------------------

        suspicious_domains = [

            ".ru",
            ".xyz",
            ".tk",
            ".top",
            ".click",
            ".gq"

        ]

        for url in urls:

            for domain in suspicious_domains:

                if domain in url:

                    risk_score += 15

                    recommendations.append(
                        f"Suspicious domain detected: {url}"
                    )

        # --------------------------------
        # Sender Detection
        # --------------------------------

        sender = re.findall(

            r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',

            email_content

        )

        if sender:

            recommendations.append(

                f"Sender Email: {sender[0]}"

            )

        # --------------------------------
        # Uppercase Detection
        # --------------------------------

        uppercase_words = re.findall(

            r'\b[A-Z]{4,}\b',

            email_content

        )

        if uppercase_words:

            risk_score += 10

            recommendations.append(

                "Too many uppercase words detected."

            )

        # --------------------------------
        # Multiple Exclamation Marks
        # --------------------------------

        if email_content.count("!") >= 3:

            risk_score += 10

            recommendations.append(

                "Too many exclamation marks detected."

            )

                    # --------------------------------
        # Maximum Score
        # --------------------------------

        if risk_score > 100:
            risk_score = 100

        # --------------------------------
        # Final Result
        # --------------------------------

        if risk_score >= 70:

            result = "🚨 Phishing Email Detected"
            threat_level = "High"

        elif risk_score >= 40:

            result = "⚠️ Suspicious Email"
            threat_level = "Medium"

        else:

            result = "✅ Email Appears Safe"
            threat_level = "Low"

        # --------------------------------
        # Default Recommendation
        # --------------------------------

        if not recommendations:

            recommendations.append(
                "No obvious phishing indicators were detected."
            )

        # --------------------------------
        # Save Report for PDF
        # --------------------------------

        latest_report = {

            "result": result,

            "risk_score": risk_score,

            "threat_level": threat_level,

            "recommendations": recommendations

        }

    return render_template(

        "index.html",

        result=result,

        risk_score=risk_score,

        threat_level=threat_level,

        recommendations=recommendations

    )


# =====================================
# PDF Download Route
# =====================================

@app.route("/download-report")
def download_report():

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "Phishing Email Analysis Report",
            styles["Title"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph(
            f"<b>Analysis Result:</b> {latest_report.get('result','N/A')}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Threat Level:</b> {latest_report.get('threat_level','N/A')}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk Score:</b> {latest_report.get('risk_score',0)} / 100",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph(
            "<b>Security Recommendations</b>",
            styles["Heading2"]
        )
    )

    for item in latest_report.get("recommendations", []):

        story.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    response = make_response(pdf)

    response.headers["Content-Type"] = "application/pdf"

    response.headers["Content-Disposition"] = (
        "attachment; filename=Phishing_Email_Report.pdf"
    )

    return response


if __name__ == "__main__":

    app.run(debug=True)