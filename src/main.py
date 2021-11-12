import time
from services.number_classifier import NumberClassifier


def main():
    start_time = time.time()
    nc = NumberClassifier()  # pylint: disable=invalid-name
    # nc.train()
    nc.sandbox()
    print("--- %s seconds ---" % (time.time() - start_time))


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
