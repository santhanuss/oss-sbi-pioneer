import json
import os
from datetime import datetime

# Resolve project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "outputs", "sample_report.json")

def generate_oss_report(results):
    report = {
        "generated_at": datetime.utcnow().isoformat(),
        "total_services": len(results),
        "services": results
    }

    # Ensure outputs directory exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(report, f, indent=4)

    print(f"📊 OSS report generated at {OUTPUT_PATH}")
