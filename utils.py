def save_file(filename, data, folder=None):

    if folder!=None:
        if folder[-1]!="/":
            folder +="/"
        filename = folder + filename

    print("filename:", filename)

    with open(filename, 'wb') as f:
        f.write(data)