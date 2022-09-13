ITEM_KEYS = [
    "x",
    "y",
    "w",
    "h",
    "min_w",
    "min_h",
    "max_w",
    "max_h",
    "is_draggable",
    "is_resizable",
    "is_bounded",
    "static",
    "drag_ignore_from",
    "drag_allow_from",
    "resize_ignore_from",
    "preserve_aspect_ratio",
    "drag_option",
    "resize_option",
]


def update_layout_item(dest, updates):
    for key in ITEM_KEYS:
        if key in updates and dest[key] != updates[key]:
            dest[key] = updates[key]


def update_layout(original, new_layout):
    item_map = {}
    id_to_delete = set()

    # index for fast lookup
    for item in original:
        n_id = item.get("i")
        item_map[n_id] = item
        id_to_delete.add(n_id)

    # Iterate new values
    for item in new_layout:
        n_id = item.get("i")
        id_to_delete.discard(n_id)
        if n_id in item_map:
            update_layout_item(item_map[n_id], item)
        else:
            original.append(item)

    # Remove any nodes in id_to_delete
    for n_id in id_to_delete:
        original.remove(item_map[n_id])
