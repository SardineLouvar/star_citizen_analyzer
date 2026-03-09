from pathlib import Path

# Absolute project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Core paths
JSON_PATH = PROJECT_ROOT / "data" / "api_data"
DB_PATH = PROJECT_ROOT / "data" / "databases"
CONFIG_PATH = PROJECT_ROOT / "config.yaml"
DEV_CONFIG_PATH = PROJECT_ROOT / "dev_config.yaml"
ANALYSIS_PATH = PROJECT_ROOT / "src" / "analysis"
ANALYSIS_DATA_PATH = ANALYSIS_PATH / "for_data"
FIG_PATH = PROJECT_ROOT / "data" / "figs"

# Ensure folders exist
JSON_PATH.mkdir(exist_ok=True)
DB_PATH.mkdir(exist_ok=True)
FIG_PATH.mkdir(exist_ok=True)

