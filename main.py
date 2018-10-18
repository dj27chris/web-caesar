from flask import Flask, request
import cgi

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
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
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
    <form action="/cypher" method="post">
        <label>
            <h3>Rotate by: 
            <input type="text" name="rot" value="0" />
            </h3>
        </label>
        <textarea cols ="30" rows="5" name="text">
        </textarea>
        
"""


@app.route("/")
def index():
    return page_header + form + page_footer



app.run()