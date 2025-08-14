from flask import Flask, request

app = Flask(__name__)

# Simple form to accept user input
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        comment = request.form['comment']
        # ❌ XSS vulnerability: user input is directly injected into the HTML
        return f"<h2>Your Comment:</h2><p>{comment}</p><a href='/'>Back</a>"
    
    # Basic HTML form
    return '''
        <form method="POST">
            Enter your comment: <br>
            <textarea name="comment"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
