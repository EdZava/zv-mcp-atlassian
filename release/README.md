# edzava-mcp-atlassian (release)

Paquete **standalone** para `uvx --from git+...@TAG?subdir=release`.

## Cursor (`mcp.json`)

```json
"git+https://github.com/EdZava/zv-mcp-atlassian.git#0.0.1-edzava.1?subdir=release"
```

## Regenerar

```bash
python scripts/sync-python-release.py
git add release/ scripts/sync-python-release.py
git tag 0.0.1-edzava.1
git push origin main --tags
```
