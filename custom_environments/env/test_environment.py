from tunnel_navigation import CustomActionMaskedEnvironment

from pettingzoo.test import parallel_api_test


if __name__ == "__main__":
    env = CustomActionMaskedEnvironment()
    env.reset()
    env.render()
    parallel_api_test(env, num_cycles=1_000_000)