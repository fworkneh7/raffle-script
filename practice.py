import requests

res = requests.get('https://shop.travisscott.com/')
# res = requests.get('http://www.baitme.com/nike-travis-scott-air-max-270-cactus-trails') can access
# res = requests.get('https://releases.ubiqlife.com/raffle/travisscott270_may29.html') cant access
# res = requests.get('https://wishatl.us12.list-manage.com/subscribe?u=461bee073ad7d85d29419cd92&id=b0e6eb971a')

print(res.headers)
print(res.status_code)
print(res.encoding)