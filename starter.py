from pkg import app

# app.config.from_pyfile('config.py')



if __name__=='__main__':
    app.config.from_pyfile('config.py')
    app.run(debug=True)