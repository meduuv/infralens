from collections.abc import Iterable, Mapping


def inventory(resources: Iterable[Mapping[str, object]]) -> dict[str, list[str]]:
    """Group infrastructure resources by type."""
    result: dict[str, set[str]] = {}
    for resource in resources:
        kind = str(resource.get("type", "unknown")).strip() or "unknown"
        name = str(resource.get("name", "")).strip()
        if not name:
            raise ValueError("resource name is required")
        result.setdefault(kind, set()).add(name)
    return {kind: sorted(names) for kind, names in sorted(result.items())}
