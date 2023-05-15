import os
import requests
from dotenv import load_dotenv
import jinja2

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")
template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)


def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)


def send_simple_message(to, subject, body, html):
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": f"ranjith<mailgun@{DOMAIN}>",
            "to": [to],
            "subject": subject,
            "text": body,
            "html": html,
        }
    )


def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the Stores REST API.",
        render_template("email/action.html", username=username)
    )
    
# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/sandboxf74c71929e9c4027901805b4d610fb8e.mailgun.org/messages",
# 		auth=("api", "1105a63947a6e7d2b9dd7bd3686bc5ff-db4df449-d6a3d8c7"),
# 		data={"from": "Mailgun Sandbox <postmaster@sandboxf74c71929e9c4027901805b4d610fb8e.mailgun.org>",
# 			"to": "ranjith <ranjithusvn@gmail.com>",
# 			"subject": "Hello ranjith",
# 			"text": "Congratulations ranjith, you just sent an email with Mailgun!  You are truly awesome!"})

# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10000 emails/month for free.