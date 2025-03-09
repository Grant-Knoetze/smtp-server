app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_server():
    start_smtp_server()
    return "SMTP server started!"

@app.route('/stop', methods=['POST'])
def stop_server():
    stop_smtp_server()
    return "SMTP server stopped."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)