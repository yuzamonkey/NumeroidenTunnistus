from mnist import MNIST
import os


class DataRepository():
    def __init__(self):
        self._mndata = self._load_mnist_data()
        self._mndata.gz = True
        self._train_imgs, self._train_labels = self._mndata.load_training()
        self._test_imgs, self._test_labels = self._mndata.load_testing()

    def _load_mnist_data(self):
        if os.path.isdir("./data"):
            return MNIST("./data")
        elif os.path.isdir("./src/data"):
            return MNIST("./src/data")
        else:
            raise Exception("No data found")

    def get_training_imgs(self):
        return self._train_imgs

    def get_training_labels(self):
        return self._train_labels

    def get_training_data(self):
        return self._train_imgs, self._train_labels

    def get_test_imgs(self):
        return self._test_imgs

    def get_test_labels(self):
        return self._test_labels

    def get_test_data(self):
        return self._test_imgs, self._test_labels

    def get_all_data(self):
        return self._train_imgs, self._train_labels, self._test_imgs, self._test_labels
