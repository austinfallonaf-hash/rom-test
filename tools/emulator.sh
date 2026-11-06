#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
bundle="$root/local/mupen64plus-bundle-linux64-2.6.0"
mkdir -p "$root/local/emulator-config" "$root/local/screenshots" \
  "$root/local/native-saves" "$root/local/emulator-states"
if [[ ! -s "$root/local/emulator-config/mupen64plus.cfg" ]]; then
  cp "$root/tools/keyboard.cfg" "$root/local/emulator-config/mupen64plus.cfg"
fi
cd "$bundle"
exec ./mupen64plus --corelib "$bundle/libmupen64plus.so.2.0.0" \
  --datadir "$bundle" --plugindir "$bundle" \
  --configdir "$root/local/emulator-config" \
  --sshotdir "$root/local/screenshots" --nosaveoptions \
  --set "Core[SaveSRAMPath]=$root/local/native-saves/" \
  --set "Core[SaveStatePath]=$root/local/emulator-states/" \
  "$@" "${ROM_PATH:-$root/local/original.z64}"
