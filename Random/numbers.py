# Convert a number to english representation
# ie. in --> 100, out --> one hundred
number_to_english = {
	6: 'billion',
	5: 'million',
	4: 'thousand',
	3: 'hundred',
	2:	{
				2: 'twenty',
				3: 'thirty',
				4: 'forty',
				5: 'fifty',
				6: 'sixty',
				7: 'seventy',
				8: 'eighty',
				9: 'ninety',
		},
	1:	{
				19: 'nineteen',
				18: 'eightteen',
				17: 'seventeen',
				16: 'sixteen',
				15: 'fifteen',
				14: 'fourteen',
				13: 'thirteen',
				12: 'twelve',
				11: 'eleven',
				10: 'ten',
		},
	0:	{
				9: 'nine',
				8: 'eight',
				7: 'seven',
				6: 'six',
				5: 'five',
				4: 'four',
				3: 'three',
				2: 'two',
				1: 'one',
		}	
}
def translate_number(number):
	# we are assuming that number is of type int
	num_string = str(number)
	if number == 0:
		return " "
	len_of_num = len(num_string)
	if len_of_num >= 3:
		return translate_number(int(num_string[0])) + " " + number_to_english[len_of_num] + " " + translate_number(int(num_string[1:]))
	# if we have a number in the tens position
	if len_of_num == 2:
		if number >= 20:
			return number_to_english[2][int(num_string[0])] + " " + translate_number(int(num_string[1:]))
		else:
			# if number is in the teens or is ten
			return number_to_english[1][number]
	else:
		# If number is less than 20
		return number_to_english[0][number]

