import switch_sides_v0
import numpy as np

masks = {}
buffer = 20 #cm
env = switch_sides_v0.parallel_env(render_mode="human")
observations, infos = env.reset()
env.render()

while env.agents:
    # insert policy here

    # Prevent agents from leaving environment boundaries
    masks = {}
    for agent in observations:
        # Agent observations: `[self_vel, self_pos, landmark_rel_positions, other_agent_rel_positions, communication]`
        x_pos, y_pos = observations[agent][2], observations[agent][3]
        masks[agent] = np.array([1,
                       1 if x_pos > buffer else 0,
                       1 if x_pos < env.aec_env.length - buffer else 0,
                       1 if y_pos < env.aec_env.width - buffer else 0,
                       1 if y_pos > 0 + buffer else 0], dtype=np.int8)
    
    # Agent action space: `[no_action, move_left, move_right, move_down, move_up]`
    actions = {agent: env.action_space(agent).sample(mask=masks[agent]) for agent in env.agents}

    observations, rewards, terminations, truncations, infos = env.step(actions)
env.close()