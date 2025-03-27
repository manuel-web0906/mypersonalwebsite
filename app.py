from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

links = [
    {"name": "Instagram", "url": "https://r.search.yahoo.com/_ylt=Awr4_zPd_ORnV8UBu4xXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1744269789/RO=10/RU=https%3a%2f%2fwww.instagram.com%2farsl_need.o2%2f/RK=2/RS=wbJwyazArNr28eorCXWEhkNewQ8-"},
    {"name": "Whatsapp", "url": "https://wa.me/628985816700"},
    {"name": "LinkedIn", "url": "https://id.linkedin.com/in/manuel-permana-putra-4168222aa"},
    {"name": "Gmail", "url": "https://mail.google.com/mail/u/0/?view=cm&tf=1&fs=1&to=manuelrg0906.putra@gmail.com"},
]

@app.route('/')
def home():
    return render_template('index.html', links=links, now=datetime.now())

if __name__ == 'main':
    app.run(debug=True)
