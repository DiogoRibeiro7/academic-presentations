# Reinforcement Learning

**From Markov Decision Processes to Deep RL**

## 📚 Overview

This presentation provides comprehensive coverage of reinforcement learning (RL), from foundational theory to state-of-the-art deep RL algorithms. The material is designed for graduate-level courses and assumes familiarity with probability, linear algebra, and Python programming.

## 🎯 Learning Objectives

By the end of this module, students will be able to:

1. **RL Foundations**
   - Formulate problems as Markov Decision Processes (MDPs)
   - Derive and apply Bellman equations
   - Understand value functions and optimal policies
   - Analyze MDP properties (stationarity, Markov property)

2. **Dynamic Programming**
   - Implement value iteration algorithm
   - Implement policy iteration algorithm
   - Understand convergence guarantees
   - Apply DP to solve small MDPs

3. **Model-Free Methods**
   - Implement Monte Carlo methods (first-visit, every-visit)
   - Apply Temporal Difference (TD) learning
   - Build Q-learning agents
   - Implement SARSA and Expected SARSA
   - Understand on-policy vs off-policy learning

4. **Function Approximation**
   - Apply linear function approximation
   - Use neural networks as function approximators
   - Implement Deep Q-Networks (DQN)
   - Understand experience replay and target networks
   - Handle continuous action spaces

5. **Policy Gradient Methods**
   - Derive policy gradient theorem
   - Implement REINFORCE algorithm
   - Build Actor-Critic architectures
   - Apply Proximal Policy Optimization (PPO)
   - Implement Trust Region Policy Optimization (TRPO)

6. **Advanced Topics**
   - Design multi-agent RL systems
   - Apply inverse RL and imitation learning
   - Implement model-based RL
   - Understand meta-RL and transfer learning

## 📋 Topics Covered

### Part 1: Foundations

**Markov Decision Processes**
- States, actions, rewards, transitions
- Markov property and stationarity
- Discounted vs average reward
- Episodic vs continuing tasks

**Bellman Equations**
- Value functions (V and Q functions)
- Bellman expectation equations
- Bellman optimality equations
- Policy evaluation and improvement

### Part 2: Dynamic Programming

**Value Iteration**
- Algorithm derivation
- Convergence guarantees
- Computational complexity
- Asynchronous DP

**Policy Iteration**
- Policy evaluation step
- Policy improvement step
- Modified policy iteration
- Comparison with value iteration

**Generalized Policy Iteration**
- Interleaving evaluation and improvement
- Truncated policy iteration
- Approximate policy iteration

### Part 3: Monte Carlo Methods

**Prediction**
- First-visit MC
- Every-visit MC
- Incremental implementation
- Variance reduction

**Control**
- Monte Carlo ES (exploring starts)
- On-policy MC control
- Off-policy MC with importance sampling
- Weighted importance sampling

### Part 4: Temporal Difference Learning

**TD Prediction**
- TD(0) algorithm
- Bias-variance tradeoff
- Batch updating
- Certainty equivalence

**TD Control**
- SARSA (on-policy TD control)
- Q-learning (off-policy TD control)
- Expected SARSA
- Double Q-learning

**n-step Methods**
- n-step TD
- n-step SARSA
- TD(λ) and eligibility traces
- Forward vs backward view

### Part 5: Function Approximation

**Linear Methods**
- Feature construction
- Gradient descent for prediction
- Semi-gradient methods for control
- Deadly triad

**Deep Q-Networks (DQN)**
- Neural network Q-functions
- Experience replay
- Target networks
- Double DQN
- Dueling DQN
- Prioritized experience replay
- Rainbow DQN

**Continuous Actions**
- Deep Deterministic Policy Gradient (DDPG)
- Twin Delayed DDPG (TD3)
- Soft Actor-Critic (SAC)

### Part 6: Policy Gradient Methods

**REINFORCE**
- Score function estimator
- Monte Carlo policy gradient
- Baseline for variance reduction
- Entropy regularization

**Actor-Critic**
- Advantage Actor-Critic (A2C)
- Asynchronous Advantage Actor-Critic (A3C)
- Generalized Advantage Estimation (GAE)
- Natural policy gradients

**Advanced Policy Optimization**
- Trust Region Policy Optimization (TRPO)
- Proximal Policy Optimization (PPO)
- PPO-Clip and PPO-Penalty
- Sample efficiency considerations

### Part 7: Advanced Topics

**Multi-Agent RL**
- Nash equilibria
- Cooperative vs competitive settings
- Multi-agent actor-critic
- Emergent behavior

**Model-Based RL**
- Dyna architecture
- Learned world models
- Planning with learned models
- AlphaZero and MuZero

**Imitation Learning**
- Behavioral cloning
- Inverse reinforcement learning
- Generative adversarial imitation learning (GAIL)
- Learning from demonstrations

**Meta-Learning & Transfer**
- Multi-task RL
- Transfer learning across tasks
- Meta-RL (learning to learn)
- Few-shot RL

## 📖 Prerequisites

**Required:**
- Probability theory (conditional probability, expectations)
- Linear algebra (matrices, eigenvalues)
- Python programming
- Basic calculus

**Recommended:**
- Dynamic programming basics
- Machine learning fundamentals
- Deep learning basics (for deep RL)
- Control theory (helpful but not required)

## 🛠️ Technical Requirements

### Software
```bash
# Core RL libraries
pip install gymnasium  # OpenAI Gym successor
pip install stable-baselines3  # RL algorithms
pip install tianshou  # Deep RL library

# Deep learning
pip install torch torchvision
pip install tensorflow  # Alternative

# Classic environments
pip install gymnasium[classic-control]
pip install gymnasium[box2d]
pip install gymnasium[atari]

# Additional tools
pip install numpy scipy matplotlib
pip install pandas seaborn
pip install tensorboard  # Training visualization
```

