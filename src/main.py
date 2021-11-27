#import time
#from services.knn import knn
from ui.ui import UI


def main():
    # start_time = time.time()
    # knn.classify_number(3, 1, 60_000, "D22")
    # end_1 = time.time()
    # print(f"--- {(end_1 - start_time)} seconds ---")
    # knn.classify_number(3, 1, 1000, "D22")
    # end_2 = time.time()
    # print(f"--- {(end_2 - end_1)} seconds ---")
    # knn.classify_number(3, 1, 10_000, "D22")
    # end_3 = time.time()
    # print(f"--- {(end_3 - end_2)} seconds ---")

    ui = UI()
    ui.start()


if __name__ == "__main__":
    main()

# import gzip
# f = gzip.open('./data/train-images-idx3-ubyte.gz','r')

# image_size = 28
# num_images = 5

# import numpy as np
# f.read(16)
# buf = f.read(image_size * image_size * num_images)
# data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
# data = data.reshape(num_images, image_size, image_size, 1)

# import matplotlib.pyplot as plt
# image = np.asarray(data[2]).squeeze()
# plt.imshow(image)
# plt.show()
