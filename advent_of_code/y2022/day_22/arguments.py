import argparse


def init_args() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--interactive",
        required=False,
        default=None,
        choices=[1, 2],
        help="Show visualization for part #",
        action="store",
        type=int,
    )
    parser.add_argument(
        "-d",
        "--data",
        required=False,
        default=False,
        action="store_true",
        help="Use data.txt instead of example.txt",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        required=False,
        default=False,
        action="store_true",
        help="Enable debug logging",
    )
    return parser.parse_args()
