def apply_lip_sync(scenes):
    for scene in scenes:
        scene["lip_synced"] = True
    return scenes