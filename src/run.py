from sbi_discovery import discover_services
from traffic_monitor import monitor_traffic
from security_checks import run_security_checks
from oss_metrics import generate_oss_report

def main():
    services = discover_services()
    results = []

    for svc in services:
        traffic = monitor_traffic(svc["name"])
        security = run_security_checks(svc)

        results.append({
            "service": svc["name"],
            "endpoint": svc["endpoint"],
            "traffic": traffic,
            "security_findings": security
        })

    generate_oss_report(results)

if __name__ == "__main__":
    main()
