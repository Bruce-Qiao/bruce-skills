#!/usr/bin/env bash
# Render a diagram or page to PNG with headless Chrome, so it can be checked by eye.
# Usage: preview.sh <file.mmd|file.svg|file.html> <out.png> [width] [height]
#   .mmd  Mermaid source (wrapped in a temporary page that loads mermaid from jsDelivr)
#   .svg / .html  rendered as-is
set -euo pipefail

SRC="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
OUT="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"
W="${3:-1280}"; H="${4:-900}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[[ -x "$CHROME" ]] || { echo "Google Chrome not found at $CHROME" >&2; exit 1; }

case "$SRC" in
  *.mmd)
    TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
    { echo '<!doctype html><meta charset="utf-8"><body style="margin:16px;background:#fff"><pre class="mermaid">'
      cat "$SRC"
      echo '</pre><script type="module">import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs"; mermaid.initialize({startOnLoad:true});</script>'
    } > "$TMP/page.html"
    URL="file://$TMP/page.html" ;;
  *.svg|*.html) URL="file://$SRC" ;;
  *) echo "Unsupported file type: $SRC" >&2; exit 1 ;;
esac

# Headless Chrome won't go narrower than 500px; show narrow (mobile) widths inside an iframe instead
WIN="$W"
if (( W < 500 )); then
  [[ -n "${TMP:-}" ]] || { TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT; }
  echo "<!doctype html><body style=\"margin:0;background:#888\"><iframe src=\"$URL\" style=\"width:${W}px;height:${H}px;border:0;display:block\"></iframe>" > "$TMP/frame.html"
  URL="file://$TMP/frame.html"; WIN=500
fi

"$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size="$WIN,$H" \
  --virtual-time-budget=8000 --screenshot="$OUT" "$URL" >/dev/null 2>&1
[[ -s "$OUT" ]] && echo "Saved $OUT" || { echo "Screenshot failed" >&2; exit 1; }
