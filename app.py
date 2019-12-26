from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        volume = int(request.form['volume'])
        ratio_a = int(request.form['ratio_a'])
        ratio_b = int(request.form['ratio_b'])
        ## epoxy == (volume * ratio a)/(ratioa + ratio b)
        epoxy = ((volume * ratio_a) / (ratio_a + ratio_b))
        hardner = volume - epoxy

        return render_template('index.html', volume=round(volume), epoxy=round(epoxy), hardner=round(hardner), ratio_a=round(ratio_a), ratio_b= round(ratio_b))

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()