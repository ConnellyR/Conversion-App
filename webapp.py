from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_page1():
    return render_template('page1.html')
@app.route("/response1")
def render_response1():
    miles = float(request.args['miles'])
    response=miles * 63360
    return render_template('response.html', response =response)

@app.route("/page2")
def render_page2():
    return render_template('page2.html')
@app.route("/response2")
def render_response2():
    mass = float(request.args['mass'])
    response=mass * -9.8
    return render_template('response.html', response =response)

@app.route("/page3")
def render_page3():
    return render_template('page3.html')
@app.route("/response3")
def render_response3():
    pe = float(request.args['pe'])
    response=pe*441
    return render_template('page3.html')
    return render_template('response.html', response =response)

    
if __name__=="__main__":
    app.run(debug=False, port=54321)
    
    
    

