# Deep Learning Self-Assessment Checklist

**Topic:** Deep Learning Fundamentals
**Related Presentation:** `../../deep_learning/`
**Last Updated:** January 2025

## How to Use This Checklist

- Check ✅ items you understand well
- Leave unchecked ⬜ items you need to study
- Use color coding (see README) for more granular tracking
- Review before quizzes, exams, and while studying

---

## 1. Neural Network Fundamentals

### Conceptual Understanding
- [ ] I can explain what a neuron does in a neural network
- [ ] I understand the difference between shallow and deep networks
- [ ] I can describe the universal approximation theorem
- [ ] I understand why depth matters in neural networks
- [ ] I can explain the role of non-linear activation functions

### Mathematical Foundations
- [ ] I can write the equation for a single neuron
- [ ] I understand matrix formulation of forward propagation
- [ ] I can compute the output of a multilayer perceptron by hand
- [ ] I know how to represent networks using mathematical notation

### Practical Skills
- [ ] I can implement a simple neural network from scratch
- [ ] I know how to initialize network weights
- [ ] I can build networks using PyTorch or TensorFlow
- [ ] I can visualize network architecture

---

## 2. Activation Functions

### Conceptual Understanding
- [ ] I understand why activation functions are necessary
- [ ] I can compare linear vs non-linear activations
- [ ] I know the trade-offs between different activation functions
- [ ] I understand the vanishing gradient problem
- [ ] I can explain when to use each activation function

### Mathematical Foundations
- [ ] I can write equations for: sigmoid, tanh, ReLU, Leaky ReLU
- [ ] I can compute derivatives of activation functions
- [ ] I understand the range and domain of each activation
- [ ] I know the gradient properties of each activation

### Practical Skills
- [ ] I can implement activation functions from scratch
- [ ] I know which activation to use for hidden layers
- [ ] I know which activation to use for output layers
- [ ] I can identify activation-related training issues

---

## 3. Backpropagation & Training

### Conceptual Understanding
- [ ] I understand the chain rule and its role in backprop
- [ ] I can explain forward and backward passes
- [ ] I understand how gradients flow through the network
- [ ] I know what causes vanishing/exploding gradients
- [ ] I understand the difference between epoch, batch, and iteration

### Mathematical Foundations
- [ ] I can derive backpropagation for a simple network
- [ ] I can compute gradients for any layer by hand
- [ ] I understand the Jacobian matrix in backprop
- [ ] I can write update equations for gradient descent

### Practical Skills
- [ ] I can implement backpropagation from scratch
- [ ] I can debug gradient computation issues
- [ ] I know how to use automatic differentiation
- [ ] I can verify gradients using numerical methods
- [ ] I can monitor training with loss curves

---

## 4. Loss Functions & Optimization

### Conceptual Understanding
- [ ] I understand the purpose of loss functions
- [ ] I can distinguish between regression and classification losses
- [ ] I know when to use different loss functions
- [ ] I understand the connection between loss and likelihood
- [ ] I can explain regularization terms (L1, L2)

### Mathematical Foundations
- [ ] I can write equations for: MSE, MAE, cross-entropy
- [ ] I can derive gradients of common loss functions
- [ ] I understand the mathematics of L1 and L2 regularization
- [ ] I can compute loss for multi-class problems

### Practical Skills
- [ ] I can implement loss functions from scratch
- [ ] I know which loss to use for different tasks
- [ ] I can add regularization to my models
- [ ] I can implement custom loss functions
- [ ] I can interpret loss values during training

---

## 5. Optimization Algorithms

### Conceptual Understanding
- [ ] I understand batch vs mini-batch vs stochastic gradient descent
- [ ] I can explain the momentum concept
- [ ] I understand adaptive learning rates
- [ ] I know the differences between Adam, RMSprop, AdaGrad
- [ ] I understand learning rate scheduling

### Mathematical Foundations
- [ ] I can write update equations for SGD with momentum
- [ ] I can derive the Adam update rule
- [ ] I understand the exponential moving average
- [ ] I know the mathematical motivation for adaptive methods

### Practical Skills
- [ ] I can implement SGD with momentum from scratch
- [ ] I know how to choose appropriate optimizers
- [ ] I can tune learning rates effectively
- [ ] I can implement learning rate schedules
- [ ] I can diagnose optimization problems

---

## 6. Convolutional Neural Networks (CNNs)

### Conceptual Understanding
- [ ] I understand the motivation for convolutions
- [ ] I can explain parameter sharing and local connectivity
- [ ] I understand the role of pooling layers
- [ ] I know the difference between valid and same padding
- [ ] I understand receptive fields

### Mathematical Foundations
- [ ] I can compute output dimensions for conv layers
- [ ] I can calculate the number of parameters in a conv layer
- [ ] I understand the convolution operation mathematically
- [ ] I can compute receptive field sizes

### Practical Skills
- [ ] I can implement 2D convolution from scratch
- [ ] I can build CNNs using deep learning frameworks
- [ ] I know common CNN architectures (LeNet, AlexNet, VGG, ResNet)
- [ ] I can apply transfer learning with pretrained CNNs
- [ ] I can visualize learned filters and feature maps

