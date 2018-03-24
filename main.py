from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
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
        <form action="/encrypt" method="post">
        <label for="rot">
            Rotate By:
            <input type="text" id="rot" name="rot" value="0"/>
        </label>
        <br>
        <br>

        <input type="textarea" id="text" name="text"/>

        <br>
        <br>
        <input type="submit" value="Submit Query"/>

    </form>     


    </body>
</html>

"""

@app.route("/")
def index():
    #return "Hello World"
    return form 
    
@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot_num = int(request.form['rot'])
    form_text = request.form['text']
    convert_string = rotate_string(form_text, rot_num)

    return "<h1>" + convert_string + "</h1>"


app.run()