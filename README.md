# Closed-Loop Balance Control Simulation in Python

An educational computational project linking simplified postural mechanics, sensory feedback and corrective control.

## Model
The body is represented as a linearized single-link inverted pendulum about the ankle. A proportional-derivative (PD) controller uses delayed, noisy estimates of body angle and angular velocity to generate corrective torque following an external perturbation.

## What this project demonstrates
- numerical simulation of a dynamical system;
- feedback-control logic;
- sensory delay/noise as explicit model parameters;
- perturbation-response analysis;
- parameter sweeps and stability reasoning;
- reproducible Python code.

## Scope
This is not a validated model of human postural control, a vestibular model, a motor-unit model, or a physical robotics controller. It is a learning bridge toward closed-loop and human-in-the-loop reasoning.

## Portfolio progression
1. EMG signal analysis — physiological signal processing.
2. Postural sway analysis — quantitative whole-body balance analysis.
3. Closed-loop balance control — computational modelling and feedback-control concepts.

## Learning goals
Complete parameter sweeps and explain why upright stance is mechanically unstable in this model, what proportional and derivative feedback contribute, why delay can destabilize feedback, and why increasing gain is not automatically better.

## Research integrity
This repository documents introductory computational modelling. It does not claim robotics-hardware experience or experimental validation.