import requests as rq
from flask import jsonify
import time as T
import random



def main():

    while True:

        page = rq.get('http://192.168.0.133:5000/api/v1/sensors/obstacles')
        
        for sens in page.json():
            print(f"{sens}: {page.json()[sens]}")
    
        right = page.json()['right']
        left = page.json()['left']
        if right == 0 and left == 0:
            if ran==2: 
                ran = random.choice([0, 1])

            if ran == 0:
                pwml = 50
                pwmr = 0
                time = 300

            else:
                pwml = 0
                pwmr = 45
                time = 250
            
        elif right == 0:
            pwml = 0
            pwmr = 45
            time = 250
            ran=2

        elif left == 0:
            pwml = 50
            pwmr = 0
            time = 300
            ran=2
        
        else:
            pwml = 50
            pwmr = 45
            time = 250
            ran=2

        page2 = rq.get(f'http://192.168.0.133:5000/api/v1/motors/both?pwmL={pwml}&pwmR={pwmr}&time={time}')
        T.sleep(0.1)

        




if __name__ == "__main__":
    main()