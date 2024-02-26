""" Input menu command
"""

print('')
print("Input command menu.")
print('')

print('- Command 1: 1')
print('- Command 2: 2')

user_command = ''

while user_command != 'q':
	while (user_command := input("\nMenu command <1/2> or Q to quit: ").lower().strip()) not in ("1", "2", "q"):
		print( f"Your answer: {user_command}")

	if user_command == '1':
		print("\nExecuting command 1.\n")
		print('\t- Sub Command 1: 1')
		print('\t- Sub Command 2: 2')

		while (sub_command := input("\nSub Menu command <1/2> or Q to quit: ").lower().strip()) not in ("1", "2", "q"):
			print( f"Your answer for sub command: {sub_command}")

		if sub_command == '1':
			print("\tExecuting sub command 1.")
		if sub_command == '2':
			print("\tExecuting sub command 2.")
		if sub_command == 'q':
			print("\tExit sub command menu.")

	if user_command == '2':
		print("Executing command 2.")

	if user_command == 'q':
		print("Quit.")

print('')
print("Command menu ENDED.")
print('')