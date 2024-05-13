import pytest
from _pytest.mark import _parse_expression as parse_expression

def pytest_collection_modifyitems(items, config):
    matchexpr = config.option.markexpr
    if not matchexpr:
        return

    expr = parse_expression(matchexpr, "Error with -m parameter")
    remaining = []
    deselected = []

    for item in items:
        markers = [m.name for m in item.iter_markers()]
        positive = set([m for m in markers if not m.startswith("not_")])
        negative = set([m[4:] for m in markers if m.startswith("not_")])
        final = positive - negative

        if expr.evaluate(lambda x: x in final):
            remaining.append(item)
        else:
            deselected.append(item)

    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = remaining
