from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__);
app.secret_key = "NGcourses2023";


namePasswordDictionary = {};
messages = [];

# function which needs an input of username and password,
# returns two bool values, if the password is wrong and
# if username is wrong in form.
def emptyFormCheck(username, password):
    wrongPassword = False;
    wrongUsername = False;
    if password == "":
        wrongPassword = True;
    if username == "":
        wrongUsername = True;
    return [wrongPassword, wrongUsername];

# page with two redirecting buttons - "login" and "register"
@app.route('/', methods=["POST", "GET"])
def mainPage():
    if request.method == "POST":
        if request.form.get('login'):
            return redirect("login");
        else:
            return redirect("register");
    else:
        return render_template("index.html");

# page of the chat, with url being a name of account
@app.route('/<name>/', methods=["POST","GET"])
def chat(name):
    if request.method == "POST" and session.get("name") == name:
        if request.form.get("chatbutton"):
            messages.append(name+ ": " + request.form.get('textbox'));
            if len(messages)>=18:
                messages.pop(0);
            return render_template("chat.html", chat=messages); 
        elif request.form.get("logout"):
            session["name"] = None;
            return redirect(url_for("mainPage"));
    elif session.get("name") == name:
        return render_template("chat.html", chat=messages);    
    else:
        return redirect(url_for("mainPage"));

# page where people can login to (only)existing accounts
@app.route('/login/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username');
        password = request.form.get('password');
        wrongData = True;
        nonExistantUser = not(username in namePasswordDictionary); 
        if not nonExistantUser:
            if namePasswordDictionary[username] == password:
                wrongData = False;
        wrongs = emptyFormCheck(username, password);
        if not nonExistantUser and not wrongs[0] and not wrongs[1] and not wrongData:
            session["name"] = request.form.get("username");
            return redirect(url_for("chat", name=username));
        return render_template("login.html", wrongPassword=wrongs[0], wrongUsername=wrongs[1],
                                             wrongData=wrongData, nonExistantUser=nonExistantUser);
    else:
        return render_template("login.html");

# page where people can make (only)new accounts
@app.route('/register/', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get('username');
        password = request.form.get('password');
        wrongs = emptyFormCheck(username, password);
        alreadyInUse = False;
        if username in namePasswordDictionary:
            alreadyInUse = True;
        if not wrongs[0] and not wrongs[1] and not alreadyInUse:
            namePasswordDictionary[username] = password;
            session["name"] = request.form.get("username");
            return redirect(url_for("chat", name=username))
        return render_template("register.html", wrongPassword=wrongs[0], 
                               wrongUsername=wrongs[1], alreadyInUse=alreadyInUse);
    else:
        return render_template("register.html");

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081);