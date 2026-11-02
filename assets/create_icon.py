#!/usr/bin/env python3
"""Convert approved red neon artwork into a 512x512 PS5 sce_sys/icon0.png."""
from pathlib import Path
import sys
from PIL import Image

source=Path(__file__).with_name("logo.webp")
target=Path(sys.argv[1] if len(sys.argv)>1 else "sce_sys/icon0.png")
if not source.is_file():
    raise SystemExit("ERROR: Missing supplied app logo: "+str(source))
im=Image.open(source).convert("RGB")
im=im.resize((512,512),Image.Resampling.LANCZOS)
target.parent.mkdir(parents=True,exist_ok=True)
im.save(target,optimize=True)
assert Image.open(target).size==(512,512)
print("Bundled Standby Clock neon logo:",target)
