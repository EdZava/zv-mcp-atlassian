# Seguridad — zv-mcp-atlassian

## Instalacion reproducible (release/)

El consumidor (GestionG5) instala desde `release/` con tag fijado:

```text
uvx --from git+https://github.com/EdZava/zv-mcp-atlassian.git@0.0.1-edzava.1?subdir=release
```

- `release/uv.lock` fija dependencias PyPI.
- `release/src/` contiene solo el codigo del MCP (sin tests ni tooling de desarrollo).

## Regenerar release

```bash
python scripts/sync-python-release.py
git add release/ scripts/sync-python-release.py
git tag 0.0.1-edzava.2   # incrementar EDZAVA_RELEASE_SUFFIX en el script
git push origin main --tags
```

## Reporte

Incidencias de seguridad: mantenedor del fork EdZava.
