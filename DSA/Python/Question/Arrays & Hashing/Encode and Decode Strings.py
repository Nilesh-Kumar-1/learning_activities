# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.
s= ["neet","code","love","you"]

print("test"[:2])
# class Solution:

#     def encode(self, strs: list[str]) -> str:
#         encoded_str = ""
#         for s in strs:
#             encoded_str += str(len(s)) + "#" + s + "-->"
#         return encoded_str


#     def decode(self, s: str) -> list[str]:
#         decoded_strs = []
#         decoding = s.split("-->")
#         for d in decoding:
#             if d:
#                 length, string = d.split("#")
#                 decoded_strs.append(string[:int(length)])
#         return decoded_strs        


# test= Solution

# print(Solution.encode(test,s))

# # Actual solution

class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str


    def decode(self, s: str) -> list[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = s[i:j]
            decoded_strs.append(s[j+1:j+1+int(length)])
            i = j+1+int(length)
        return decoded_strs
     