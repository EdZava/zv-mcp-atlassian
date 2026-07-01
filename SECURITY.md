# Seguridad — zv-mcp-atlassian

## Instalacion reproducible (release/)

El consumidor (GestionG5) instala desde `release/` con tag fijado:

```text
uvx --from git+https://github.com/EdZava/zv-mcp-atlassian.git@0.0.1-release.1?subdir=release
```

- `release/uv.lock` fija dependencias PyPI.
- `release/src/` contiene solo el codigo del MCP (sin tests ni tooling de desarrollo).

## Regenerar release

Configuracion en `.mcp-release.toml`; sincronizacion con [zv-mcp-release-toolkit](https://github.com/EdZava/zv-mcp-release-toolkit):

```bash
./scripts/sync-release.sh
# o: uv run mcp-release-toolkit sync --config .mcp-release.toml
git add release/ .mcp-release.toml
git tag 0.0.1-release.2   # incrementar release_suffix en .mcp-release.toml
git push origin main --tags
```

## Reporte

Incidencias de seguridad: mantenedor del fork EdZava.
