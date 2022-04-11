from collections import Counter
from sklearn.cluster import KMeans, OPTICS
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
import hdbscan
import operator

def extractColorPaletteFromImg(img_src):

    image = cv2.imread(img_src)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # print("image:", image)

    print("img shape:", image.shape)

    # resize image to smaller to contain less pixels:
    image = cv2.resize(image, (image.shape[1]//4, image.shape[0]//4), interpolation = cv2.INTER_AREA)                                          
    plt.imshow(image)
    plt.show()

    
    pixels_flattened = image.reshape((image.shape[0]*image.shape[1], 3))

    # pixels_flattened = image.flatten()
    print("pixels_flattened:", pixels_flattened)

    # counts = Counter(pixels_flattened)
    # counts = Counter([[1, 2, 3], [1, 2, 3], [1, 4]])
    # values, counts = np.unique(pixels_flattened, return_counts=True)
    values, counts = np.unique(np.array([[1, 2, 3], [1, 2, 3], [1, 4,4]]), return_counts=True)
    print("counts:", counts)
    print("values:", values)


    unique_pixel_values = [list(x) for x in set(tuple(x) for x in pixels_flattened)]
    print("unique_data:", unique_pixel_values)

    count_vals = {}


    for pixel in pixels_flattened:
        count_vals[str(list(pixel))]  = count_vals.get(str(list(pixel)), 0)+1


    print("cnt vals:", count_vals)

    # sorted_d = dict( sorted(count_vals.items(), key=operator.itemgetter(1),reverse=True))
    # print('Dictionary in descending order by value : ',sorted_d)

    a = sorted(count_vals.items(), key=lambda x: x[1], reverse=True)    
    print("a sorted:", a)
    
    most_encountered_color = a[0][0]
    nr_px_most_color = a[0][1]

    
    print("most_encountered color:", most_encountered_color )
    print("hex:", rgb_to_hex(eval(most_encountered_color)))
    print("nr pixels most color:", nr_px_most_color)

    print("first 5 colors:")
    i = 1

    most_popular_colors = []
    while a[i][1]==nr_px_most_color:
        print(rgb_to_hex(eval(a[i][0])))
        i+=1
        most_popular_colors.append(eval(a[i][0]))

    print("most popular colors:", most_popular_colors)






    # modified_image = preprocess(image)
    # analyze(modified_image)



def extractColorsFromImg(img_src):
    pass


def preprocess(raw):
    # image = cv2.resize(raw, (900, 600), interpolation = cv2.INTER_AREA)                                          
    image = raw
    image = image.reshape((image.shape[0]*image.shape[1], 3))
    plt.imshow(image)
    plt.show()
    return image

def analyze(img):
    clf = KMeans(n_clusters = 5)
    # clf = OPTICS()
    # clusterer = hdbscan.HDBSCAN()

    # clusterer.fit(img)

    color_labels = clf.fit_predict(img)
    # color_labels = clusterer.labels_

    print("color labels:", color_labels)


    center_colors = clf.cluster_centers_
    # center_colors = clusterer.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

    plt.figure(figsize = (12, 8))
    plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
    plt.show()
    # plt.savefig("my_pie.png")
    print("Found the following colors:\n")
    for color in hex_colors:
      print(color)
      

def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        hex_color += ("{:02x}".format(int(i)))
    return hex_color

img_src = "uploads/30-40-fantasy3-1-247x296.jpg"
color_palette = extractColorPaletteFromImg(img_src)
print("color palette:", color_palette)