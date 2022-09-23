class Solution:
  def __init__(self):
    self.map = {} # key: (s1, s2), value: bool

  def isScramble(self, s1, s2):
    if (s1, s2) in self.map:
      return self.map[(s1, s2)]

    if len(s1) != len(s2):
            # Memorization
      self.map[(s1, s2)] = False
      return False

    if s1 == s2:
            # Memorization
      self.map[(s1, s2)] = True
      return True

        # Prunning
    if sorted(s1) != sorted(s2):
            # Memorization
      self.map[(s1, s2)] = False
      return False

        # i starts from 1, otherwise s[0:0] causes RecursionError
    for i in range(1, len(s1)):
      if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
        return True

      if self.isScramble(s1[:i], s2[len(s2)-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
        return True

        # Memorization
    self.map[(s1, s2)] = False
    return False

sr1 = input("string_1: ")
sr2 = input("string_2: ")
s = Solution()
print(s.isScramble(sr1,sr2))
