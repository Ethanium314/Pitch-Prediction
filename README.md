# Pitch-Prediction
SENG 474 Project - Realtime baseball pitch prediction

The purpose of this project is to create a model that can accurately predict the next pitch thrown in a game of baseball, between fastball and offspeed. We pull data from 3 levels of baseball: MLB, College, and the team of one of our members.

## Prediction Model

We will be using a neural network with the following parameters:

TODO: List parameters

Inputs:

- Hitter vs. Pitchers count metric (TODO: Define how this is calculated)
- Outs metric (0 if 0 outs, 0.5 if 1 out, 1 if 2 outs)
- 1st base occupied
- 2nd base occupied
- 3rd base occupied
- Catcher pitch metric (TODO: Define how this is calculated, metric of which pitch they prefer)
- Pitcher pitch metric (TODO: Define how this is calculated, metric of which pitch they prefer)
- Hitter threat metric (TODO: Define how this is calculated, matric of how much a hitter is perceived as a threat)
- Last pitch type
- Last pitch outcome (Strike, ball, or neither (new AB))

(Note: Could also do this with clustering of pitchers and/or catchers and/or hitters)

Output:

- Confidence of fastball or offspeed