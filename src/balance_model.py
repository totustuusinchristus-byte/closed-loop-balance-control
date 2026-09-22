"""Educational closed-loop standing-balance simulation."""
import numpy as np
import pandas as pd

def simulate_balance(duration=12.0, dt=0.002, mass=75.0, com_height=1.0,
                     inertia=None, gravity=9.81, kp=900.0, kd=260.0,
                     sensory_delay=0.10, angle_noise_sd=0.0008,
                     velocity_noise_sd=0.004, perturbation_time=2.0,
                     perturbation_torque=35.0, perturbation_duration=0.08,
                     seed=7):
    if inertia is None:
        inertia = mass * com_height**2
    n = int(duration / dt) + 1
    t = np.arange(n) * dt
    theta = np.zeros(n); omega = np.zeros(n)
    tau_control = np.zeros(n); tau_external = np.zeros(n)
    rng = np.random.default_rng(seed)
    delay_steps = max(0, int(round(sensory_delay / dt)))
    p0 = int(round(perturbation_time / dt))
    p1 = min(n, p0 + int(round(perturbation_duration / dt)))
    tau_external[p0:p1] = perturbation_torque
    for i in range(n - 1):
        j = max(0, i - delay_steps)
        theta_est = theta[j] + rng.normal(0, angle_noise_sd)
        omega_est = omega[j] + rng.normal(0, velocity_noise_sd)
        tau_control[i] = -kp * theta_est - kd * omega_est
        alpha = (mass*gravity*com_height*theta[i] + tau_control[i] + tau_external[i]) / inertia
        omega[i+1] = omega[i] + alpha*dt
        theta[i+1] = theta[i] + omega[i+1]*dt
    tau_control[-1] = tau_control[-2]
    return pd.DataFrame({"time_s":t,"angle_rad":theta,"angle_deg":np.degrees(theta),
                         "angular_velocity_rad_s":omega,"control_torque_Nm":tau_control,
                         "external_torque_Nm":tau_external})

def response_metrics(df, perturbation_time=2.0):
    post = df[df["time_s"] >= perturbation_time]
    return {
        "peak_abs_angle_deg": float(post["angle_deg"].abs().max()),
        "post_perturbation_rms_angle_deg": float(np.sqrt(np.mean(post["angle_deg"]**2))),
        "integrated_squared_control_effort": float(np.trapz(post["control_torque_Nm"]**2, post["time_s"]))
    }
