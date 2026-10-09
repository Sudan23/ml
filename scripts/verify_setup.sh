#!/usr/bin/env bash
# Audit and Health Check for MLDS Course Setup
# Organization: The-British-College-Nepal

ORG="The-British-College-Nepal"
TEAM="mlds-ai-l5-s1"

echo "============================================================"
echo "📊 UFCFAS-15-2 / MLDS Course Infrastructure Health Check"
echo "   Organization: $ORG"
echo "============================================================"
echo ""

echo "👥 Organization Members:"
MEMBERS_COUNT=$(gh api "orgs/$ORG/members" --jq 'length' 2>/dev/null || echo "0")
echo "   Total active members: $MEMBERS_COUNT / 36 target"

echo ""
echo "👥 Cohort Team ($TEAM):"
TEAM_COUNT=$(gh api "orgs/$ORG/teams/$TEAM" --jq '.members_count' 2>/dev/null || echo "0")
echo "   Team members count: $TEAM_COUNT"

echo ""
echo "📦 Template Repositories:"
gh repo list "$ORG" --limit 50 --json name,isTemplate \
  --jq '.[] | select(.isTemplate == true) | "   - \(.name)"'

echo ""
echo "📚 Student Repositories:"
STUDENT_REPOS=$(gh repo list "$ORG" --limit 300 --jq '.[] | select(.name | startswith("mlds-")) | .name' 2>/dev/null | wc -l || echo "0")
echo "   Total student repositories: $STUDENT_REPOS / 105 target"

echo ""
echo "🐳 Docker Image Verification:"
docker images | grep "alkimi/ml" || echo "   (Run: docker pull alkimi/ml:week1)"

echo ""
echo "============================================================"
echo "✅ Audit completed!"
echo "============================================================"
