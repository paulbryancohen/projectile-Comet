# Dictionaries - collection of key / value pairs
d = {'sekhar' : '999-999-9999', 'sue' : '111-111-1111' , 'chris' : '888-888-8888'}
print(d)
d['david'] = '222-222-2222'
print(d)
print(d['sekhar'])

for i in d:
    print(i, d[i])