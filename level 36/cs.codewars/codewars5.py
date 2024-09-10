def is_anagram(test, original):
    test_sorted = "".join(sorted(test.lower()))
    original_sorted = "".join(sorted(original.lower()))
    
    return test_sorted == original_sorted