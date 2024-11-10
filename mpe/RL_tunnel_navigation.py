# from pettingzoo.mpe import simple_spread_v3

import tunnel_navigation_v0

env = tunnel_navigation_v0.parallel_env(render_mode="human") # uses parallel API so that all agents move at the same time
observations, infos = env.reset()

while env.agents:
    # this is where you would insert your policy
    actions = {agent: env.action_space(agent).sample() for agent in env.agents}

    observations, rewards, terminations, truncations, infos = env.step(actions)
env.close()
