import pymongo

client = pymongo.MongoClient("mongodb://jaisingh:jaisingh%40123@cluster0-shard-00-00-ht9pp.mongodb.net:27017,cluster0-shard-00-01-ht9pp.mongodb.net:27017,cluster0-shard-00-02-ht9pp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb=client.employee

def add_students(name,age,rollno,branch):
     mydb.employees.insert_one(
            {
            "nane" : name,
            "age" : age,
            "rollno" : rollno,
            "branch" : branch
            })
     return "Employee added successfully"

def fetch_all_employee():
    user = mydb.employees.find()
    for i in user:
        print (i)

add_students("abc","19","123","cse")
add_students("def",19,124,"cse")
add_students("ghi",19,125,"cse")
add_students("jkl",19,126,"cse")
add_students("mno",19,127,"cse")


fetch_all_employee()