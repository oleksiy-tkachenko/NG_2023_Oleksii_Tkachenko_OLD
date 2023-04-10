import requests
linkList = input("Input your links with spaces between them:\n").split()
for link in linkList:
    linkStatusCode = requests.request("GET", link).status_code
    if (linkStatusCode==200 or linkStatusCode==302):
        print("OK")
    else:
        print("FAIL")