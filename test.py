import requests
import os

def get_pic_by_url(lists):
    output_path = './output'
    for url in lists:
        filename = output_path + '/' + url.split('/')[-1]
        if os.path.exists(filename):
            print('File have already exist.')
            continue
        try:
            r = requests.get(url,timeout=5)
        except requests.exceptions.RequestException as e:
            print(e)
            continue
        with open(filename,'wb') as f:
            f.write(r.content)

if __name__ == "__main__":
    file_path = './urllist.txt'
    with open(file_path, 'r') as f:
        lines = f.readlines()
        url_list = []
        for line in lines:
            url_list.append(line.strip('\n'))
    
    get_pic_by_url(url_list)
