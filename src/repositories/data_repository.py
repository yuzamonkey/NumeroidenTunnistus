from mnist import MNIST


class DataRepository():
    """Class for loading MNIST data
    """

    def __init__(self):
        """DataRepository class constructor
        """
        self._mndata = self._load_mnist_data()
        self._mndata.gz = True
        self._train_imgs, self._train_labels = self._mndata.load_training()
        self._test_imgs, self._test_labels = self._mndata.load_testing()

    def _load_mnist_data(self, path="./src/data"):
        """Loads the MNIST data using MNIST library. https://github.com/sorki/python-mnist

        Args:
            path (str, optional): Path to .gz-files. Defaults to "./src/data".

        Returns:
            MNIST: MNIST class object
        """
        return MNIST(path)

    def get_training_imgs(self):
        """
        Returns:
            int[][]: 60_000 training images
        """
        return self._train_imgs

    def get_training_labels(self):
        """
        Returns:
            int[]: 60_000 classification values of training image data
        """
        return self._train_labels

    def get_testing_imgs(self):
        """
        Returns:
            int[][]: 10_000 testing images
        """
        return self._test_imgs

    def get_testing_labels(self):
        """
        Returns:
            int[]: 10_000 classification values of testing image data
        """
        return self._test_labels

    def get_all_data(self):
        """
        Returns:
            tuple(int[][], int[], int[][], int[]): 60_000 training images,
            60_000 classification values of training images, 10_000 testing images,
            10_000 classification values of testing images.
        """
        return self._train_imgs, self._train_labels, self._test_imgs, self._test_labels


data_repository = DataRepository()
