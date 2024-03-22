"""Core workflow for Spatial Transcriptomics Prep by Red@."""

PROJECT_NAME = "Spatial Transcriptomics Prep"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
