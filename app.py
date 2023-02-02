from flask import Flask, render_template,request,json
from pymongo import MongoClient

app=Flask("__name__")

client=MongoClient("mongodb://127.0.0.1:27017")

@app.route("/",methods=["post","get"])
def form_data():
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        mobile=request.form.get("mobile")

        database=client.students
        collection=database.stu
        collection.insert_one({
        "id":id,
        "name":name,
        "mobile":mobile
        })
        client.close()

        return "<h1>successfully inserted</h1>"
    return render_template("index.html")


@app.route("/api",methods=["post","get"])
def postman_data():
    l=request.json
    database=client.students
    collection=database.stu
    for i in l:
        collection.insert_one(i)
    client.close()

    return "successfully inserted"

if __name__=="__main__":
    app.run(debug=True)