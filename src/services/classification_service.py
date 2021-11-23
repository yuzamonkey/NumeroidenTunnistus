import random
from repositories.data_repository import data_repository
from utils.utils import as_2d_arrays, image_with_threshold

class ClassificationService:
    def get_example_number(self, idx, threshold=1):
        imgs = data_repository.get_testing_imgs()
        img = as_2d_arrays(image_with_threshold(imgs[idx], threshold))
        retval = ""
        for i in range(len(img)):
            for j in range(len(img[0])):
                if img[i][j] == 1:
                    retval += "⚫ "
                    #retval += "▪ "
                else:
                    retval += "  "
            retval += "\n"

        return retval

    def start_knn_classification(self, k, threshold, distance_measure, test_size, train_size):
        print("\nSTART KNN WITH PARAMS")
        print("K ", k)
        print("THRESHOLD ", threshold)
        print("DIST ", distance_measure)
        print("TEST_SIZE ", test_size)
        print("TRAIN_SIZE ", train_size)
        print("")

classification_service = ClassificationService()