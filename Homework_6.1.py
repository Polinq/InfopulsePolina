import requests

def is_in_db(url, id):
    url = url
    id = id
    for i in [resp]:
        return("Yes" if i in [resp] else "No")

url = "http://pulse-rest-testing.herokuapp.com/roles/"
r = requests.post(url, data = {"name": "Harry_Potter", "type": "Wizard", "level": "14", "book": "2"}) #Created an object
response = r.json()
i = response["id"]
s = r.status_code
print("Status code 1: ", s, "Id: ", i)

r1 = requests.get(url + str(i)) #Check that the object has been created
s1 = r1.status_code
print("Status code 2: ", s1)

req = requests.get(url) #Check thet the object is in the whole list of roles
resp = req.json()
w = is_in_db(resp, i)
print(w)

new_url = url + str(i)
reqw = requests.put(new_url, data = {"name": "Hermiona", "type": "Witch", "level": "13", "book": "7"}) #Change the object
stats = reqw.status_code
print("Status code 3: ", s1)


print("ID: ", i)
rwst = requests.get(url + str(i)) #Check that the changed object has been created
s4 = rwst.status_code
#print(rwst.url)
print("Status code 4: ", s4)

r3 = requests.get(url) #Check thet the object is in the whole list of roles
resp = r3.json()
o = is_in_db(resp, i)
print(o)

i = response["id"]
print("ID: ",i)
reqwsts = requests.delete('http://pulse-rest-testing.herokuapp.com/roles/' + str(i)) #delete the object
s9 = reqwsts.status_code
print("Response 1: ", s9)


r4 = requests.get(url) #Check thet the object IS NOT in the whole list of roles
resp = r4.json()
l = is_in_db(resp, i)
print(l)
