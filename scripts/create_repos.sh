#!/usr/bin/env bash
# Automated Repository Provisioning Script
# Creates 105 private repositories (3 modules × 35 students)
# Organization: The-British-College-Nepal

set -e

ORG="The-British-College-Nepal"
MODULES=("data-preprocessing" "model-building" "deployment")
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
USERNAMES_FILE="${SCRIPT_DIR}/github_usernames.txt"

if [ ! -f "$USERNAMES_FILE" ]; then
  echo "❌ Error: $USERNAMES_FILE not found!"
  echo "   Generate it first via: gh api orgs/$ORG/members --jq '.[].login' | sort > ${USERNAMES_FILE}"
  exit 1
fi

TOTAL_STUDENTS=$(grep -cve '^\s*$' "$USERNAMES_FILE")
TOTAL_EXPECTED=$(( TOTAL_STUDENTS * ${#MODULES[@]} ))
COUNT=0

echo "🚀 Provisioning student repositories in $ORG..."
echo "   Total Students: $TOTAL_STUDENTS"
echo "   Modules: ${MODULES[*]}"
echo "   Target Repositories: $TOTAL_EXPECTED"
echo ""

while read -r username; do
  username=$(echo "$username" | xargs)
  [ -z "$username" ] && continue

  # Skip instructor account if present
  if [ "$username" == "Sudan23" ]; then
    continue
  fi

  for module in "${MODULES[@]}"; do
    REPO="mlds-${module}-${username}"
    TEMPLATE="$ORG/${module}-template"
    COUNT=$((COUNT + 1))

    printf "[%3d/%3d] Setting up %-45s" "$COUNT" "$TOTAL_EXPECTED" "$REPO..."

    # Create repo from template
    if gh repo create "$ORG/$REPO" \
      --private \
      --template "$TEMPLATE" >/dev/null 2>&1; then
      echo " ✓ (Created)"
    else
      echo " - (Exists/Skipped)"
    fi

    # Add student as collaborator with push permissions
    gh api -X PUT "repos/$ORG/$REPO/collaborators/$username" \
      -f permission="push" >/dev/null 2>&1 || true

    sleep 2  # GitHub API rate limit prevention
  done
done < "$USERNAMES_FILE"

echo ""
echo "✅ Finished provisioning repositories!"
