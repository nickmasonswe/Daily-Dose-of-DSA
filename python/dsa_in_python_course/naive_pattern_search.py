def pattern_search(text, pattern):
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    match_count = 0
    for char in range(len(pattern)):
      if pattern[char] == text[index + char]:
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)
# naivest possible version. Could use sliding window at size m where 
# n is length of text and # m is the length of the pattern and n>m
# also could use KMP algorithm instead