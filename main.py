from flask import Flask, request
import cgi
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
  <html>
    <head>
      <title> Web Caesar </title>
      <style>
      body {background-color:rgba(165,96,235,0.5);}
       form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
      </style>
    </head>
    <body>
"""


page_footer = """
    </body>
</html>
"""

#the main body of the form
form = """
    <form method="post">
        <label>
            <h3>Rotate by: 
            <input type="text" name="rot" value="0" />
            </h3>
        </label>
        <textarea cols ="60" rows="5" name="text">
        {0}
        </textarea>
        <br>
        <input type="submit">
        
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    rot = int(rot)

    new_text = rotate_string(text, rot)

    content = page_header + '<h1>' + form.format(new_text) + '</h1>' + page_footer

    return content


@app.route("/")
def index():
    text = ''
    content = page_header + form.format(text) + page_footer

    return content



app.run()