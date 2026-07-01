#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
uvx --from "git+ssh://git@github.com/EdZava/zv-mcp-release-toolkit.git@v0.3.2" \
  mcp-release-toolkit publish --config .mcp-release.toml --root .
