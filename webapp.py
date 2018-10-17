from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('page1.html')

@app.route("/response")
def render_response():
    miles = float(request.args['miles'])
   
    return render_template('response.html', response =reply)


@app.route("/page2")
def render_response():
   # miles = float(request.args['miles'])
   
    return render_template('response.html', response =reply)

@app.route("/page3")
def render_response():
   # miles = float(request.args['miles'])
   
    return render_template('response.html', response =reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
    
    
    

