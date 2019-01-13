from flask import Flask, render_template, request
import re
 
app = Flask(__name__)
 
 
def count_sentences(text):
 
    sentences = re.findall(r'[a-z0-9\\’\\\']+', text.lower())
 
    return len(sentences)

def count_words(text):
    words = re.findall(r'[^\t\n\r\f\v]',text.lower())
    return len(words)


 
 
@app.route('/', methods=['POST', 'GET'])
def home():
 
    total = ''
 
    if request.method == 'POST':
        text = request.form['text']
        total_sentences = count_sentences(text)
        total_words = count_words(text)
 
        return render_template('main.html', total_sentences=total_sentences,total_words=total_words,input_words=text)

    return render_template('main.html', total_sentences=total_sentences)
 
 
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
