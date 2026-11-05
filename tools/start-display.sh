#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$root/local/x11"
# Run in a managed terminal; stop this process with Ctrl-C when finished.
exec Xorg :7 -config "$root/tools/xorg-dummy.conf" \
  -logfile "$root/local/x11/Xorg.log" -noreset -nolisten tcp
