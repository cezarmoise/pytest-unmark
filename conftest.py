#!/usr/bin/env python3

def pytest_collection_modifyitems(items):
    """
    Move the markers from the parents to the items
    Remove markers that have an equivalent negative marker

    before: 
        item.own_markers = [mark_1, not_mark2]
        item.parent.own_markers = [mark2, mark3]
        item.iter_markers = [mark1, not_mark2, mark2, mark3]
    after
        item.own_markers = [mark_1, mark3]
        item.parent.own_markers = []
        item.iter_markers = [mark1, mark3]
    """

    for item in items:
        # iter_markers() return this item's markers + the markers of the parent
        markers = [m.name for m in item.iter_markers()]
        positive = set([m for m in markers if not m.startswith("not_")])
        negative = set([m[4:] for m in markers if m.startswith("not_")])
        # only retain those markers that don't have an equivalent negative marker 
        item.own_markers = [m for m in item.iter_markers() if m.name in positive - negative]

    for item in items:
        for parent in item.iter_parents():
            if item is not parent:
                # remove markers from parents, so subsequent calls of this hook have the correct marker list
                parent.own_markers = []
