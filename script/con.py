import sys
import base64
import requests
import os

name = None
if len(sys.argv) > 1:
    name = sys.argv[1]

def main():
    if name:
        with open( name , 'rb') as pic:
            # data = pic.read()
            res = requests.post('http://localhost:6969/read', files = {
                'pic' : pic
            })

            print( res , res.json())
            print( res.json()["_med_info"] )
        return

    for file in os.listdir('./images'):
        with open('./images/'+ file , 'rb') as pic:
            # data = pic.read()
            res = requests.post('http://localhost:6969/read', files = {
                'pic' : pic
            })
            print('======================')
            # print( res , res.json())
            print( res.json()["_med_info"],f"filename : {file}" )
            print('======================')


main()