from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", grid=[('X', 'O', ' ', 'X')[i % 4] for i in range(9)])

@app.route("/api/mark", methods=['POST'])
def mark():
    print(f'marking {request.get_data(as_text=True)}')
    return jsonify({'message': 'Ok'})

if __name__ == "__main__":
    app.debug = True
    app.run()
