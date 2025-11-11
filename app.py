from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello():
    greeting_message = "Hello, This Python Flask app is being deployed using Github Actions and ArgoCD to EKS Cluster count=6"
    return render_template('index.html', message=greeting_message)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
