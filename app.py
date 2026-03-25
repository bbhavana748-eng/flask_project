from flask import Flask, jsonify, request, redirect, url_for, render_template

app = Flask(__name__)

# API route (NO file reading now → no error)
@app.route('/api')
def get_data():
    data = [
        {"name": "John", "email": "john@example.com"},
        {"name": "Alice", "email": "alice@example.com"}
    ]
    return jsonify(data)

# Form route
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return redirect(url_for('success'))
    return render_template('form.html')

# Success route
@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run()
