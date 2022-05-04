import requests

for i in range(10, 11):
    url = f'https://placedata.reddit.com/data/canvas-history/' \
          f'2022_place_canvas_history-0000000000{i}.csv.gzip'
    
    print(f"Downloading {url}...")

    file_name = "./data/" + url.split('/')[-1]
    data = requests.get(url)

    with open(file_name, 'wb') as file:
        file.write(data.content)

print("Im done :)")