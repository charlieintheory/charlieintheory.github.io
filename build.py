"""Copy the dependency-free website into the static deployment directory."""

from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
output = root / "dist"
output.mkdir(exist_ok=True)
for name in ("index.html", "styles.css"):
    shutil.copy2(root / name, output / name)
shutil.copytree(root / "assets", output / "assets", dirs_exist_ok=True)
print(f"Static website built in {output}")
