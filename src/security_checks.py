def run_security_checks(service):
    """
    Perform basic security posture checks on SBI services.
    """
    findings = []

    if not service.get("auth_enabled"):
        findings.append("AUTH_MISSING")

    if not service.get("tls_enabled"):
        findings.append("TLS_NOT_ENABLED")

    if service.get("endpoint", "").startswith("http://"):
        findings.append("INSECURE_PROTOCOL")

    if not findings:
        findings.append("SECURE")

    return findings
