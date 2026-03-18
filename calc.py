#!/usr/bin/env python3

while True:
	stack = []

	try: s = input()
	except KeyboardInterrupt: exit()

	for e in s.split(" "):
		if e.isdigit() or e.startswith("-") and e[1:].isdigit():
			stack.append(int(e))
			continue

		if len(stack) < 2:
			print("Too Few Arguments")
			break

		b, a = stack.pop(), stack.pop()

		match e:
			case "+": stack.append(a + b)
			case "-": stack.append(a - b)
			case "*": stack.append(a * b)
			case "/": stack.append(a // b)
			case _:
				print("Invalid Token")
				break

	if len(stack) == 1:
		print(stack[0])
	else:
		print("Invalid Input")
	
