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
    url = r'https://github.com/dariush-bahrami/Number-Recognition-Application/raw/master/trained_models/MNIST%20-%20Convolutional%20-%20SGD%20-%20Loss%200_0218%20-%20Acc%200_9927.h5'
    content = download(url)
    path = extract_file_name(url)
    with open(path, mode='wb') as file:
        file.write(content)
