# Project report

## Learning algorithm

The learning algorithm used is vanilla Deep Q Learning as described in original paper. As an input the vector of state is used instead of an image so convolutional neural nework is replaced with deep neural network. The deep neural network has following layers:

- Fully connected layer - input: 37 (state size) output: 128
- Fully connected layer - input: 128 output 64
- Fully connected layer - input: 64 output: (action size)

Parameters used in DQN algorithm:

- Maximum steps per episode: 1000
- Starting epsilion: 1.0
- Ending epsilion: 0.01
- Epsilion decay rate: 0.999

## Results

![results](images/plot.png)

```
Episode 100	Average Score: 0.33
Episode 200	Average Score: 0.92
Episode 300	Average Score: 1.63
Episode 400	Average Score: 2.27
Episode 500	Average Score: 3.22
Episode 600	Average Score: 4.37
Episode 700	Average Score: 5.34
Episode 800	Average Score: 6.44
Episode 900	Average Score: 6.81
Episode 1000	Average Score: 7.87
Episode 1100	Average Score: 8.06
Episode 1200	Average Score: 8.28
Episode 1300	Average Score: 9.60
Episode 1400	Average Score: 10.64
Episode 1500	Average Score: 10.78
Episode 1600	Average Score: 10.78
Episode 1700	Average Score: 10.68
Episode 1800	Average Score: 11.74
Episode 1900	Average Score: 11.60
Episode 2000	Average Score: 11.88
Episode 2100	Average Score: 12.44
Episode 2165	Average Score: 13.00\Environment solved in 2065 episodes!	Average Score: 13.00
```

### Untrained agent

![untrained](images/untrained.gif)

### Trained agent

![trained](images/trained.gif)

## Ideas for future work

1. Extensive hyperparameter optimization
2. Double Deep Q Networks
3. Prioritized Experience Replay
4. Dueling Deep Q Networks
5. RAINBOW Paper
6. Learning from pixels