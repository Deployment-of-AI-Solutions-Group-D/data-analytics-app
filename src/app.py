from flask import Flask, render_template
import analysis
import os

app = Flask(__name__)
print("Template folder path:", os.path.join(os.getcwd(), 'templates'))

@app.route('/')
def index():
    print("Current Working Directory: ", os.getcwd())
    results = analysis.run_analysis()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
