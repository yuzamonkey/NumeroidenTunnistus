from mnist import MNIST


class MNISTGETTER():
    def __init__(self):
        self._mndata = MNIST("./data")
        self._mndata.gz = True

    def get_data(self):
        train_imgs, train_labels = self._mndata.load_training()
        test_imgs, test_labels = self._mndata.load_testing()
        return train_imgs, train_labels, test_imgs, test_labels


def main():
    train_imgs, train_labels, test_imgs, test_labels = MNISTGETTER().get_data()
    print_image_and_result(train_imgs[0], train_labels[0])
    print_image_and_result(test_imgs[0], test_labels[0])
    print(len(train_imgs))
    print(len(test_imgs))


def print_image_and_result(img, result):
    for i in range(len(img)):
        to_print = ". "
        if img[i] != 0:
            to_print = "@ "
        if (i+1) % 28 == 0:
            print(to_print, end="\n")
        else:
            print(to_print, end="")
    print("IS: ", result)


if __name__ == "__main__":
    main()
