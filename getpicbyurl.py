import requests
import os

def get_pic_by_url(lists):
    output_path = './output'
    for url in lists:
        filename = url.split('/')[-1]
        filepath = output_path + '/' + filename
        if os.path.exists(filepath):
            print(filename + ' - File has already existed.')
            continue
        try:
            r = requests.get(url) # timeout=10
        except requests.exceptions.RequestException as e:
            print(filename,end='')
            print(e)
            continue
        with open(filepath,'wb') as f:
            print(filename + ' - File downloads successfully.')
            f.write(r.content)

if __name__ == "__main__":
    file_path = './urllist.txt'
    with open(file_path, 'r') as f:
        lines = f.readlines()
        url_list = []
        for line in lines:
            url_list.append(line.strip('\n'))
    
    get_pic_by_url(url_list)