### Environments
```python
# Install popular RL environments
pip install pybullet  # Robotics
pip install dm-control  # DeepMind Control Suite
pip install procgen  # Procedural generation
pip install minigrid  # Grid world environments
```

## 📝 Materials

### Presentation
- **File:** `rl_beamer.tex`
- **Compile:** `pdflatex rl_beamer.tex` (run twice)
- **Format:** Beamer slides with aspect ratio 16:9

### Code Examples
Code implementations available in:
- `../code/reinforcement_learning/` (when created)

### Exercises
Practice problems available in:
- `../exercises/reinforcement_learning/` (when created)

## 📚 Recommended References

### Textbooks

1. **Reinforcement Learning: An Introduction** - Sutton & Barto (2018)
   - The definitive RL textbook
   - Free online: http://incompleteideas.net/book/the-book-2nd.html

2. **Algorithms for Reinforcement Learning** - Szepesvári (2010)
   - Concise mathematical treatment
   - Excellent for theory

3. **Deep Reinforcement Learning** - Plaat (2022)
   - Modern deep RL methods
   - Practical implementation focus

### Research Papers

**Foundations:**
- Watkins & Dayan (1992) - "Q-learning"
- Rummery & Niranjan (1994) - "On-line Q-learning using connectionist systems"

**Deep RL Breakthroughs:**
- Mnih et al. (2015) - "Human-level control through deep RL (DQN)"
- Silver et al. (2016) - "Mastering the game of Go with deep RL (AlphaGo)"
- Schulman et al. (2017) - "Proximal policy optimization (PPO)"
- Haarnoja et al. (2018) - "Soft actor-critic (SAC)"
- Schrittwieser et al. (2020) - "MuZero"

**Policy Gradients:**
- Williams (1992) - "Simple statistical gradient-following (REINFORCE)"
- Sutton et al. (2000) - "Policy gradient methods"
- Schulman et al. (2015) - "Trust region policy optimization (TRPO)"
- Mnih et al. (2016) - "Asynchronous methods for deep RL (A3C)"

**Multi-Agent:**
- Lowe et al. (2017) - "Multi-agent actor-critic for mixed cooperative-competitive"
- Foerster et al. (2018) - "Counterfactual multi-agent policy gradients"

**Model-Based:**
- Sutton (1991) - "Dyna, an integrated architecture"
- Kaiser et al. (2020) - "Model-based RL for Atari"

### Online Resources
- **CS 285** (UC Berkeley) - Deep Reinforcement Learning
- **Spinning Up** (OpenAI) - https://spinningup.openai.com/
- **Stable Baselines3 Docs** - https://stable-baselines3.readthedocs.io/
- **Gymnasium Docs** - https://gymnasium.farama.org/

## 🎓 Assessment

Students will be evaluated on:

1. **Problem Sets (40%)**
   - Implement value iteration and policy iteration
   - Build Q-learning agent for GridWorld
   - Implement DQN for Atari games
   - Code PPO for continuous control

2. **Quizzes (20%)**
   - MDP formulation
   - Bellman equations
   - Algorithm comparison
   - Hyperparameter selection

3. **Final Project (40%)**
   - Solve complex RL problem
   - Compare multiple algorithms
   - Analyze learning curves
   - Write technical report

See `../assessments/` for detailed rubrics and evaluation criteria.

## 💡 Study Tips

1. **Master the Theory**
   - Derive Bellman equations
   - Prove convergence for simple cases
   - Understand bias-variance tradeoffs

2. **Start Simple**
   - Implement tabular methods first
   - Test on small environments (GridWorld)
   - Verify correctness before scaling

3. **Debug Systematically**
   - Plot learning curves
   - Visualize learned policies
   - Check gradient magnitudes
   - Use smaller networks initially

4. **Experiment Methodically**
   - Vary one hyperparameter at a time
   - Run multiple seeds
   - Use TensorBoard for tracking
   - Document experiments

5. **Read Classic Papers**
   - Start with Sutton & Barto chapters
   - Read DQN, A3C, PPO papers
   - Implement key ideas from papers
   - Compare your results to papers

## 🔗 Related Topics

- **Prerequisites:** Probability, Dynamic Programming, Machine Learning
- **Follow-up:** Robotics, Game AI, Control Systems
- **Complementary:** Optimization, Deep Learning, Causal Inference
- **Applications:** Robotics, Games, Resource Allocation, Finance

## 🎮 Common RL Environments

### Classic Control
- **CartPole** - Balance pole on cart
- **MountainCar** - Drive car up hill
- **Pendulum** - Swing up inverted pendulum
- **Acrobot** - Two-link robot

### Robotics
- **Fetch** - Robotic manipulation
- **Shadow Hand** - Dexterous manipulation
- **Humanoid** - Bipedal locomotion

### Games
- **Atari** - Classic Atari 2600 games
- **MuJoCo** - Continuous control
- **ProcGen** - Procedural environments

### Grid Worlds
- **FrozenLake** - Navigate icy grid
- **Taxi** - Pick up and drop off passengers
- **MiniGrid** - Various grid-world tasks

## ⚠️ Common Pitfalls

1. **Reward Shaping** - Can introduce unintended behavior
2. **Exploration** - Insufficient exploration leads to local optima
3. **Credit Assignment** - Long-term dependencies are difficult
4. **Hyperparameters** - RL is very sensitive to hyperparameters
5. **Reproducibility** - Random seeds and environment versions matter
6. **Deadly Triad** - Function approximation + bootstrapping + off-policy

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
