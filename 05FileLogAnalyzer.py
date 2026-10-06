"""File Log Analyzer - Analyze log file and extract error statistics."""


def read_file(filename: str) -> list:
    """Read and display log file contents.

    Args:
        filename: Path to log file

    Returns:
        List of log lines
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.readlines()
        for line in content:
            print(line.strip())
        return content


def analyze_log(content: list) -> dict:
    """Analyze log file and count log levels.

    Args:
        content: List of log lines

    Returns:
        Dictionary with counts of each log level
    """
    counts = {}
    for line in content:
        error_level = line.split()[0]
        if not error_level:
            continue
        counts[error_level] = counts.get(error_level, 0) + 1

    return counts


def most_common_error(error_lvl: list) -> str | None:
    """Find most common error message.

    Args:
        error_lvl: List of log lines

    Returns:
        Most common error message or None if no errors
    """
    errors = {}
    for line in error_lvl:
        parts = line.split(maxsplit=1)
        if len(parts) < 2 or parts[0] != "ERROR":
            continue
        message = parts[1].strip()
        errors[message] = errors.get(message, 0) + 1

    if not errors:
        return None
    return max(errors, key=errors.get)


def most_common_dbg_lvl(dbg_lvl: dict) -> str | None:
    """Find most common debug level.

    Args:
        dbg_lvl: Dictionary with debug level counts

    Returns:
        Most common debug level or None if empty
    """
    if not dbg_lvl:
        return None

    return max(dbg_lvl, key=dbg_lvl.get)


if __name__ == "__main__":
    lines = read_file("swlog.log")

    counts = analyze_log(lines)
    print("\n" + "="*25 + "Log Summary")
    for level, n in counts.items():
        print(f"\n{level}: {n}")

    print(f"\nMost common error: {most_common_error(lines)}")

    print(f"\nMost common debug level: {most_common_dbg_lvl(counts)}")
