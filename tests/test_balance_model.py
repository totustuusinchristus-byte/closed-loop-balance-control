import numpy as np
from src.balance_model import simulate_balance, response_metrics

def test_simulation_schema_and_finite_values():
    df=simulate_balance(duration=3.0,seed=1)
    assert {"time_s","angle_deg","control_torque_Nm","external_torque_Nm"} <= set(df.columns)
    assert np.isfinite(df.select_dtypes("number").to_numpy()).all()

def test_reproducible_with_seed():
    a=simulate_balance(duration=3.0,seed=3)
    b=simulate_balance(duration=3.0,seed=3)
    assert np.allclose(a["angle_rad"],b["angle_rad"])

def test_response_metrics_nonnegative():
    out=response_metrics(simulate_balance(duration=4.0,seed=2))
    assert all(v>=0 for v in out.values())
