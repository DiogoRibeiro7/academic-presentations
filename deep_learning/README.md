# Deep Learning Fundamentals

**Comprehensive introduction to neural networks and deep learning architectures**

## 📚 Overview

This presentation provides a comprehensive introduction to deep learning, covering fundamental concepts, modern architectures, and practical implementation techniques. The material is designed for graduate-level courses and assumes familiarity with linear algebra, calculus, and Python programming.

## 🎯 Learning Objectives

By the end of this module, students will be able to:

1. **Mathematical Foundations**
   - Understand the mathematical foundations of neural networks
   - Derive backpropagation algorithm from first principles
   - Implement gradient descent and its variants

2. **Network Architectures**
   - Design and train multilayer perceptrons
   - Build Convolutional Neural Networks (CNNs) for computer vision
   - Implement Recurrent Neural Networks (RNNs) and LSTMs for sequential data
   - Understand Transformer architecture and attention mechanisms

3. **Optimization Techniques**
   - Apply modern optimization methods (SGD, Momentum, Adam, AdamW)
   - Implement learning rate scheduling
   - Use gradient clipping and normalization techniques

4. **Regularization**
   - Apply dropout, batch normalization, and layer normalization
   - Implement early stopping and model checkpointing
   - Use data augmentation for improved generalization

5. **Practical Skills**
   - Train deep networks using PyTorch or TensorFlow
   - Debug training issues (vanishing/exploding gradients)
   - Evaluate model performance and diagnose overfitting/underfitting

## 📋 Topics Covered

### Part 1: Foundations
- Perceptron and linear models
- Multilayer perceptrons (MLPs)
- Activation functions (ReLU, sigmoid, tanh, Swish, GELU)
- Loss functions (MSE, cross-entropy, focal loss)
- Backpropagation algorithm
- Gradient descent variants

### Part 2: Convolutional Neural Networks
- Convolution operations and feature maps
- Pooling layers
- Classic architectures (LeNet, AlexNet, VGG)
- Modern architectures (ResNet, DenseNet, EfficientNet)
- Transfer learning and fine-tuning

### Part 3: Recurrent Architectures
- Vanilla RNNs and vanishing gradients
- Long Short-Term Memory (LSTM)
- Gated Recurrent Units (GRU)
- Bidirectional RNNs
- Sequence-to-sequence models

### Part 4: Attention & Transformers
- Attention mechanisms
- Self-attention and multi-head attention
- Transformer architecture
- BERT, GPT, and other modern models
- Vision Transformers (ViT)

### Part 5: Training Best Practices
- Initialization strategies (Xavier, He)
- Batch normalization and layer normalization
- Dropout and regularization
- Learning rate scheduling
- Gradient clipping
- Mixed precision training

## 📖 Prerequisites

**Required:**
- Linear algebra (matrix operations, eigenvalues)
- Calculus (derivatives, chain rule, gradients)
- Python programming
- Basic probability and statistics

**Recommended:**
- NumPy and basic scientific computing
- Experience with scikit-learn
- Familiarity with basic machine learning concepts

## 🛠️ Technical Requirements

### Software
```bash
# Python environment
pip install torch torchvision torchaudio
pip install tensorflow  # Alternative to PyTorch
pip install numpy scipy matplotlib seaborn
pip install scikit-learn pandas
pip install tensorboard  # For visualization
```

### Hardware
- **Minimum:** CPU with 8GB RAM
- **Recommended:** GPU with CUDA support (8GB+ VRAM)
- **Cloud alternatives:** Google Colab, Kaggle Notebooks, AWS SageMaker

## 📝 Materials

### Presentation
- **File:** `deep_learning_beamer.tex`
- **Compile:** `pdflatex deep_learning_beamer.tex` (run twice)
- **Format:** Beamer slides with aspect ratio 16:9

### Code Examples
Code implementations will be available in:
- `../code/deep_learning/` (when created)

### Exercises
Practice problems available in:
- `../exercises/deep_learning/` (when created)

## 📚 Recommended References

### Textbooks
1. **Deep Learning** - Goodfellow, Bengio, Courville (2016)
   - The definitive deep learning textbook
   - Free online: https://www.deeplearningbook.org/

2. **Neural Networks and Deep Learning** - Aggarwal (2018)
   - More recent, with practical focus
   - Excellent coverage of modern architectures

3. **Dive into Deep Learning** - Zhang et al. (2021)
   - Interactive book with code
   - Free online: https://d2l.ai/

### Research Papers

**Foundational:**
- LeCun et al. (1998) - "Gradient-based learning applied to document recognition"
- Krizhevsky et al. (2012) - "ImageNet classification with deep CNNs (AlexNet)"
- He et al. (2016) - "Deep residual learning for image recognition (ResNet)"

**Transformers:**
- Vaswani et al. (2017) - "Attention is all you need"
- Devlin et al. (2019) - "BERT: Pre-training of deep bidirectional transformers"
- Dosovitskiy et al. (2021) - "An image is worth 16x16 words (ViT)"

**Training Techniques:**
- Ioffe & Szegedy (2015) - "Batch normalization"
- Ba et al. (2016) - "Layer normalization"
- Kingma & Ba (2015) - "Adam: A method for stochastic optimization"
- Loshchilov & Hutter (2019) - "Decoupled weight decay regularization (AdamW)"

### Online Resources
- **CS231n** (Stanford) - Convolutional Neural Networks for Visual Recognition
- **CS224n** (Stanford) - Natural Language Processing with Deep Learning
- **Fast.ai** - Practical Deep Learning for Coders
- **PyTorch Tutorials** - https://pytorch.org/tutorials/
- **TensorFlow Tutorials** - https://www.tensorflow.org/tutorials

## 🎓 Assessment

Students will be evaluated on:

1. **Problem Sets (40%)**
   - Implement backpropagation from scratch
   - Build and train CNN for image classification
   - Implement LSTM for sequence prediction
   - Fine-tune pretrained models

2. **Quizzes (20%)**
   - Mathematical foundations
   - Architecture components
   - Training techniques

3. **Final Project (40%)**
   - Apply deep learning to real-world problem
   - Compare multiple architectures
   - Write technical report
   - Present findings

See `../assessments/` for detailed rubrics and evaluation criteria.

## 💡 Study Tips

1. **Master the Math First**
   - Work through backpropagation derivation by hand
   - Understand gradient computation at each layer
   - Practice matrix calculus

2. **Code from Scratch**
   - Implement simple networks without frameworks
   - Build custom training loops
   - Debug gradient computations

3. **Use Frameworks Wisely**
   - Start with high-level APIs (Keras, Lightning)
   - Graduate to lower-level APIs (PyTorch, TensorFlow)
   - Understand what's happening under the hood

4. **Experiment Extensively**
   - Try different architectures
   - Vary hyperparameters systematically
   - Keep detailed experiment logs

5. **Read Papers**
   - Start with classic papers
   - Follow recent advances on arXiv
   - Implement key ideas from papers

## 🔗 Related Topics

- **Prerequisites:** Statistical Learning, Feature Engineering
- **Follow-up:** Reinforcement Learning, Computer Vision, NLP
- **Complementary:** Optimization, Explainable AI

## 📧 Contact

For questions about this module:
- **Instructor:** Diogo Ribeiro
- **Email:** dfr@esmad.ipp.pt
- **Office Hours:** By appointment
- **Issues:** [GitHub Issues](https://github.com/diogoribeiro7/academic-presentations/issues)

## 📄 License

**Content:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
**Code:** MIT License

---

*Last Updated: January 2025*
*Part of the Academic Presentations series by Diogo Ribeiro, ESMAD & Mysense.ai*
