import argparse
from spatial_transcriptomics_prep.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Preparation utilities for spatial transcriptomics sample metadata and region grids.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
