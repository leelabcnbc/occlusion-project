imagenet_root = '/home/haow3/occlusion-project/data/imagenet/'
caffe_root = '/home/haow3/software/caffe-rc3/'
result_root = '/home/haow3/occlusion-project/result/'

new_to_original_class_id = [99, 113, 132, 144, 321, 344, 386, 494, 497, 512, 525, 526, \
650, 656, 737, 763, 844, 848, 903, 945]

original_to_new_class_id = {512: 9, 321: 4, 386: 6, 99: 0, 132: 2, 848: 17, 497: 8,\
650: 12, 903: 18, 844: 16, 525: 10, 494: 7, 144: 3, 113: 1, 763: 15, 526: 11, 344: 5,\
656: 13, 737: 14, 945: 19}