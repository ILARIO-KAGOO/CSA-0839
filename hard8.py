def isScramble(s1, s2):
  map = {}
  if (s1, s2) in map:
    return map[(s1, s2)]

  if len(s1) != len(s2):
          # Memorization
    map[(s1, s2)] = False
    return False

  if s1 == s2:
          # Memorization
    map[(s1, s2)] = True
    return True

      # Prunning
  if sorted(s1) != sorted(s2):
          # Memorization
    map[(s1, s2)] = False
    return False

      # i starts from 1, otherwise s[0:0] causes RecursionError
  for i in range(1, len(s1)):
    if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]):
      return True

    if isScramble(s1[:i], s2[len(s2)-i:]) and isScramble(s1[i:], s2[:len(s2)-i]):
      return True
  map[(s1, s2)] = False
  return False

sr1 = input("string_1: ")
sr2 = input("string_2: ")
print(isScramble(sr1,sr2))