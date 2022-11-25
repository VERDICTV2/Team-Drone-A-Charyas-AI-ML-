
from detecto import core, utils, visualize
from detecto.visualize import show_labeled_image, plot_prediction_grid
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

custom_transforms = transforms.Compose([
transforms.ToPILImage(),
transforms.Resize(900),
transforms.RandomHorizontalFlip(0.5),
transforms.ColorJitter(saturation=0.2),
transforms.ToTensor(),
utils.normalize_transform(),
])



Train_dataset=core.Dataset("D:\\Edhitha 2023\\new_seg\\train",transform=custom_transforms)#L1
Test_dataset = core.Dataset("D:\\Edhitha 2023\\new_seg\\test")#L2
loader=core.DataLoader(Train_dataset, batch_size=2, shuffle=True)#L3
model = core.Model(['Target'])#L4
losses = model.fit(loader, Test_dataset, epochs=25, lr_step_size=5, learning_rate=0.001, verbose=True)#L5

model.save('model_weights.pth')
model = core.Model.load('model_weights.pth', ['Target']) 