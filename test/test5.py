import urllib3
resp = urllib3.request(
    "POST",
    "https://httpbin.org/post",
    fields={"field": "value"}
)

print(resp.json()["form"])