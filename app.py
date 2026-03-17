from flask import Flask, render_template_string
import socket
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the hostname (Pod Name) and IP
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Simple HTML template to display info
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Flask App</title>
        <style>
            body { font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f4f4f4; }
            .card { background: white; padding: 20px; display: inline-block; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            h1 { color: #333; }
            .info { color: #007bff; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Flask App is Running!</h1>
            <p><strong>Status:</strong> <span style="color: green;">Deployment Successful</span></p>
            <p><strong>Pod Name (Hostname):</strong> <span class="info">{{ hostname }}</span></p>
            <p><strong>Pod IP Address:</strong> <span class="info">{{ ip_address }}</span></p>
            <hr>
            <p>Try refreshing to see if you hit a different Pod!</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, hostname=hostname, ip_address=ip_address)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    
# from flask import Flask
# import os

# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Saurabh says Hello world!!!"


# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
