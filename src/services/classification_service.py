from repositories.data_repository import data_repository
from utils.utils import as_2d_arrays, image_with_threshold, image_as_2d_string
from services.knn import knn
from ui.results import results


class ClassificationService:
    def get_example_number(self, idx, threshold=1):
        imgs = data_repository.get_training_imgs()
        img = as_2d_arrays(image_with_threshold(imgs[idx], threshold))
        return image_as_2d_string(img)
        
    def start_knn_classification(self, k, threshold, distance_measure, test_size, train_size):
        print("\nSTART KNN WITH PARAMS")
        print("K ", k)
        print("THRESHOLD ", threshold)
        print("DIST ", distance_measure)
        print("TEST_SIZE ", test_size)
        print("TRAIN_SIZE ", train_size)
        print("")

        correct_count, errors_count, errors = knn.classify_set_of_numbers(
            k, threshold, test_size, train_size, distance_measure)
        results.set_correct_count(correct_count)
        results.set_errors_count(errors_count)
        results.set_errors(errors)


classification_service = ClassificationService()
