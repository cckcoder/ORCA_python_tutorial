# Example

# Passing Grade = 3.0
# How much students pass this exam?
"""
grade = [3.5, 4.0, 3.8, 2.9, 3.0, 1.7, 4.0, 2.9]
pass_score = 3.0

num_pass = 0

for sc in grade:
	if sc >= pass_score:
		num_pass += 1

print("There are ",num_pass," students pass this exam.")
"""

#Word Count
word = """
			 Hello pylthon, how are you today.
			 today is Monday and There are 2 pens on The table
			 """
find = "on"
counter = 0

for i in range(len(word)):
	if word[i] == find[0]:
		w_len = len(find)

