"""
Comparison of the bounds provided by R-MAX and Lipschitz-R-Max.
"""

from llrl.envs.twostates import TwoStates
from llrl.agents.lrmax import LRMax
from llrl.agents.rmax import RMax
from llrl.agents.rmax_vi import RMaxVI
from simple_rl.agents import RandomAgent
from simple_rl.run_experiments import run_agents_on_mdp


def test(agent):
    Q = agent.Q_memory[0]
    for s in Q:
        for a in Q[s]:
            print('Q', s, a, Q[s][a])


def main():
    # MDP
    mdp1 = TwoStates(rewards=(0., 1.), proba=(0., 0.))
    # mdp2 = TwoStates(rewards=(0., 1.), proba=(.9, .9))

    # Agents
    rand_agent = RandomAgent(actions=mdp1.get_actions())
    rmax_agent = RMax(actions=mdp1.get_actions(), gamma=.9, horizon=3, count_threshold=20)
    rmax_vi_agent = RMaxVI(actions=mdp1.get_actions(), gamma=.9, horizon=3, count_threshold=20)
    lrmax_agent = LRMax(actions=mdp1.get_actions(), gamma=0.9, horizon=3, count_threshold=20)

    # Run
    run_agents_on_mdp([rmax_vi_agent, rmax_agent, rand_agent], mdp1, instances=5, episodes=10, steps=40,
                      reset_at_terminal=True, verbose=False)
    test(lrmax_agent)


if __name__ == "__main__":
    main()
