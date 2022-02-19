from this import d
from urllib.request import Request, urlopen
import json
from time import sleep

current_round = 1649757
fin_nums = ""

for j in range(100):

 def get_numbers(): 
  req = Request('https://drand.cloudflare.com/public/' + str(current_round) , headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
  html = urlopen(req).read()
  import json
  html=html.decode()
  d=json.loads(html)
  return(d["randomness"])

 cur_nums = get_numbers()
 
 fin_nums = fin_nums + cur_nums

 current_round = current_round - 1

res = ''.join(format(i, '08b') for i in bytearray(fin_nums, encoding ='utf-8'))

#print(str(res))

def max_consecutive_0(input_str): 
     return  max(map(len,input_str.split('1')))

def max_consecutive_1(input_str): 
     return  max(map(len,input_str.split('0')))

print("Maximum length of consecutive 0’s:")
print(max_consecutive_0(res))

print("Maximum length of consecutive 1’s:")
print(max_consecutive_1(res))