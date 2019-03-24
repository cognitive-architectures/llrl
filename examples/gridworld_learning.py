from simple_rl.agents import QLearningAgent, RandomAgent
from simple_rl.tasks import GridWorldMDP
from simple_rl.run_experiments import run_agents_on_mdp
from llrl.agents.rmax import RMax


def main():
    # Setup MDP.
    mdp = GridWorldMDP(width=6, height=6, init_loc=(1, 1), goal_locs=[(6, 6)])

    # Setup Agents.
    ql_agent = QLearningAgent(actions=mdp.get_actions())
    rand_agent = RandomAgent(actions=mdp.get_actions())
    rmax_agent = RMax(actions=mdp.get_actions(), gamma=.9, horizon=3, count_threshold=1)

    # Run experiment and make plot.
    run_agents_on_mdp([rmax_agent, ql_agent, rand_agent], mdp, instances=10,
                      episodes=100, steps=20, reset_at_terminal=True, verbose=False)


if __name__ == "__main__":
    main()