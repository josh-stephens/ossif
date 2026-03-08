#!/bin/bash
# Email weekly OSSIF translation token report via skippy SMTP relay.
# Designed to run from bettik via launchd cron.

set -euo pipefail

REPO_ROOT="$HOME/Projects/ossif"
REPORT_SCRIPT="$REPO_ROOT/scripts/translation-report.py"
REPORT_FILE="/tmp/ossif-translation-report.html"

# Pull latest logs from repo
cd "$REPO_ROOT"
git pull --quiet 2>/dev/null || true

# Check for any logs
if ! ls "$REPO_ROOT/scripts/logs/translate-"*.json &>/dev/null; then
    echo "No translation logs found, skipping email."
    exit 0
fi

# Generate report to file
python3 "$REPORT_SCRIPT" --output "$REPORT_FILE"

# Read the HTML
REPORT_HTML=$(cat "$REPORT_FILE")

# Send via skippy SMTP relay
ssh skippy python3 -c "
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

msg = MIMEMultipart('alternative')
msg['Subject'] = '[OSSIF] Weekly Translation Token Report'
msg['From'] = 'automation@eusd.org'
msg['To'] = 'josh.stephens@gmail.com'

html = sys.stdin.read()
msg.attach(MIMEText('View this email in an HTML-capable client.', 'plain'))
msg.attach(MIMEText(html, 'html'))

with smtplib.SMTP('10.15.10.35', 25) as s:
    s.send_message(msg)
print('Token report email sent')
" <<< "$REPORT_HTML"

rm -f "$REPORT_FILE"
echo "Done."
