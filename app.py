from flask import Flask, render_template,request,json
from pymongo import MongoClient

app=Flask("__name__")

client=MongoClient("mongodb://127.0.0.1:27017")

@app.route("/",methods=["post","get"])
def fun():
    l=request.json
    database=client.students
    collection=database.stu
    for i in l:
        collection.insert_one({
        "id":i["id"],
        "name":i["name"],
        "mobile":i["mobile"]
        })
    print("inserted")
    client.close()

    return "successfully inserted"

if __name__=="__main__":
    app.run(debug=True)