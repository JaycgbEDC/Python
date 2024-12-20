from environs import Env


env = Env()
env.read_env()


TIMEOUT = env.int("TIMEOUT", 10)
REDIS_HOST = env.str("REDIS_HOST", "localhost")
REDIS_PORT = env.int("REDIS_PORT", 6379)
REDIS_PASSWORD = env.str("REDIS_PASSWORD", None)
REDIS_KEY = env.str("REDIS_KEY", "antispider5")
PROXY_POOL_URL = env.str("PROXY_POOL_URL", "http://127.0.0.1:5555/random")
VALID_STATUSES = env.list("VALID_STATUSES", [200])
MAX_FAILED_TIME = env.int("MAX_FAILED TIME", 20)