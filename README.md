# Closed-Loop Balance Control Simulation in Python

An educational computational model linking simplified postural mechanics, delayed sensory feedback and corrective control.

## Scientific question
How do feedback gains and sensory delay influence the response of a simplified upright-body model to a brief perturbation?

## Model
The body is represented as a linearized single-link inverted pendulum about the ankle:

`I θ¨ = mgh θ + τ_control + τ_external`

A proportional-derivative controller generates corrective torque from delayed, noisy estimates of body angle and angular velocity:

`τ_control = -Kp θ_est - Kd ω_est`

## Reproduce
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python analysis.py
pytest -q
```

The analysis saves baseline response metrics and a sensory-delay sweep.

## Repository structure
- `src/balance_model.py` — simulation and response metrics.
- `analysis.py` — baseline and delay experiments.
- `data/baseline_metrics.csv` — baseline summary.
- `tests/` — reproducibility and numerical checks.
- `LEARNING_GUIDE.md` — concepts and parameter exercises.
- `.github/workflows/` — automated Python checks.

## Skills demonstrated
Python, NumPy, pandas, numerical simulation, feedback-control concepts, parameter sweeps, reproducibility and basic testing.

## Interpretation and limitations
This is a deliberately simplified educational model. It is not a validated human postural-control model, vestibular model, motor-unit model, neural decoder, ROS2 controller or robotics-hardware implementation. Its purpose is to build transparent foundations for reasoning about feedback, delay, perturbations and stability.

## Development goals
Complete Kp/Kd sensitivity maps, identify stable/unstable parameter regions and document how physiological measurements could inform a richer model.
