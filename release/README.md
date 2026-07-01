# release-mcp-atlassian (release)

Paquete **standalone** para `uvx --from git+...@TAG?subdir=release`.

## Cliente MCP (`mcp.json`)

```json
"git+https://github.com/EdZava/zv-mcp-atlassian.git#0.0.1-release.1?subdir=release"
```

## Regenerar

```bash
mcp-release-toolkit sync --config .mcp-release.toml
git add release/ .mcp-release.toml
git tag 0.0.1-release.1
git push origin main --tags
```
