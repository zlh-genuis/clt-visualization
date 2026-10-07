# CLT Visualization

This project uses a simple Python simulation to illustrate the Central Limit Theorem.

The population distribution is exponential, which is right-skewed. For each sample size (`n = 5`, `30`, and `100`), the program repeatedly draws samples and calculates their means. The histograms show that the distribution of the sample mean becomes more normal as the sample size increases.

## Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Run the simulation

```bash
python3 clt_simulation.py
```

Running the script displays the chart and saves it as `clt_visualization.png` in the project root. As the sample size increases, the distribution of sample means becomes more similar to a normal distribution.
