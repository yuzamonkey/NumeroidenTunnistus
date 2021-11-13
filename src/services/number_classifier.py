from repositories.data_repository import DataRepository
from utils.utils import images_with_threshold


class NumberClassifier:
    """Class for number classification

    Attributes:
        train_imgs: training image data
        train_labels: training image labels
        test_imgs: testing image data
        test_labels: testing image labels
    """

    def __init__(self):
        """NumberClassifier constructor. Gets data from DataRepository class
        """
        self._dr = DataRepository()
        train_imgs, self._train_labels, test_imgs, self._test_labels = self._dr.get_all_data()
        self._train_imgs = images_with_threshold(train_imgs, 140)
        self._test_imgs = images_with_threshold(test_imgs, 140)

    def classify_set_of_numbers(self, k, number_of_test_images, number_of_training_imgs):
        """Classifies a set of data with given parameters with k-nearest neighbor method

        Args:
            k (int): value of k
            number_of_test_images (int): number of how many test images are wanted to be tested.
            Range between 1-10_000
            number_of_training_imgs (int): number of how many training images are used.
            Range between 1-60_000

        Returns:
            float: Success percentage
        """
        num_of_errors = 0
        for i in range(number_of_test_images):
            label = self._test_labels[i]
            result = self.classify_number(k, i, number_of_training_imgs)
            if result != label:
                num_of_errors += 1
                # print("RESULT: ", result, " Should have been ", label)
        percentage = (1 - (num_of_errors / number_of_test_images)) * 100
        print("PERCENTAGE: ", percentage, "%")
        return percentage

    def classify_number(self, k, test_set_index, number_of_training_imgs):
        """Classifies a number with given parameters with k-nearest neighbor method

        Args:
            k (int): value of k
            test_set_index (int): index of number to be classified from test set
            number_of_training_imgs (int): number of how many training images are used.
            Range between 1-60_000

        Returns:
            int: classification value
        """
        test_img = self._test_imgs[test_set_index]
        k_nearest = []  # tuples: (value, index)
        for i in range(number_of_training_imgs):
            dist = self._compare_d23(test_img, self._train_imgs[i])
            k_nearest = self._update_k_nearest(k, k_nearest, (dist, i))

        result = self._result_from_k_nearest(k_nearest)
        return result

    def _update_k_nearest(self, k, k_nearest, dist):
        """Updates the k-nearest neighbors

        Args:
            k (int): value of k
            k_nearest (tuple(distance, index)[]): current k-nearest neighbors
            dist (tuple(distance, index)): neighbor to be compared with current k-nearest neighbors

        Returns:
            tuple(distance, index)[]: updated k-nearest neighbors
        """
        if len(k_nearest) < k:
            k_nearest.append(dist)
            return k_nearest
        sorted_list = sorted(k_nearest, reverse=True)
        if dist[0] < sorted_list[0][0]:
            sorted_list[0] = dist
            return sorted_list
        return k_nearest

    def _result_from_k_nearest(self, k_nearest):
        """Gives the classification result on k-nearest neighbors

        Args:
            k_nearest (tuple(distance, index)[]): current k-nearest neighbors

        Returns:
            int: classification value
        """
        results = []
        for item in k_nearest:
            results.append(self._train_labels[item[1]])
        return max(set(results), key=results.count)

    def _compare_d22(self, img1, img2):
        """Distance measure D22 from
        https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf

        Args:
            img1 (int[]): image data
            img2 (int[]): image data

        Returns:
            float: distance between two images
        """
        ### f_2 = max(d(A, B), d(B, A))
        return max(self._set_dist(img1, img2), self._set_dist(img2, img1))

    def _compare_d23(self, img1, img2):
        """Distance measure D23 from
        https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf

        Args:
            img1 (int[]): image data
            img2 (int[]): image data

        Returns:
            float: distance between two images
        """
        ### f_3 = (d(A,B) + d(B, A)) / 2
        return (self._set_dist(img1, img2) + self._set_dist(img2, img1)) / 2

    def _set_dist(self, A, B):
        """Distance between two datasets A and B. Directed distance measure d6 from
        https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf

        Args:
            A (int[]): dataset
            B (int[]): dataset

        Returns:
            float: distance between two datasets
        """
        # d_6 = 1/N_a * ∑(a ∈ A) d(a, B)
        sum_of_distances = 0
        for i in range(len(A)): # pylint: disable=consider-using-enumerate
            sum_of_distances += self._point_dist(A[i], B[i])
        return 1/len(A) * sum_of_distances

    def _point_dist(self, a, b):
        """Heuristic distance between two points

        Args:
            a (int): integer value
            b (int): integer value

        Returns:
            int: distance between values a and b
        """
        # d(a, B) = min(b∈B)||a-b||
        return abs(a - b)

    def print_image_and_result(self, img, result, threshold=1):
        """Prints image and result

        Args:
            img (int[]): image data
            result (int): class of the image
            threshold (int, optional): Grayscale pixel values equal or greater than threshold
            will be printed. Defaults to 1.
        """
        for i, value in enumerate(img):
            # to_print = f"{value} "
            to_print = "  "
            if value >= threshold:
                to_print = "@ "
            if (i+1) % 28 == 0:
                print(to_print, end="\n")
            else:
                print(to_print, end="")
        print("IS: ", result)
