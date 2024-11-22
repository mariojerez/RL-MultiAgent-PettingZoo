import pygame
import numpy as np
from switch_sides_v0 import env as create_env


def main(continuous_actions=False, num_agents=1, max_cycles=250):
    """
    Interactive control script with configurable options.
    :param continuous_actions: Whether to use continuous actions (True) or discrete actions (False).
    :param num_agents: Number of agents in the environment.
    :param max_cycles: Maximum number of steps in the environment.
    """
    # Initialize the environment
    env = create_env(render_mode="human", N=num_agents, max_cycles=max_cycles, continuous_actions=continuous_actions)
    observations, infos = env.reset(), None

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Robot Interactive Control")
    clock = pygame.time.Clock()

    if continuous_actions:
        # Define continuous action mapping
        max_linear_velocity = 2.0
        max_angular_velocity = 2.0
        action_mapping = {
            pygame.K_UP: [max_linear_velocity, 0.0],       # Move forward
            pygame.K_DOWN: [-max_linear_velocity, 0.0],    # Move backward
            pygame.K_LEFT: [0.0, max_angular_velocity],    # Turn left
            pygame.K_RIGHT: [0.0, -max_angular_velocity],  # Turn right
        }
        default_action = [0.0, 0.0]
    else:
        # Define discrete action mapping
        action_mapping = {
            pygame.K_UP: 1,    # Move forward
            pygame.K_DOWN: 2,  # Move backward
            pygame.K_LEFT: 3,  # Turn left
            pygame.K_RIGHT: 4  # Turn right
        }
        default_action = 0
    current_agent_index = 0
    current_agent = env.agents[current_agent_index]
    # Main control loop
    running = True
    while running and env.agents:
        # current_agent = env.agent_selection  # Get the current agent to act
        # action = 0 if not continuous_actions else [0.0, 0.0]  # Default: no action
        action = default_action 
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Switch to the next agent
                    current_agent_index = (current_agent_index + 1) % len(env.agents)
                    current_agent = env.agents[current_agent_index]
                    print(f"Switched to {env.agents[current_agent_index]}")


        # Check for key presses
        keys = pygame.key.get_pressed()
        for key, value in action_mapping.items():
            if keys[key]:
                action = value
                break  # Use the first matching key

        # Ensure the action is valid for the agent's action space
        action_space = env.action_space(current_agent)
        if continuous_actions:
            action = np.clip(action, action_space.low, action_space.high)
        else:
            assert action in range(action_space.n), f"Action {action} out of bounds!"

        # Debug: Print action for the current agent
        print(f"Agent: {current_agent}, Action: {action}")

        # Create action dictionary for step
        actions = {agent: default_action for agent in env.agents}  # Default actions
        actions[current_agent] = action  # Set action for the current agent only


        # Step the environment with the action for the current agent
        env.step(action)

        # Render the environment
        env.render()

        # Limit frame rate
        clock.tick(30)

    # Close the environment
    env.close()
    pygame.quit()


if __name__ == "__main__":
    # Let user choose the configuration
    # print("Choose action type:")
    # print("1. Discrete actions")
    # print("2. Continuous actions")
    # action_type = int
    # (input("Enter 1 or 2: "))
    continuous  = False

    num_agents = 3
    max_steps = 250

    main(continuous_actions=continuous, num_agents=num_agents, max_cycles=max_steps)
