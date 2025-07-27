import random
import re
import requests
import sys
import time

url = 'https://caliroots.typeform.com/to/HjsMiy'


def main(limit):
    for i in range(0, limit):
        payload = {
            'form[email:Fi1mS3bZn3VF]': 'youremail@gmail.com',
            'form[list:56641463][choices]': sizes[random.randint(0, 11)],  # don't change
            'form[landed_at]': '1500901708',  # don't change
            'form[language]': 'en',  # don't change
            'form[terms:QS4P6gmSVp8s]': '1',  # don't change
            'form[textfield:Boa0BNN75u6R]': 'Amsterdam',  # change to ur city
            'form[textfield:EKZm78mYLBbE]': 'streetname 1',  # change to ur street name + number
            'form[textfield:IIdtgeMwp8Gp]': list1[random.randint(0, 99)],  # DO NOT CHANGE !
            'form[textfield:MQfwQiem4TEw]': '20906',  # change to ur zip code
            'form[textfield:bHSS1rapvhha]': list1[random.randint(0, 99)],  # DO NOT CHANGE
            'form[textfield:n3yXjbpstFmJ]': 'MD',
        }
        resp = requests.post(url, data=payload)
        if any(re.findall(r'thank', str(resp.text), re.IGNORECASE)):
            print(time.strftime("%H:%M:%S") + " / Successfully entered!")
        else:
            print(time.strftime("%H:%M:%S") + " / Could not enter!")


main(100)  # change to the amount u want, currently 100 times.
exit()
