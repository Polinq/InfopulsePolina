import requests

def is_in_db(url, id):
    url = url
    id = id
    for i in [resp]:
        return("Yes" if i in [resp] else "No")



base_url = "http://pulse-rest-testing.herokuapp.com/books/"
p = requests.post(base_url, data = {"title": "Alice", "author": "writer"}) #Created an object
otvet = p.json()
d = otvet["id"]
st = p.status_code
print("Status code 1: ", p, "Id: ", d)

p1 = requests.get(base_url + str(d)) #Check that the object has been created
otvet1 = p1.status_code
print("Status code 2: ", otvet1)

req = requests.get(base_url) #Check thet the object is in the whole list of roles
resp = req.json()
t = is_in_db(resp, d)
print(t)

new_url = base_url + str(d)
reqw = requests.put(new_url, data = {"title": "Portrait of Dorian Grey", "author": "O.Henry"}) #Change the object
stats = reqw.status_code
print("Status code 3: ", p1)


print("ID: ", d)
rwst = requests.get(base_url + str(d)) #Check that the changed object has been created
s4 = rwst.status_code
#print(rwst.url)
print("Status code 4: ", s4)

r3 = requests.get(base_url) #Check thet the object is in the whole list of roles
resp = r3.json()
w = is_in_db(resp, d)
print(w)

d = otvet["id"]
print("ID: ",d)
reqwsts = requests.delete('http://pulse-rest-testing.herokuapp.com/books/' + str(d)) #delete the object
s9 = reqwsts.status_code
print("Response: ", s9)


r4 = requests.get(base_url) #Check thet the object IS NOT in the whole list of roles
resp = r4.json()

f = is_in_db(resp, d)
print(f)



