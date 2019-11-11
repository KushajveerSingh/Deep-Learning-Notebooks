# Deep Learning Notebooks

List of my jupyter notebooks. I use <a href='https://pytorch.org/' target='_blank'>PyTorch</a> + <a href='https://www.fast.ai/' target='_blank'>fastai</a> as my main deep learning libraries and the notebooks are build using these libraries.

* **Multi Sample Dropout** is implemented and tested on CIFAR-100 for cyclic learning. My losses converged 4x faster when using num_samples=8. <a href='https://github.com/KushajveerSingh/Deep-Learning-Notebooks/tree/master/Multi%20Sample%20Dropout' target='_blank'>notebook</a>, <a href='https://arxiv.org/abs/1905.09788' target='_blank'>paper</a>

* Summarizing **Leslie N. Smith's research** in cyclic learning and hyper-parameter setting techniques. <a href='https://github.com/KushajveerSingh/Deep-Learning-Notebooks/tree/master/Leslie%20N.%20Smith%20paper%20notebooks%20(fastai)' target='_blank'>notebook</a>

    I refer to the following papers by Leslie N. Smith
    * A disciplined approach to neural network hyper-parameters: Part 1 -- learning rate, batch size, momentum, and weight decay
    * Super-Convergence: Very Fast Training of Neural Networks Using Learning Rates
    * Exploring loss function topology with cyclical learning rates
    * Cyclical Learning Rates for Training Neural Networks

* **Weight Standardization** is implemented and tested on cyclic learning. I find that it does not work well with cyclic learning using CIFAR-10. <a href='https://github.com/KushajveerSingh/Deep-Learning-Notebooks/tree/master/Blog%20Posts%20Notebooks/Weight%20Standardization:%20A%20New%20Normalization%20in%20town' target='_blank'>notebook</a>, <a href='https://arxiv.org/abs/1903.10520' target='_blank'>paper</a>

* Library Tutorials
    1. <a href='https://github.com/KushajveerSingh/Deep-Learning-Notebooks/tree/master/Blog%20Posts%20Notebooks/Training%20AlexNet%20with%20tips%20and%20checks%20on%20how%20to%20train%20CNNs' target='_blank'>Training AlexNet with tips and checks on how to train CNNs</a>