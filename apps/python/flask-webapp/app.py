from flask import Flask
import socket, os

app = Flask(__name__)

@app.route("/")
def hello_world():
    bg_color = os.environ.get('BG_COLOR', 'white')
    font_color = os.environ.get('FONT_COLOR', 'black')
    custom_header = os.environ.get('CUSTOM_HEADER', 'Welcome!')
    custom_photo = os.environ.get('CUSTOM_PHOTO', '')
    hostname = socket.gethostname()

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>DevOps Arena</title>
        <style>
            body {{
                background-color: {bg_color};
                color: {font_color};
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }}
            h1 {{
                font-size: 2.5em;
                margin-bottom: 20px;
            }}
            img {{
                max-width: 400px;
                height: auto;
                margin: 20px 0;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}
            h2 {{
                margin-top: 30px;
                font-size: 1.5em;
            }}
        </style>
    </head>
    <body>
        <h1>{custom_header}</h1>
        <img src="{custom_photo}" alt="Customer Photo">
        <h2>Hello World! Served from <b>{hostname}</b></h2>
    </body>
    </html>
    """
    return html
