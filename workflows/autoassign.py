name: Auto Assign to Organization Member

on:
  issues:
    types: [opened]
  pull_request:
    types: [opened]

jobs:
  assign-random-member:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3  # Updated to the latest version
      
      - name: Run custom assignment script
        run: python ../../scripts/assign_member_to_issues.py
        env:
          GITHUB_TOKEN: ${{ secrets.MY_PAT }}
          ORG_NAME: 'GuineaBot3Labs'  # Ensure this is correct
          REPO_NAME: ${{ github.repository }}  # Verify this resolves correctly
          ISSUE_NUMBER: ${{ github.event.issue.number || github.event.pull_request.number }}
