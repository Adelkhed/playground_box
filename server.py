from flask import Flask, render_template
app =Flask(__name__)



@app.route('/play/')
def play():
    return render_template('index.html', number=3,color= "aqua")

@app.route('/play/<int:number>')
def play_number(number):
    return render_template('index.html', number=number,color= "aqua")

@app.route('/play/<int:number>/<string:color>')
def play_number_color(number,color):
    return render_template('index.html', number=number,color= color)

if __name__ == '__main__':
    app.run(debug=True)


