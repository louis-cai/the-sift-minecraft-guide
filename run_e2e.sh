#!/usr/bin/env bash
# ==============================================================================
# run_e2e.sh - One-click E2E Automated Regression Test Runner for thesiftguide.com
# Usage:
#   ./run_e2e.sh                    # Defaults to --target live (https://thesiftguide.com)
#   ./run_e2e.sh --target live      # Run against live Cloudflare Pages production
#   ./run_e2e.sh --target local     # Run against local static files with auto-server
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Locate Python binary with playwright installed
PYTHON_BIN=""
if [ -f "/home/louis/.hermes/hermes-agent/venv/bin/python3" ]; then
    PYTHON_BIN="/home/louis/.hermes/hermes-agent/venv/bin/python3"
elif [ -f "/home/louis/.clawteam/.venv/bin/python3" ]; then
    PYTHON_BIN="/home/louis/.clawteam/.venv/bin/python3"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python3)"
else
    echo "Error: python3 not found." >&2
    exit 1
fi

echo "================================================================="
echo "   TheSiftGuide.com Playwright E2E Regression Test Runner"
echo "================================================================="
echo "Interpreter: $PYTHON_BIN"
echo "Workdir:     $SCRIPT_DIR"
echo "Arguments:   $*"
echo "-----------------------------------------------------------------"

exec "$PYTHON_BIN" "$SCRIPT_DIR/tests/test_e2e_thesiftguide.py" "$@"
