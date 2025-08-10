def extensions():
    extension=input('File name:').strip()
    if extension.lower().endswith('.gif'):
        print('image/gif')
    elif extension.lower().endswith('.jpg') or extension.lower().endswith('.jpeg'):
        print('image/jpeg')
    elif extension.lower().endswith('.png'):
        print('image/png')
    elif extension.lower().endswith('.pdf'):
        print('application/pdf')
    elif extension.lower().endswith('.txt'):
        print('text/plain')
    elif extension.lower().endswith('.zip'):
        print('application/zip')
    elif extension.lower().endswith('') or extension.lower().endswith('.bin'):
        print('application/octet-stream')
extensions()
