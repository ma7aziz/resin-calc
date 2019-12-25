from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        volume = int(request.form['volume'])
        epoxy = ((volume * 100) / 140)
        hardner = volume - epoxy 
        return render_template('index.html', volume=round(volume), epoxy=round(epoxy), hardner=round(hardner))

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()