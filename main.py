from flask import Flask, render_template, redirect, flash
app = Flask('app')

app.config['SECRET_KEY'] = 'HAglkjlttjglfA'

@app.route('/')
def index():
  return redirect('/flashing')

@app.route('/flashing')
def flashing():
  flash('Sucesso', 'success')
  return render_template('flashing.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)