S = input()
case_fold = S.casefold()
reverse_str = reversed(case_fold)

if list(case_fold) == list(reverse_str):
	print('Yes')
else:
	print('No')