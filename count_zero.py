num=12009002003
count=0
def countzero(num):
    global count
    if num<10:
        return
    remain=num%10
    if remain==0:
        count+=1
    return countzero(num//10)
countzero(num)
print(count)    