---

## 7. Recurrent Neural Networks (RNNs)

### Conceptual Understanding
- [ ] I understand why RNNs are needed for sequences
- [ ] I can explain the concept of hidden state
- [ ] I understand the vanishing gradient problem in RNNs
- [ ] I know the difference between RNN variants (vanilla, LSTM, GRU)
- [ ] I understand bidirectional RNNs

### Mathematical Foundations
- [ ] I can write the equations for vanilla RNN
- [ ] I can write the equations for LSTM gates
- [ ] I understand backpropagation through time (BPTT)
- [ ] I can explain gradient flow in LSTM

### Practical Skills
- [ ] I can implement a simple RNN from scratch
- [ ] I can build LSTMs using frameworks
- [ ] I know when to use RNNs vs other architectures
- [ ] I can handle variable-length sequences
- [ ] I can implement sequence-to-sequence models

---

## 8. Transformers & Attention

### Conceptual Understanding
- [ ] I understand the attention mechanism
- [ ] I can explain self-attention
- [ ] I understand multi-head attention
- [ ] I know the architecture of the Transformer
- [ ] I understand positional encoding

### Mathematical Foundations
- [ ] I can write the equations for scaled dot-product attention
- [ ] I understand the query-key-value formulation
- [ ] I can compute attention scores mathematically
- [ ] I know the dimensions in multi-head attention

### Practical Skills
- [ ] I can implement attention from scratch
- [ ] I can use pretrained Transformers (BERT, GPT)
- [ ] I know when Transformers are better than RNNs
- [ ] I can fine-tune Transformer models
- [ ] I understand Vision Transformers (ViT)

---

## 9. Regularization Techniques

### Conceptual Understanding
- [ ] I understand overfitting and underfitting
- [ ] I can explain how dropout prevents overfitting
- [ ] I understand batch normalization and its benefits
- [ ] I know the difference between batch, layer, and instance norm
- [ ] I understand data augmentation

### Mathematical Foundations
- [ ] I can write the dropout operation mathematically
- [ ] I understand the statistics computed in batch norm
- [ ] I can derive the forward and backward pass of batch norm
- [ ] I understand how dropout changes during inference

### Practical Skills
- [ ] I can implement dropout from scratch
- [ ] I can add batch normalization to my networks
- [ ] I know where to place normalization layers
- [ ] I can implement data augmentation
- [ ] I can use early stopping effectively

---

## 10. Training Best Practices

### Conceptual Understanding
- [ ] I understand the bias-variance tradeoff
- [ ] I can explain learning rate warmup
- [ ] I understand gradient clipping
- [ ] I know about mixed precision training
- [ ] I understand the lottery ticket hypothesis

### Mathematical Foundations
- [ ] I understand different weight initialization schemes (Xavier, He)
- [ ] I know the mathematical motivation for batch normalization
- [ ] I can explain the mathematics of gradient clipping

### Practical Skills
- [ ] I can choose appropriate initialization
- [ ] I can implement gradient clipping
- [ ] I can use learning rate scheduling
- [ ] I can train using mixed precision
- [ ] I can diagnose training problems (loss not decreasing, exploding gradients, etc.)
- [ ] I can use TensorBoard or similar tools for monitoring

---

## 11. Model Evaluation & Debugging

### Conceptual Understanding
- [ ] I understand train/validation/test splits
- [ ] I can interpret learning curves
- [ ] I know how to diagnose overfitting and underfitting
- [ ] I understand the role of a validation set
- [ ] I can identify common failure modes

### Practical Skills
- [ ] I can properly split data for deep learning
- [ ] I can create and interpret learning curves
- [ ] I can use validation sets for hyperparameter tuning
- [ ] I can implement model checkpointing
- [ ] I can debug neural networks systematically

---

## Self-Assessment Summary

**Count your checks:**
- Total items: 115
- Items checked: _____ / 115
- Percentage: _____ %

**Readiness for Assessment:**
- 90-100%: Excellent, ready for exam
- 75-89%: Good, review weak areas
- 60-74%: Adequate, need focused study
- <60%: Need significant review

**Priority Areas to Study:**
(List topic sections with fewest checks)
1. _____________________
2. _____________________
3. _____________________

**Study Plan:**
- Date of next assessment: __________
- Study hours needed: __________
- Focus areas: __________

---

## Additional Resources

**If you need help with:**
- **Fundamentals:** Review slides 1-20, textbook chapters 1-3
- **Backpropagation:** Work through derivation in slides 25-35
- **CNNs:** Stanford CS231n lectures, implement from scratch
- **RNNs/LSTMs:** Colah's blog, Karpathy's char-rnn
- **Transformers:** "Attention is All You Need" paper, Illustrated Transformer
- **Practical skills:** Complete coding assignments, Kaggle tutorials

**Office Hours:** Schedule time if you have many unchecked items
**Study Group:** Find peers to work through difficult concepts

---

*Last Updated: January 2025*
*Part of the Academic Presentations Assessment Materials*
