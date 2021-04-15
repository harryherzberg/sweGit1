def devise(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i)
            i+=1

forced = input("give number for devisors:   ")

forced = int(forced)
print ("devisors for "+ str(forced)+" : ")
devise(forced)
