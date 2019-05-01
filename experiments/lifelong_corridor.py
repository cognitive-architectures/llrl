"""
Lifelong RL experiment in constant transition function setting
"""

import numpy as np

from llrl.agents.rmax import RMax
from llrl.agents.lrmax_ct import LRMaxCT
from llrl.utils.env_handler import make_env_distribution
from llrl.experiments_maker import run_agents_lifelong


GAMMA = .9


def experiment():
    env_distribution = make_env_distribution(env_class='corridor', n_env=10, gamma=GAMMA, w=20, h=1)
    actions = env_distribution.get_actions()

    m = 1
    max_mem = 2
    rmax = RMax(actions=actions, gamma=GAMMA, count_threshold=m)
    lrmax0_2 = LRMaxCT(actions=actions, gamma=GAMMA, count_threshold=m, max_memory_size=max_mem, prior=0.2)
    lrmax0_6 = LRMaxCT(actions=actions, gamma=GAMMA, count_threshold=m, max_memory_size=max_mem, prior=0.6)
    lrmax1_0 = LRMaxCT(actions=actions, gamma=GAMMA, count_threshold=m, max_memory_size=max_mem, prior=1.0)

    agents_pool = [rmax, lrmax0_2, lrmax0_6, lrmax1_0]

    run_agents_lifelong(
        agents_pool, env_distribution, samples=50, episodes=50, steps=10, reset_at_terminal=False,
        open_plot=True, cumulative_plot=False, is_tracked_value_discounted=True, plot_only=False
    )


if __name__ == '__main__':
    np.random.seed(1993)
    experiment()