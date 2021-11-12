from repositories.data_repository import DataRepository
from utils.utils import images_with_threshold


class NumberClassifier:
    def __init__(self):
        self._dr = DataRepository()
        # self._train_imgs, self._train_labels, self._test_imgs, self._test_labels = self._dr.get_all_data()

        train_imgs, self._train_labels, test_imgs, self._test_labels = self._dr.get_all_data()
        self._train_imgs = images_with_threshold(train_imgs, 140)
        self._test_imgs = images_with_threshold(test_imgs, 140)

    def sandbox(self, test_set_index = 423, number_of_training_imgs = 10_000):
        random_number = 423  # result: 2
        test_img, test_label = self._test_imgs[random_number], self._test_labels[random_number]

        k = 5
        k_nearest = []  # tuples: (value, index)
        for i in range(number_of_training_imgs):
            dist = self._compare_D22(test_img, self._train_imgs[i])
            k_nearest = self._update_k_nearest(k, k_nearest, (dist, i))
        
        result = self._result_from_k_nearest(k_nearest)
        return result

    def _update_k_nearest(self, k, k_nearest, dist):
        if len(k_nearest) < k:
            k_nearest.append(dist)
            return k_nearest
        sorted_list = sorted(k_nearest, reverse=True)
        if dist[0] < sorted_list[0][0]:
            sorted_list[0] = dist
            return sorted_list
        else:
            return k_nearest

    def _result_from_k_nearest(self, k_nearest):
        results = []
        for item in k_nearest:
            results.append(self._train_labels[item[1]])
        return max(set(results), key=results.count)

    def _compare_D22(self, img1, img2):
        ### f_2 = max(d(A, B), d(B, A))
        return max(self._set_dist(img1, img2), self._set_dist(img2, img1))

    def _compare_D23(self, img1, img2):
        ### f_3 = (d(A,B) + d(B, A)) / 2
        return (self._set_dist(img1, img2) + self._set_dist(img2, img1)) / 2

    def _set_dist(self, A, B):
        # d_6 = 1/N_a * ∑(a ∈ A) d(a, B)
        N_a = len(A)
        sum_of_distances = 0
        for i in range(len(A)):
            sum_of_distances += self._point_and_set_dist(A[i], B[i])
        return 1/N_a * sum_of_distances

    def _point_and_set_dist(self, a, b):
        # d(a, B) = min(b∈B)||a-b||
        return abs(a - b)

    def print_image_and_result(self, img, result, threshold=1):
        for i, value in enumerate(img):
            to_print = f"{value} "
            # to_print = ". "
            # if value >= threshold:
            #     to_print = "@ "
            if (i+1) % 28 == 0:
                print(to_print, end="\n")
            else:
                print(to_print, end="")
        print("IS: ", result)
