from repositories.data_repository import DataRepository
from utils.utils import images_with_threshold


class NumberClassifier:
    def __init__(self):
        self._dr = DataRepository()
        # self._train_imgs, self._train_labels, self._test_imgs, self._test_labels = self._dr.get_all_data()

        train_imgs, self._train_labels, test_imgs, self._test_labels = self._dr.get_all_data()
        self._train_imgs = images_with_threshold(train_imgs, 140)
        self._test_imgs = images_with_threshold(test_imgs, 140)

    def sandbox(self):
        random_number = 423  # result: 2
        test_img, test_label = self._test_imgs[random_number], self._test_labels[random_number]

        self.print_image_and_result(test_img, test_label)

        k = 5
        k_nearest = []  # tuples: (value, index)
        for i in range(5000):
            dist = self._compare_D22(test_img, self._train_imgs[i])
            #dist = self._compare_D23(test_img, self._train_imgs[i])
            
            # print(f"DISTANCE BETWEEN {test_label} and {self._train_labels[i]} is {dist}")
            # print(f"i = {i}, dist = {dist}")
            k_nearest = self._update_k_nearest(k, k_nearest, (dist, i))
        print("K NEAREST", k_nearest)
        print("VALUES:")
        k_nearest = sorted(k_nearest)
        for item in k_nearest:
            print(self._train_labels[item[1]], end=", ")
        result = self._result_from_k_nearest(k_nearest)
        print("RESULT = ", result, "SHOULD BE = ", test_label)

        print("\nCOMPARISONS:") 
        for item in k_nearest:
            self.print_image_and_result(self._train_imgs[item[1]], self._train_labels[item[1]])

    def _update_k_nearest(self, k, k_nearest, dist):
        if len(k_nearest) < k:
            k_nearest.append(dist)
            return k_nearest
        # sorted_list = sorted(k_nearest, reverse=True)
        # if dist[0] < sorted_list[0][0]:
        sorted_list = sorted(k_nearest)
        if dist[0] > sorted_list[0][0]:
            sorted_list[0] = dist
            return sorted_list
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

    # def _set_dist(self, A, B):
    #     ### d_6 = 1/N_a * ∑(a ∈ A) d(a, B)
    #     N_a = len(A)
    #     sum_of_distances = 0
    #     for i in range(len(A)):
    #         sum_of_distances += self._point_and_set_dist(A[i], B)

    #     # d(a, B) = min(b∈B)||a-b||
    #     return 1/N_a * sum_of_distances
    
    def _set_dist(self, A, B):
        ### d_6 = 1/N_a * ∑(a ∈ A) d(a, B)
        N_a = len(A)
        sum_of_distances = 0
        for i in range(len(A)):
            if A[i] == B[i]:
                sum_of_distances += 1

        # d(a, B) = min(b∈B)||a-b||
        return 1/N_a * sum_of_distances

    def _point_and_set_dist(self, point_a, set_B):
        ### d(a, B) = min(b∈B)||a-b||
        # min_value = 99999
        # for i in range(len(set_B)):
        #     value = abs(point_a - set_B[i])
        #     min_value = min(min_value, value)
        # return min_value
        return point_a

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
