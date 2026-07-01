#!/usr/bin/env python3
"""Genera release/ instalable via uvx --from git+...?subdir=release."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RELEASE = ROOT / "release"
SOURCE_PYPROJECT = ROOT / "pyproject.toml"

# Incrementar al republicar (paridad con gitlab-mcp edzava.N)
EDZAVA_RELEASE_SUFFIX = "edzava.1"

# Paquete fuente en src/ (nombre de carpeta)
SRC_PACKAGE_DIR = "mcp_atlassian"

# Version base publicada (sin sufijo dev de VCS)
BASE_VERSION = "0.0.1"


def pin_dependencies(deps: list[str]) -> list[str]:
  result: list[str] = []
  for dep in deps:
    # Conservar marcadores de plataforma (; platform_system==...)
    if ";" in dep:
      spec, marker = dep.split(";", 1)
      spec = spec.strip()
      marker = marker.strip()
      if any(op in spec for op in (">=", "<=", "!=", "~=", "==", "<", ">")):
        result.append(f"{spec}; {marker}")
      else:
        result.append(f"{spec}; {marker}")
      continue
    if any(op in dep for op in (">=", "<=", "!=", "~=", "==", "<", ">")):
      result.append(dep)
    else:
      result.append(dep)
  return result


def main() -> int:
  if not SOURCE_PYPROJECT.is_file():
    print("sync-python-release: falta pyproject.toml en la raiz", file=sys.stderr)
    return 1

  source = tomllib.loads(SOURCE_PYPROJECT.read_text(encoding="utf-8"))
  project = source["project"]
  src_path = ROOT / "src" / SRC_PACKAGE_DIR
  if not src_path.is_dir():
    print(f"sync-python-release: falta {src_path}", file=sys.stderr)
    return 1

  release_version_tag = f"{BASE_VERSION}-{EDZAVA_RELEASE_SUFFIX}"
  release_version_pep = f"{BASE_VERSION}+{EDZAVA_RELEASE_SUFFIX}"
  release_name = f"edzava-{project['name']}"

  release_pyproject = f"""[project]
name = "{release_name}"
version = "{release_version_pep}"
description = "MCP Atlassian (fork EdZava, instalable desde release/)"
requires-python = "{project['requires-python']}"
dependencies = [
{chr(10).join(f'  "{d}",' for d in pin_dependencies(project["dependencies"]))}
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project.scripts]
mcp-atlassian = "mcp_atlassian:main"

[tool.hatch.build.targets.wheel]
packages = ["src/{SRC_PACKAGE_DIR}"]
"""

  if RELEASE.exists():
    shutil.rmtree(RELEASE)
  RELEASE.mkdir(parents=True)
  shutil.copytree(src_path, RELEASE / "src" / SRC_PACKAGE_DIR)

  (RELEASE / "pyproject.toml").write_text(release_pyproject, encoding="utf-8")

  subprocess.run(
    ["uv", "lock"],
    cwd=RELEASE,
    check=True,
  )

  readme = f"""# edzava-mcp-atlassian (release)

Paquete **standalone** para `uvx --from git+...@TAG?subdir=release`.

## Cursor (`mcp.json`)

```json
"git+https://github.com/EdZava/zv-mcp-atlassian.git#{release_version_tag}?subdir=release"
```

## Regenerar

```bash
python scripts/sync-python-release.py
git add release/ scripts/sync-python-release.py
git tag {release_version_tag}
git push origin main --tags
```
"""
  (RELEASE / "README.md").write_text(readme, encoding="utf-8")

  print(f"release sincronizado: {release_name}@{release_version_tag} (pep440: {release_version_pep})")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
