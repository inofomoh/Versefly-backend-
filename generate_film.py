from ai_characters import create_characters
from scene_generator import build_scenes
from lip_sync_engine import apply_lip_sync
from video_exporter import export_video

def generate_full_film(script):
    characters = create_characters(script)
    scenes = build_scenes(script, characters)
    lip_synced = apply_lip_sync(scenes)
    output_file = export_video(lip_synced)
    return output_file