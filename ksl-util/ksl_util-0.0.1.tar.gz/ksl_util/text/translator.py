from ksl_util.log import printlog

def translate(string):
    
    batch_list = [
        'batch_size', 'batch', 'batchSize', 'BatchSize', 'batch size', 'batchsize'
    ]
    
    img_size_list = [
        'img_size', 'image_size', 'imgSize', 'ImageSize', 'Image_Size', 'image size', 'imagesize', 'imgsize'
    ]
    
    img_resize_flag_list = [
        'imageresizeflag', 'imgresizeflag', 'imgflag', 'imgresizingflag', 'resizeflag'
    ]
    
    train_flag_list = [
        'train', 'trn', 'training'
    ]
    
    valid_flag_list = [
        'valid', 'vld', 'validation'
    ]
    
    test_flag_list = [
        'test', 'tst', 'testing'
    ]
    
    
    batch = 'batch_size'
    img_size = 'image_size'
    img_resize_flag = 'image_resize_flag'
    train_flag = 'trn'
    valid_flag = 'vld'
    test_flag = 'tst'


    string_tmp = string.lower()
    string_tmp = string_tmp.replace('_', '')
    
    
    if string_tmp in batch_list: return batch
    elif string_tmp in img_size_list: return img_size
    elif string_tmp in img_resize_flag_list: return img_resize_flag
    elif string_tmp in train_flag_list: return train_flag
    elif string_tmp in valid_flag_list: return valid_flag
    elif string_tmp in test_flag_list: return test_flag
    else: return string
    


class translated_dictionary:
    
    def __init__(self, init_value=None):
        self.__dictionary__ = dict()
        self.__keys__ = list()
        
        if init_value is not None:
            self.translate(init_value)
        
    
    def translate(self, dictionary):
        
        for key in dictionary.keys():
            self.__keys__.append(translate(key))
            self.__dictionary__[translate(key)] = dictionary[key]
            
    
    def __getitem__(self, item):
        return self.__dictionary__[translate(item)]
    
    def keys(self):
        return self.__keys__
    