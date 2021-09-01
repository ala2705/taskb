url = "https://stackoverfdddlow2d.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given"
url_length = len(url)

url_sum = 0
for i in range(url_length):
    url_sum += ord(url[i])
print(url_sum)

n = 2
chunks = [url[i:i+n] for i in range(0, len(url), n)]
print(chunks)
print(len(chunks))
a = len(chunks)%4
print(a)
b = len(chunks)/2
print(int(b))
