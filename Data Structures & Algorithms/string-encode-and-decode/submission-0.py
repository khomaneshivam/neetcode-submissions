from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for word in strs:
            encoded.append(str(len(word)))
            encoded.append("#")
            encoded.append(word)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Read the length
            length = ""

            while s[i] != "#":
                length += s[i]
                i += 1

            length = int(length)

            # Skip '#'
            i += 1

            # Read the next 'length' characters
            decoded.append(s[i:i + length])

            # Move to the next encoded string
            i += length

        return decoded