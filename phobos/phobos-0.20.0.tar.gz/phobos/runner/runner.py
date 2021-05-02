from .scheduler import get_scheduler
from .optimizer import get_optimizer
from datetime import datetime

import torch
import os
import logging

from phobos.logger.baselogger import configure_logger
from torch.autograd import Variable
from phobos.metrics.metrics import Metrics


class Runner():
    """Runner class.

    Parameters
    ----------
    model : torch.nn.Module
        model to train or validate.
    optimizer : torch.optim
        optimizer to minimize loss.
    criterion : phobos.loss
        criterion to measure loss for model.
    train_loader : torch.utils.data.Dataloader
        dataloader to load training dataset.
    val_loader : torch.utils.data.Dataloader
        dataloader to load validation dataset.
    args : list
        list of arguments.
    polyaxon_exp : poyaxon.tracking.Run
        polyaxon experiment.

    Attributes
    ----------
    gpu : int
        id of gpu for model run.
    train_metrics : type
        Description of attribute `train_metrics`.
    val_metrics : type
        Description of attribute `val_metrics`.
    epoch : int
        training epoch.

    """

    def __init__(self,
                 model,
                 criterion,
                 train_loader,
                 val_loader,
                 args,
                 polyaxon_exp=None):
        """Initialises runner object.

        Parameters
        ----------
        model : torch.nn.Module
            model to train or validate.
        criterion : phobos.loss
            criterion to measure loss for model.
        train_loader : torch.utils.data.Dataloader
            dataloader to load training dataset.
        val_loader : torch.utils.data.Dataloader
            dataloader to load validation dataset.
        args : namespace
            namespace of input arguments.
        polyaxon_exp : poyaxon.tracking.Run
            polyaxon experiment.

        """
        self.polyaxon_exp = polyaxon_exp
        self.gpu = args.gpu
        self.model = model
        self.criterion = criterion
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.optimizer = get_optimizer(args.optimizer, args.optimizer_args, model)
        if hasattr(args, 'scheduler') and hasattr(args, 'scheduler_args'):
            self.scheduler = get_scheduler(args.scheduler, args.scheduler_args, self.optimizer)
        else:
            self.scheduler = None
        self.train_metrics = Metrics(polyaxon_exp=polyaxon_exp,
                                     phase='train',
                                     metrics_strings=args.metrics,
                                     num_classes=args.num_classes)
        self.val_metrics = Metrics(polyaxon_exp=polyaxon_exp,
                                   phase='val',
                                   metrics_strings=args.metrics,
                                   num_classes=args.num_classes)
        self.log_level = args.log_level
        self.log_file = os.path.join(args.log_dir, datetime.now().strftime("%d-%b-%Y_%H:%M:%S") + ".log")
        configure_logger(self.log_level, self.log_file)

        self.epoch = 0

    def set_epoch_metrics(self):
        """Sets epoch metrics and increments epoc count
            at the end of every epoch.

        """
        logging.debug("Enter set_epoch_metrics routine")
        self.train_metrics.reset()
        self.val_metrics.reset()
        self.epoch += 1
        logging.debug("Exit set_epoch_metrics routine")

    def tensorize_batch(self, input_tensor, label_tensor):
        """Tensorize batch of input images and labels,
            and move them to gpu.

        Parameters
        ----------
        input_tensor : numpy.ndarray
            batch of input images.
        label_tensor : numpy.ndarray
            batch of input labels.

        Returns
        -------
        (torch.Tensor,torch.Tensor)
            input and label tensors in gpu.

        """
        logging.debug("Enter tensorize_batch routine")
        input_tensor = Variable(input_tensor).float()
        label_tensor = Variable(label_tensor).long()
        if self.gpu > -1:
            input_tensor = input_tensor.to(self.gpu)
            label_tensor = label_tensor.to(self.gpu)
        logging.debug("Exit tensorize_batch routine")

        return input_tensor, label_tensor

    def train_forward_backward(self, input_tensor, label_tensor):
        """Performs forward propagation, loss evaluation
        and backward propagation while training model.

        Parameters
        ----------
        input_tensor : torch.Tensor
            tensorised batch of input images.
        label_tensor : torch.Tensor
            tensorised batch of input labels.

        Returns
        -------
        (torch.Tensor,torch.nn.Module)
        prediction_tensor : torch.Tensor
            output/prediction tensor from model.
        loss : torch.nn.Module
            forward propagation loss

        """
        # Zero the gradient
        logging.debug("Enter train_forward_backward routine")
        self.optimizer.zero_grad()

        # Get model predictions, calculate loss, backprop
        prediction_tensor = self.model(input_tensor)
        loss = self.criterion(prediction_tensor, label_tensor)
        loss.backward()
        self.optimizer.step()
        logging.debug("Exit train_forward_backward routine")

        return prediction_tensor, loss

    def eval_forward(self, input_tensor, label_tensor):
        """Performs forward propagation while evaluating model.

        Parameters
        ----------
        input_tensor : torch.Tensor
            tensorised batch of input images.
        label_tensor : torch.Tensor
            tensorised batch of input labels.

        Returns
        -------
        (torch.Tensor,torch.nn.Module)
        prediction_tensor : torch.Tensor
            output/prediction tensor from model.
        loss : torch.nn.Module
            forward propagation loss

        """
        # Get predictions and calculate loss
        logging.debug("Enter eval_forward routine")
        prediction_tensor = self.model(input_tensor)
        loss = self.criterion(prediction_tensor, label_tensor)
        logging.debug("Exit eval_forward routine")

        return prediction_tensor, loss

    def train_model(self):
        """Trains model.

        Returns
        -------
        dict
            dictionary of training metrics.

        """
        logging.debug("Enter train_model routine")
        self.model.train()

        for input_tensor, label_tensor in self.train_loader:
            input_tensor, label_tensor = self.tensorize_batch(
                input_tensor, label_tensor)

            prediction_tensor, loss = self.train_forward_backward(
                input_tensor, label_tensor)
            self.train_metrics.compute(prediction_tensor, label_tensor, loss)

            # clear batch variables from memory
            del input_tensor, label_tensor
        logging.debug("Exit train_model routine")

        return self.train_metrics.crunch_it(self.epoch)

    def eval_model(self):
        """Evaluates model.

        Returns
        -------
        dict
            dictionary of evaluation metrics.

        """
        # self.model.eval()
        logging.debug("Enter eval_model routine")
        with torch.no_grad():
            for input_tensor, label_tensor in self.val_loader:
                input_tensor, label_tensor = self.tensorize_batch(
                    input_tensor, label_tensor)

                prediction_tensor, loss = self.eval_forward(
                    input_tensor, label_tensor)
                self.val_metrics.compute(prediction_tensor, label_tensor, loss)

                # clear batch variables from memory
                del input_tensor, label_tensor

        metrics = self.val_metrics.crunch_it(self.epoch)

        if self.scheduler:
            self.scheduler.step(metrics['val_loss'])
        logging.debug("Exit eval_model routine")

        return metrics
