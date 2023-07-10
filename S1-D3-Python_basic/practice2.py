employes= [
    {"name":"akash", "salary":30000, "designation":"developer"},
    {"name":"aman", "salary":40000, "designation":"developer"},
    {"name":"anuj", "salary":20000, "designation":"developer"},
    {"name":"aadarsh", "salary":10000, "designation":"developer"}
]

max=0
res={}

for employe in employes:
    if(employe["salary"]>max):
        max=employe["salary"]
        res=employe


print(res) 
