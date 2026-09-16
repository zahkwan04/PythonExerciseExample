# Imagine your software generates this log:

# INFO System started
# INFO Loading configuration
# ERROR Failed to connect
# INFO Retrying connection
# ERROR Connection timeout
# WARNING Low memory
# INFO Connection successful
# ERROR Sensor failure

# Write Python code that reads the log and calculates:

# INFO: 4
# WARNING: 1
# ERROR: 3

# Bonus:

# Most common error: Connection timeout

# This is actually quite close to something you'd encounter in real engineering/software work.

def read_file(filename: str) -> list:

    with open(filename, "r") as f:
        content = f.readlines()
        for line in content:
            print(line.strip())
        return content


def analyze_log(content: list) -> dict:
    counts = {}
    for line in content:
        error_level = line.split()[0]
        if not error_level:
            continue
        counts[error_level] = counts.get(error_level, 0) + 1

    return counts


def most_common_error(error_lvl: list) -> str | None:
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
    if not dbg_lvl:
        return None
    
    return max(dbg_lvl, key = dbg_lvl.get)


if __name__ == "__main__":
    lines = read_file("swlog.log")

    counts = analyze_log(lines)
    print("\n=========Log Summary=========")
    for level, n in counts.items():
        print(f"\n{level}: {n}")

    print(f"\nMost common error: {most_common_error(lines)}")

    print(f"\nMost common debug level: {most_common_dbg_lvl(counts)}")