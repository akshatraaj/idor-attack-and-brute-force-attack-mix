import requests

print("Since the link in the project one is not working, so I am using toy shop wala link.")
for i in range(1,5000):
    url=f"http://ec2-3-6-91-214.ap-south-1.compute.amazonaws.com/profile?id={i}"
    r=requests.get(url=url)
    if r.status_code==200:
        print(url)