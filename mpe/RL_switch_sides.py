import switch_sides_v0
import numpy as np
import gymnasium as gym  # Ensure Gymnasium is imported
from gymnasium.spaces import Discrete

# Initialize the environment
env = switch_sides_v0.parallel_env(render_mode="human")
observations, infos = env.reset()
env.render()

# Define the action effects
action_effects = {
    0: (0, 0),   # Stay
    1: (0, 1),   # Move Up
    2: (0, -1),  # Move Down
    3: (-1, 0),  # Move Left
    4: (1, 0),   # Move Right
}

while env.agents:
    actions = {}

    

    for agent in env.agents:
        # Retrieve the agent's current position from observations
        # Assuming observation[0] is x and observation[1] is y
        agent_observation = observations.get(agent)
    

        current_x = agent_observation[0]
        current_y = agent_observation[1]

        # Initialize mask with all actions allowed
        mask = np.ones(5, dtype=np.int8)  # Assuming 5 possible actions (0 to 4)

        # Determine which actions would keep the agent within bounds
        for action, (dx, dy) in action_effects.items():
            new_x = current_x + dx
            new_y = current_y + dy
            if not (-1 <= new_x <= 1 and -1 <= new_y <= 1):
                mask[action] = 0  # Disallow this action

        # Create a Discrete action space instance for masking
        action_space = env.action_space(agent)
        if isinstance(action_space, Discrete):
            try:
                # Sample an action with the mask
                action = action_space.sample(mask=mask)
                actions[agent] = action
            except Exception as e:
                print(f"Error sampling action for {agent}: {e}")
                # Fallback to a default action (e.g., Stay)
                actions[agent] = 0
        else:
            raise TypeError(f"Unsupported action space type for {agent}: {type(action_space)}")

    # Take a step in the environment with the masked actions
    observations, rewards, terminations, truncations, infos = env.step(actions)
    env.render()

env.close()
