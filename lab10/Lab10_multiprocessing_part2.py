from urllib import request


def multiprocessing_images(link):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    request.urlretrieve(link, "downloads/{}.{}".format(filename, fileformat))