#Write a Python program to find the longest common prefix of all strings. Use the Python set.

strings = ["flower", "flow", "flight"]

if not strings:
    print("No strings provided")
else:
  
    shortest = min(strings, key=len)

    longest_prefix = ""

    for i in range(len(shortest)):
        prefix = shortest[:i + 1]

        prefixes = set(s[:i + 1] for s in strings)

        if len(prefixes) == 1:
            longest_prefix = prefix
        else:
            break

    print("Longest Common Prefix:", longest_prefix)
