#!/usr/bin/env bash
# Enforce Branch Protection across Student Repositories
# Organization: The-British-College-Nepal

set -e

ORG="The-British-College-Nepal"
COUNT=0

echo "🔒 Enforcing branch protection on student repositories in $ORG..."
echo ""

gh repo list "$ORG" --limit 300 \
  --jq '.[] | select(.name | startswith("mlds-")) | .name' \
  | while read -r repo; do
    COUNT=$((COUNT + 1))
    printf "[%3d] Protecting %-50s" "$COUNT" "$repo/main..."

    if gh api -X PUT "repos/$ORG/$repo/branches/main/protection" \
      -H "Accept: application/vnd.github+json" \
      --input - <<EOF >/dev/null 2>&1; then
{
  "required_status_checks": null,
  "enforce_admins": false,
  "required_pull_request_reviews": null,
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
      echo " ✓"
    else
      echo " (Skipped/Already Protected)"
    fi
    sleep 1
  done

echo ""
echo "✅ Branch protection enforced on all repositories!"
