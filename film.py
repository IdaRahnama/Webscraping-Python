ho = 0
r = 0
c = 0
hi = 0
ad = 0
ac = 0
m = int(input())
for i in range(m):
    n = input()
    genre_array = n.split()
    for j in range(1, 4, 1):
        if genre_array[j] == 'Horror':
            ho += 1
        elif genre_array[j] == 'Romance':
            r += 1
        elif genre_array[j] == 'Comedy':
            c += 1
        elif genre_array[j] == 'History':
            hi += 1
        elif genre_array[j] == 'Adventure':
            ad += 1
        elif genre_array[j] == 'Action':
            ac += 1
print('Action : {}'.format(ac))
print('Comedy : {}'.format(c))
print('History : {}'.format(hi))
print('Horror : {}'.format(ho))
print('Romance : {}'.format(r))
print('Adventure : {}'.format(ad))