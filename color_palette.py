from collections import Counter
from math import dist
from sklearn.cluster import KMeans, OPTICS
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
# import hdbscan
import operator

from sklearn.cluster import SpectralClustering
from sklearn.metrics.pairwise import euclidean_distances


import matplotlib.pyplot as plt
import numpy as np



def extractColorPaletteFromImg(img_src):

    image = cv2.imread(img_src)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # print("image:", image)

    # print("img shape:", image.shape)

    # resize image to smaller to contain less pixels:
    image = cv2.resize(image, (image.shape[1]//10, image.shape[0]//10), interpolation = cv2.INTER_AREA)                                          
    # plt.imshow(image)
    # plt.show()

    
    pixels_flattened = image.reshape((image.shape[0]*image.shape[1], 3))

    # # pixels_flattened = image.flatten()
    # print("pixels_flattened:", pixels_flattened)

    # # counts = Counter(pixels_flattened)
    # # counts = Counter([[1, 2, 3], [1, 2, 3], [1, 4]])
    # # values, counts = np.unique(pixels_flattened, return_counts=True)
    # values, counts = np.unique(np.array([[1, 2, 3], [1, 2, 3], [1, 4,4]]), return_counts=True)
    # print("counts:", counts)
    # print("values:", values)


    # unique_pixel_values = [list(x) for x in set(tuple(x) for x in pixels_flattened)]
    # print("unique_data:", unique_pixel_values)

    # count_vals = {}


    # for pixel in pixels_flattened:
    #     count_vals[str(list(pixel))]  = count_vals.get(str(list(pixel)), 0)+1


    # print("cnt vals:", count_vals)

    # # sorted_d = dict( sorted(count_vals.items(), key=operator.itemgetter(1),reverse=True))
    # # print('Dictionary in descending order by value : ',sorted_d)

    # a = sorted(count_vals.items(), key=lambda x: x[1], reverse=True)    
    # print("a sorted:", a)
    
    # most_encountered_color = eval(a[0][0])
    # nr_px_most_color = a[0][1]

    
    # print("most_encountered color:", most_encountered_color )
    # print("hex:", rgb_to_hex(most_encountered_color))
    # print("nr pixels most color:", nr_px_most_color)

    # print("first 5 colors:")
    # i = 1

    # most_popular_colors = []

    # most_popular_colors = pixels_flattened

    # while a[i][1]==nr_px_most_color:
    #     print(rgb_to_hex(eval(a[i][0])))
    #     i+=1
    #     most_popular_colors.append(eval(a[i][0]))

    # print("most popular colors:", most_popular_colors)


    # # most_popular_colors = [[1, 2, 1], [3, 4, 1], [3, 4, 1], [3, 4, 1]]
    # dist_matrix = euclidean_distances([most_encountered_color], most_popular_colors)
    # print("distance matrix:", dist_matrix)
    # # argmax_idx = np.argmax(dist_matrix)
    # argmax_idx = np.unravel_index(dist_matrix.argmax(), dist_matrix.shape)
    # print("argmax_idx:", argmax_idx)
    # print("biggest_distance:", dist_matrix[argmax_idx[0]][argmax_idx[1]])
    # biggest_dist_color = most_popular_colors[argmax_idx[1]]
    # print("color with biggest_distance:", biggest_dist_color)
    # print("hex:", rgb_to_hex(biggest_dist_color))

    # display 3D plot of colors:    
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')

    # # for color in most_popular_colors:
    # for color in pixels_flattened:
    #     r, g, b = color
    #     ax.scatter(r, g, b, color=rgb_to_hex(color))

    # plt.show()




    hex_colors = analyze(pixels_flattened)
    return hex_colors
    # for color in hex_colors:
    #   print(color)



    # modified_image = preprocess(image)
    # analyze(modified_image)




# def extractColorPaletteFromImg2(img_src, color_wheel_src='color_wheel1.png'):

#     image = cv2.imread(img_src)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


#     image = cv2.resize(image, (image.shape[1]//10, image.shape[0]//10), interpolation = cv2.INTER_AREA)                                          
#     plt.imshow(image)
#     plt.show()

#     color_wheel = cv2.imread(color_wheel_src)
#     color_wheel = cv2.cvtColor(color_wheel, cv2.COLOR_BGR2RGB)

#     color_wheel = cv2.resize(color_wheel, (color_wheel.shape[1]//10, color_wheel.shape[0]//10), interpolation = cv2.INTER_AREA)                                          

#     plt.imshow(color_wheel)
#     plt.show()

#     width, height = color_wheel.shape[1], color_wheel.shape[0]

#     pixels_flattened = image.reshape((image.shape[0]*image.shape[1], 3))

#     plt.imshow(color_wheel)
#     for i in range(height):
#         for j in range(width):
#             for pixel in pixels_flattened:
#                 if np.array_equal(color_wheel[i][j], pixel):
#                     print(pixel)
#                     plt.plot(i, j, marker="X")

#     plt.show()
    

def extractColorsFromImg(img_src):
    pass


def preprocess(raw):
    # image = cv2.resize(raw, (900, 600), interpolation = cv2.INTER_AREA)                                          
    image = raw
    image = image.reshape((image.shape[0]*image.shape[1], 3))
    plt.imshow(image)
    plt.show()
    return image

def analyze(img, visualize=False):
    clf = KMeans(n_clusters = 5)
    # clf = OPTICS()
    # clusterer = hdbscan.HDBSCAN()

    # clusterer.fit(img)

    color_labels = clf.fit_predict(img)
    # color_labels = clusterer.labels_

    # print("color labels:", color_labels)


    center_colors = clf.cluster_centers_
    # center_colors = clusterer.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

    if visualize:
        plt.figure(figsize = (12, 8))
        plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
        plt.show()
        # plt.savefig("my_pie.png")
    # print("Found the following colors:\n")

    return hex_colors  

def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        hex_color += ("{:02x}".format(int(i)))
    return hex_color


if __name__=="__main__":
    img_src = "uploads/30-40-fantasy3-1-247x296.jpg"
    color_palette = extractColorPaletteFromImg(img_src)
    # color_palette = extractColorPaletteFromImg2(img_src)

    print("color palette:", color_palette)