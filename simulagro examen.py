# n 
# d 
# m


# ¿n % 3664 == 0?
# ¿(n × d) % 2 == 0?
# ¿m % 2 == 0?

n = 5
m =5
d =5



def isTrue(n , m,d):
    nd = n *d
    cond1  = n / 3664
    cond2 = n*d
    cond3 = m


    return (n % 3664 == 0) and ((n * d) % 2 == 0) and (m % 2 == 0)


print(isTrue(7328,2,8))