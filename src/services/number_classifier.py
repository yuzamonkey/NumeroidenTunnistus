from repositories.data_repository import DataRepository


class NumberClassifier:
    def __init__(self):
        self._dr = DataRepository()

    def print_something(self):
        pass
        # train_imgs, train_labels, test_imgs, test_labels = self._dr.get_all_data()
        # self.print_image_and_result(train_imgs[0], 140, train_labels[0])
        # self.print_image_and_result(test_imgs[0], 140, test_labels[0])
        # print(len(train_imgs))
        # print(len(test_imgs))

    def train(self):
        imgs, labels = self._dr.get_training_data()
        self.print_image_and_result(imgs[465], 140, labels[465])

    def print_image_and_result(self, img, threshold=1, result=-1):
        for i in range(len(img)):
            to_print = ". "
            if img[i] >= threshold:
                to_print = "@ "
            if (i+1) % 28 == 0:
                print(to_print, end="\n")
            else:
                print(to_print, end="")
        print("IS: ", result)
