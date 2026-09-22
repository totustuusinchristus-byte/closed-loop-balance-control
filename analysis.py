"""Run baseline and feedback-delay experiments for the balance model."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from src.balance_model import simulate_balance,response_metrics

Path("figures").mkdir(exist_ok=True); Path("data").mkdir(exist_ok=True)
base=simulate_balance()
pd.DataFrame([response_metrics(base)]).to_csv("data/baseline_metrics.csv",index=False)
plt.figure(figsize=(9,4)); plt.plot(base.time_s,base.angle_deg); plt.axvline(2,ls="--")
plt.xlabel("Time (s)"); plt.ylabel("Body angle (deg)"); plt.tight_layout()
plt.savefig("figures/baseline_response.png",dpi=160); plt.close()

rows=[]
plt.figure(figsize=(9,4))
for delay in [0,.05,.10,.15,.20]:
    sim=simulate_balance(sensory_delay=delay); rows.append({"delay_s":delay,**response_metrics(sim)})
    plt.plot(sim.time_s,sim.angle_deg,label=f"{int(delay*1000)} ms")
pd.DataFrame(rows).to_csv("data/delay_sweep.csv",index=False)
plt.xlabel("Time (s)"); plt.ylabel("Body angle (deg)"); plt.legend(); plt.tight_layout()
plt.savefig("figures/delay_comparison.png",dpi=160); plt.close()
print(pd.DataFrame(rows))
