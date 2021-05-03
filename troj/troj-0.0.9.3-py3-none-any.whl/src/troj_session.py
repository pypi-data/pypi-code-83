import numpy as np
import art
from art.estimators.classification import PyTorchClassifier, KerasClassifier
import torch
from troj_dataset import TrojDataLoader, TrojDataset
import tensorflow as tf
from attack import array_utils, TrojEpsilon


'''
I imagine this class is like a session, it stores all the stuff we'd need to access frequently, collating it into one class
for now will store the client instance with key infod
also dataset information


Session:
    Methods:
        create_troj_dataset:
            initializes the dataframe
        create_attack:
            initializes the attack target using the model as input
        run_troj_test(test_loader, loss):
        
'''


class TrojSession():
    def __init__(self):
        super().__init__()
        # thing that makes requests to the troj api
        self.client = None
        # dataframe with the user's testing data
        self.dataset = None
        # dataloader made from the dataset
        self.dataloader = None
        self.adv_classifier = None
        self.attacker = None
        self.model = None
        self.loss_func = None

    def create_troj_dataset(self, image_folder_path, annotation_file=None):
        ds = TrojDataset()
        if annotation_file == None:
            ds.CreateDF(image_folder_path)
        else:
            ds.CreateDF(image_folder_path, annotation_file)

        self.dataset = ds

    def create_troj_dataloader(self, transforms=None):
        if self.dataset != None:
            self.dataloader = TrojDataLoader(self.dataset.dataframe, self.dataset.data_structure, self.dataset.root_folder, transforms=transforms)
            
        else:
            return "error"

    def create_attack_target(self, model, loss, input_shape, num_classes):
        '''
        Instantiates Max's TrojEpsAttack class with params, saves under session class for self accessibility
        '''

        # create the attack Object
        try:
            self.model = model
            classifier = PyTorchClassifier(
                model, loss, input_shape, num_classes)
            self.adv_classifier = classifier
            attacker = TrojEpsilon.TrojEpsAttack(classifier)
            self.attacker = attacker
        except print(0):
            print("Error instantiating attack")
            self.adv_classifier = None

    def Create_Troj_Epsilon_Attack(self, model, input_shape, num_classes, loss_func=None):
        print(type(model))
        model_type = type(model)
        if issubclass(model_type, torch.nn.Module):
            if loss_func is not None:
                # ensure model is in eval mode, not sure how to check that rn
                self.classifier = PyTorchClassifier(model, loss_func, input_shape, num_classes)
            else:
                print("Pass in loss function with pytorch classifier!")
            
        elif issubclass(model_type, tf.keras.Model):
            # ensure model is compiled tensorflow
            if True:
                self.classifier = KerasClassifier(model)




        self.attacker = TrojEpsilon.TrojEpsAttack(self.classifier)
        self.loss_func = loss_func

    def attack_and_log(self, data, target, test_loss, prediction, index, device):
        '''
        This will work for pytorch, tensorflow has no device
        '''
        # index = index.numpy()
        # send data and target to cpu, convert to numpy
        data, target = data.detach().cpu().numpy(), target.detach().cpu().numpy()
        # generate the adversarial image using the data numpy array and label numpy array
        adv_x = self.attacker.generate(data, target)
        # change loss function reduction again (?)
        self.loss_func.reduction = 'none'
        # use the classifier object to predict the output of the adversarial image
        adv_preds = self.classifier.predict(adv_x)
        # calculate the loss from the prediction
        adv_loss = self.loss_func(torch.from_numpy(adv_preds).to(device), torch.from_numpy(
            target).to(device)).clone().detach().cpu().numpy()
        # get the perturbation distance between x and adv_x
        perturbation = array_utils.compute_Lp_distance(data, adv_x)
    


        # want to write a function to add all this shit at once, can we obfuscate it in a simple way?
        self.dataset.dataframe.loc[index, 'Linf_perts'] = perturbation
        self.dataset.dataframe.loc[index, 'Loss'] = test_loss
        self.dataset.dataframe.loc[index, 'Adversarial_Loss'] = adv_loss
        self.dataset.dataframe.loc[index, 'prediction'] = prediction
        self.dataset.dataframe.loc[index, 'Adversarial_prediction'] = np.argmax(
            adv_preds, axis=1)
