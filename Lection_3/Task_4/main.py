import requests
linkList = input("Input your links with spaces between them:\n").split()
for link in linkList:
    try:
        linkStatusCode = requests.request("GET", link).status_code
    except:
        print("unknown error - FAIL")
    else:
        if (linkStatusCode==200 or linkStatusCode==302):
            print(f"{linkStatusCode} - OK")
        else:
            print(f"{linkStatusCode} - FAIL")