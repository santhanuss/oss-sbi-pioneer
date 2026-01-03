import random
import time

def monitor_traffic(service_name):
    """
    Simulate SBI traffic metrics.
    """
    return {
        "service": service_name,
        "latency_ms": random.randint(20, 300),
        "error_count": random.choice([0, 0, 1, 2]),
        "timestamp": int(time.time())
    }
