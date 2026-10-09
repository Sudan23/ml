#!/usr/bin/env bash
# Automated Student Invitation Script
# Organization: The-British-College-Nepal
# Course: UFCFAS-15-2 / MLDS-AI (BSc AI Level 5 Semester 1)

set -e

ORG="The-British-College-Nepal"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EMAILS_FILE="${SCRIPT_DIR}/emails.txt"

if [ ! -f "$EMAILS_FILE" ]; then
  echo "❌ Error: $EMAILS_FILE not found!"
  exit 1
fi

TOTAL=$(grep -cve '^\s*$' "$EMAILS_FILE")
COUNT=0

echo "🚀 Sending organization invitations for $ORG ($TOTAL recipients)..."
echo ""

while read -r email; do
  email=$(echo "$email" | xargs)
  [ -z "$email" ] && continue

  COUNT=$((COUNT + 1))
  printf "[%2d/%2d] Inviting %-42s" "$COUNT" "$TOTAL" "$email..."

  if gh api -X POST "orgs/$ORG/invitations" \
    -f email="$email" \
    -f role="direct_member" >/dev/null 2>&1; then
    echo " ✓ (Invited)"
  else
    echo " - (Already invited, member, or error)"
  fi
  sleep 1
done < "$EMAILS_FILE"

echo ""
echo "✅ Finished sending invitations!"
echo "   Monitor acceptance with: gh api orgs/$ORG/members --jq 'length'"
