import hashlib
  
secret = "iwrupvqb"
count = 1
while True:
    x = secret + str(count)
    result = hashlib.md5(x.encode('utf-8')).hexdigest()[:5]
    if result == "00000":
        print(count)
        break
    count += 1