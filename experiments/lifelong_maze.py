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
    env_distribution = make_env_distribution(env_class='maze', n_env=10, gamma=GAMMA, w=5, h=5)
    actions = env_distribution.get_actions()

    epsilon = .1
    delta = .05
    m_r = np.log(2. / delta) / (2. * epsilon ** 2)
    m_t = 2. * (np.log(2**(24. - 2.)) - np.log(delta)) / (epsilon**2)
    m = int(max(m_r, m_t))
    print(m)
    exit()

    max_mem = 4
    rmax = RMax(actions=actions, gamma=GAMMA, count_threshold=m)
    lrmax0_2 = LRMaxCT(actions=actions, gamma=GAMMA, count_threshold=m, max_memory_size=max_mem, prior=0.2)
    lrmax0_6 = LRMaxCT(actions=actions, gamma=GAMMA, count_threshold=m, max_memory_size=max_mem, prior=0.6)
    lrmax1_0 = LRMaxCT(actions=actions, gamma=GAMMA, count_threshold=m, max_memory_size=max_mem, prior=1.0)

    agents_pool = [rmax, lrmax0_2, lrmax0_6, lrmax1_0]

    run_agents_lifelong(
        agents_pool, env_distribution, samples=30, episodes=30, steps=10,
        reset_at_terminal=False, open_plot=True, cumulative_plot=False, is_tracked_value_discounted=False
    )


if __name__ == '__main__':
    np.random.seed(1993)
    experiment()
