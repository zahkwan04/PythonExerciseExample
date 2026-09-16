# 7. CSV Test Result Analyzer

# Since you work with test scripts, this one is especially relevant.

# Imagine a CSV containing:

# Test_ID,Expected,Actual
# TC_001,PASS,PASS
# TC_002,PASS,FAIL
# TC_003,PASS,PASS
# TC_004,FAIL,FAIL
# TC_005,PASS,PASS

# Write a Python program that produces:

# Total tests: 5
# Passed: 4
# Failed: 1
# Pass rate: 80%

# Then identify:

# Failed tests:
# TC_002

# Bonus: generate a new summary.txt file automatically.