from math import sqrt
from repositories.data_repository import data_repository as dr
from utils.utils import as_2d_arrays, images_with_threshold


class KNN:
    """Class for number classification

    Attributes:
        train_imgs: training image data
        train_labels: training image labels
        test_imgs: testing image data
        test_labels: testing image labels
    """

    def __init__(self):
        """KNN constructor. Gets data from DataRepository class
        """
        self._dr = dr
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
        errors = []
        for i in range(number_of_test_images):
            label = self._test_labels[i]
            result = self.classify_number(k, i, number_of_training_imgs)
            if result != label:
                errors.append((i, result))
            print(f"{i+1}/{number_of_test_images}")

        # for i, r in errors:
        #     print("RESULT: ", r, " Should have been ",
        #           self._test_labels[i], "at index ", i)
        #     print_image_and_result(self._test_imgs[i], self._test_labels[i])
        percentage = (1 - (len(errors) / number_of_test_images)) * 100
        print(
            f"""PERCENTAGE: {percentage}%
            ({number_of_test_images - len(errors)} / {number_of_test_images})""")
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
        test_img = as_2d_arrays(self._test_imgs[test_set_index])
        k_nearest = []  # tuples: (value, index)
        for i in range(number_of_training_imgs):
            dist = self._compare_d22(
                test_img, as_2d_arrays(self._train_imgs[i]))
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
        sum_of_distances = 0.0
        for i in range(len(A)):  # pylint: disable=consider-using-enumerate
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    sum_of_distances += self._point_to_set_dist(i, j, B)
        return 1/len(A) * sum_of_distances

    def _point_to_set_dist(self, A_i, A_j, B):
        """Calculates the distance from point in set A to closest point in set B

        Args:
            A_i (int): First index of set A
            A_j (int): Second index of set A
            B (int): Set B

        Returns:
            float: Distance from A[i][j] to closest point in set B
        """
        # Danger of looping forever
        # Is not optimised
        found = False
        dist = 999
        min_i = A_i
        max_i = A_i
        min_j = A_j
        max_j = A_j
        while not found:
            for i in range(min_i, max_i):
                for j in range(min_j, max_j):
                    if B[i][j] == 1:
                        found = True
                        dist = min(dist, self._calc_dist(A_i, A_j, i, j))
            if not found:
                if min_i > 0:
                    min_i -= 1
                if max_i < 27:
                    max_i += 1
                if min_j > 0:
                    min_j -= 1
                if max_j < 27:
                    max_j += 1
            else:
                break
        return dist

    def _calc_dist(self, A_i, A_j, B_i, B_j):
        """Euclidian distance between two points

        Args:
            A_i (int): First index of set A
            A_j (int): Second index of set A
            B_i (int): First index of set B
            B_j (int): Second index of set B

        Returns:
            float: Euclidian distance between two points
        """
        # sqrt((xa-xb)^2 + (ya-yb)^2)
        return sqrt(pow(A_i - B_i, 2) + pow(A_j - B_j, 2))


knn = KNN()
