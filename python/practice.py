def bubble(liist):
    n = len(liist)
    for i in range(n):
        for j in range(0, n-i-1):
            if liist[j] > liist[j+1]:
                liist[j], liist[j+1] = liist[j+1], liist[j]
    return liist
lst = [5,9,7,6,1,2,4,3,8,0]
print(bubble(lst))