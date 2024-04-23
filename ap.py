from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/')
def teste1 ():
    return render_template('aulamvc.html')

@app.route('/gravar', methods=['POST'])
def teste2 ():
    nomerec= request.form['nome']
    emailrec = request.form['email']
    senharec = request.form['senha']
    print(nomerec)
    print(emailrec)
    print(senharec)
    return render_template('aulamvc.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)