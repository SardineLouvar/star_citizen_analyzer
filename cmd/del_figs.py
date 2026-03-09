from pathlib import Path

from src.paths import FIG_PATH


if __name__ == "__main__":
    """
    quick way to delete all figures in the figs folder
    """
    folder = Path(FIG_PATH)
    path_len = len(str(FIG_PATH))

    for file in folder.rglob("*.png"):
        file.unlink()
        print(f"deleted fig {str(Path(file))[(path_len+1):]}")