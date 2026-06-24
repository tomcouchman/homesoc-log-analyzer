# HomeSOC Log Analyzer

HomeSOC Log Analyzer is a beginner-friendly Python cybersecurity project that analyzes SSH authentication logs and detects suspicious login behaviour.

## Project overview

This tool reads a Linux-style authentication log file and identifies IP addresses with repeated failed login attempts. It then assigns a basic risk level and generates a security report.

The project was built to practise practical blue-team cybersecurity skills, including log analysis, detection logic, risk scoring, and incident-style reporting.

## Current features

- Reads a sample SSH authentication log
- Detects repeated failed login attempts
- Extracts source IP addresses
- Counts failed login attempts by IP
- Assigns a risk level
- Prints findings to the terminal
- Saves a report to `reports/security_report.txt`

## Detection logic

The tool currently flags an IP address as suspicious when it has 5 or more failed SSH login attempts.

Risk levels:

- 5-9 failed attempts: MEDIUM
- 10+ failed attempts: HIGH

## Example output

```text
HomeSOC Log Analyzer Report
===========================

[MEDIUM] Suspicious login activity detected
IP Address: 192.168.1.50
Failed login attempts: 6
Reason: Multiple failed SSH login attempts from the same IP address.

Report saved to: reports/security_report.txt