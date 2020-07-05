import time

i=0

while i < 4:
    time.sleep(60*15)
    print ('Take a short break')
    i+=1
if i is 3:
    print ('You should take a long braek')
    print ('You spent alot of time working give yourself a break :)')
    time.sleep(60*10)
