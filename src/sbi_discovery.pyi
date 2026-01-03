import yaml

def load_sbi_services(config_path="configs/sbi_services.yaml"):
    """
    Load SBI services from YAML config.
    Acts as OSS inventory source.
    """
    try:
        with open(config_path, "r") as f:
            data = yaml.safe_load(f)
            return data.get("services", [])
    except Exception as e:
        print(f"[ERROR] Failed to load SBI services: {e}")
        return []

def discover_services():
    services = load_sbi_services()
    inventory = []

    for svc in services:
        inventory.append({
            "name": svc.get("name"),
            "endpoint": svc.get("endpoint"),
            "auth_enabled": svc.get("auth", False),
            "tls_enabled": svc.get("tls", False)
        })

    return inventory

if __name__ == "__main__":
    services = discover_services()
    print("📡 SBI Service Inventory")
    for s in services:
        print(f"- {s['name']} | Auth={s['auth_enabled']} | TLS={s['tls_enabled']}")
