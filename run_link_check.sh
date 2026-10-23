#!/usr/bin/env bash
# Dead-link gate. Exit 0 = pass. Exit != 0 = BLOCK DEPLOY.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

LYCHEE_BIN="${LYCHEE_BIN:-$HOME/.local/bin/lychee}"
if [ ! -x "$LYCHEE_BIN" ]; then
    echo "ERROR: lychee binary not found or not executable at $LYCHEE_BIN" >&2
    exit 1
fi

SITE_NAME="$(basename "$PWD")"
OUT_JSON="/tmp/lychee_${SITE_NAME}.json"
OUT_ERR="/tmp/lychee_${SITE_NAME}.err"

if [ "${1:-}" = "--live" ]; then
    echo "Running live internal link check for https://thesiftguide.com..."
    OUT_JSON="/tmp/lychee_${SITE_NAME}_live.json"
    OUT_ERR="/tmp/lychee_${SITE_NAME}_live.err"
    "$LYCHEE_BIN" --config "$SCRIPT_DIR/.lychee.toml" \
        --exclude '.*' \
        --include 'thesiftguide\.com' \
        --format json \
        "https://thesiftguide.com" > "$OUT_JSON" 2> "$OUT_ERR" || {
        echo "DEAD LINKS DETECTED (live) - see $OUT_JSON and $OUT_ERR" >&2
        cat "$OUT_ERR" >&2
        exit 1
    }
    echo "Live link check PASSED"
    exit 0
fi

# Default mode: --offline validates internal href integrity (anchors, relative paths).
"$LYCHEE_BIN" --config "$SCRIPT_DIR/.lychee.toml" \
    --offline \
    --extensions html \
    --exclude '\.bak$' \
    --format json \
    . > "$OUT_JSON" 2> "$OUT_ERR" || {
    echo "DEAD LINKS DETECTED - see $OUT_JSON and $OUT_ERR" >&2
    cat "$OUT_ERR" >&2
    exit 1
}

echo "Link check PASSED"
