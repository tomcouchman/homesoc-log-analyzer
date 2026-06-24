import re
from collections import defaultdict


LOG_FILE = "data/sample_auth.log"
REPORT_FILE = "reports/security_report.txt"
FAILED_LOGIN_THRESHOLD = 5


def extract_failed_login_ip(log_line):
    """
    Extract the source IP address from a failed SSH login line.
    """

    if "Failed password" not in log_line:
        return None

    ip_pattern = r"from (\d+\.\d+\.\d+\.\d+)"
    match = re.search(ip_pattern, log_line)

    if match:
        return match.group(1)

    return None


def analyze_failed_logins(file_path):
    """
    Read a log file and count failed login attempts by IP address.
    """

    failed_login_counts = defaultdict(int)

    with open(file_path, "r") as file:
        for line in file:
            ip_address = extract_failed_login_ip(line)

            if ip_address:
                failed_login_counts[ip_address] += 1

    return failed_login_counts


def get_risk_level(failed_attempts):
    """
    Assign a risk level based on the number of failed login attempts.
    """

    if failed_attempts >= 10:
        return "HIGH"
    elif failed_attempts >= FAILED_LOGIN_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"


def generate_report(failed_login_counts):
    """
    Generate a security report and return it as text.
    """

    report_lines = []

    report_lines.append("HomeSOC Log Analyzer Report")
    report_lines.append("===========================")

    suspicious_activity_found = False

    for ip_address, failed_attempts in failed_login_counts.items():
        if failed_attempts >= FAILED_LOGIN_THRESHOLD:
            suspicious_activity_found = True
            risk_level = get_risk_level(failed_attempts)

            report_lines.append("")
            report_lines.append(f"[{risk_level}] Suspicious login activity detected")
            report_lines.append(f"IP Address: {ip_address}")
            report_lines.append(f"Failed login attempts: {failed_attempts}")
            report_lines.append("Reason: Multiple failed SSH login attempts from the same IP address.")

    if not suspicious_activity_found:
        report_lines.append("")
        report_lines.append("No suspicious login activity detected.")

    return "\n".join(report_lines)


def save_report(report_text, output_file):
    """
    Save the report to a text file.
    """

    with open(output_file, "w") as file:
        file.write(report_text)


def main():
    failed_login_counts = analyze_failed_logins(LOG_FILE)
    report_text = generate_report(failed_login_counts)

    print(report_text)

    save_report(report_text, REPORT_FILE)
    print(f"\nReport saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()