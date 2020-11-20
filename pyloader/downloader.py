import requests
from klondbar.microbar import micro_bar


def extract_file_name(url):
    return url.split('/')[-1].replace('%', ' ')


def download(url, chunk_size=1024):
    file_name = extract_file_name(url)
    response = requests.get(url, stream=True, allow_redirects=True)
    total_size = int(response.headers.get('content-length'))
    iterations = total_size//chunk_size + 1
    content = []
    for i in micro_bar(response.iter_content(chunk_size),
                       title=f'Downloading "{file_name[:20]}"',
                       iterations_number=iterations):                           
            if i:
                content.append(i)
    return b''.join(content)




if __name__ == '__main__':
    url = r'https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_10mb.mp4'
    content = download(url)
    path = f'test/{extract_file_name(url)}'
    with open(path, mode='wb') as file:
        file.write(content)
