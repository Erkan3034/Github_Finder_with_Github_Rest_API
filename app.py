from flask import Flask, render_template, request
import requests 

app = Flask(__name__)


base_url = "https://api.github.com/users/" # Github API'sini kullanabilmek için base_url'i tanımladık

@app.route("/", methods=["GET", "POST"]) # GET ve POST isteklerini kabul etmemiz lazım
def index():
    if request.method == "POST":
        username = request.form["username"] # Formdan gelen username'i alıyoruz
        response = requests.get(base_url + username) # Github API'sini kullanarak username'e ait verileri alıyoruz
        if response.status_code == 200:
            user_data = response.json()
            return render_template("index.html", profile=user_data)
        else:
            return render_template("index.html", profile=None, error="User not found, please try again with a valid username!")
    else:
        return render_template("index.html", profile=None)










if __name__ == "__main__":
    app.run(debug=True)