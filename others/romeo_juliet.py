import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

res.status_code == requests.codes.ok
res.raise_for_status()
len(res.text)
print(res.text[:250])


play_file = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    play_file.write(chunk)

play_file.close()