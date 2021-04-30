import os

import torch
from torch import nn
from torch import optim

import torchvision
from torchvision import transforms
from torchvision.models import vgg19

import numpy as np
from PIL import Image

from .utils.functions import gram, inv_norm, convert_to_path


def forward(x_input, net, style_layer_index, content_layer_index) -> ([], []):
    """Forward propagate an input image, extract features
    for the content and style conv layers

    :param x_input: An input image of dimension [1, channel, height , width]
    :type x_input: torch.tensor, required
    :param net: Sequential network that is used to forward propagate
    :type net: nn.Module, required
    :param style_layer_index: List containing indexes of Conv layers used for style
    :type style_layer_index: list, required
    :param content_layer_index: List containing indexes of Conv layers used for content
    :type content_layer_index: list, required

    :return: Features extracted from style layers and content layers
    :rtype: tuple(list, list)
    """
    style_features, content_features = [], []
    for idx, layer in enumerate(net):
        x_input = layer(x_input)
        if idx in style_layer_index:
            style_features.append(x_input)
        elif idx in content_layer_index:
            content_features.append(x_input)

    return (style_features, content_features)


def run_style_transfer(style_image, content_image, output_dir, image_size=512, n_epochs=300, beta=1e5, alpha=1.0, learning_rate=1e-3, output_interval=10):
    """Runs style transfer on a content image

    :param style_image: Path of the style image
    :type style_image: pathlib.Path, reqiuired
    :param content_image: Path of the content image
    :type content_image: pathlib.Path, required
    :param output_dir: Path to output the stylized images (must be a directory)
    :type output_dir: pathlib.Path, required
    :param image_size: Size of the output image (default 512)
    :type image_size: int, optional
    :param n_epochs: Number of epochs (default 300)
    :type n_epochs: int, optional
    :param beta: Weight value for Style Loss (default 1e5)
    :type beta: float, optional
    :param alpha: Weight value for Content Loss (default 1.0)
    :type alpha: float, optional
    :param learning_rate: Learning rate (Default 0.01)
    :type learning_rate: float, optional
    :param output_interval: After `output_interval` epochs, an image will be saved (default 10)
    :type output_interval: int, optional

    """
    # Ensure all provided paths are of pathlib.Path type
    style_image = convert_to_path(style_image)
    content_image = convert_to_path(content_image)
    output_dir = convert_to_path(output_dir)

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Using {device}')

    net = vgg19(pretrained=True).features.to(device)

    # conv1_1, conv2_1, conv3_1, conv4_1, conv5_1
    style_layer_index = [0, 5, 10, 19, 28]

    # conv4_2
    content_layer_index = [21]

    transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
    ])

    # Load Images
    assert(os.path.isfile(style_image))
    assert(os.path.isfile(content_image))

    style_image = transform(Image.open(style_image)).unsqueeze(0).to(device)
    content_image = transform(Image.open(content_image)).unsqueeze(0).to(device)
    style_layer_weights = [0.75, 0.5, 0.2, 0.2, 0.2]

    # Pre-compute the Gram matrix for style
    style_features, _ = forward(style_image, net, style_layer_index, content_layer_index)
    _, content_features = forward(content_image, net, style_layer_index, content_layer_index)

    style_grams = [gram(feature) for feature in style_features]

    x_input = torch.clone(content_image).to(device)

    optimizer = optim.LBFGS([x_input.requires_grad_()], lr=learning_rate)

    # Use Mean Squared Error loss functions for both losses
    criterion_content = nn.MSELoss()
    criterion_style = nn.MSELoss()
    c_losses, s_losses = [], []

    for epoch in range(n_epochs):
        def closure():
            optimizer.zero_grad()
            t_style, t_content = forward(x_input, net, style_layer_index, content_layer_index)

            content_loss = criterion_content(t_content[0], content_features[0])

            style_loss = 0
            for i in range(len(t_style)):
                t_gram = gram(t_style[i])
                style_loss += (style_layer_weights[i] * criterion_style(t_gram, style_grams[i]))

            c_losses.append(content_loss.item())
            s_losses.append(style_loss.item())

            total_loss = (alpha * content_loss) + (beta * style_loss)
            total_loss.backward(retain_graph=True)

            print("Total Loss:", total_loss.item())

            return total_loss

        optimizer.step(closure)

        if epoch % output_interval == 0:
            image = transforms.ToPILImage()(inv_norm(x_input.clone().detach().cpu().squeeze()))
            output_dir.mkdir(parents=True, exist_ok=True)
            image.save(output_dir / f"{epoch}.png")
