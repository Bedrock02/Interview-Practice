=begin
Implement an algorithm to determine if a string as all unique characters. what if you can not use aditional data structures?
Ref. Cracking the Codeing Interview Chapter 1.1
=end

#without datastructures
def uniquness_first_approach(string)
	search_index = 0
	string.each_char do |character|
		
		string[search_index+1..-1].each_char do |suspect|
			if string[search_index] == suspect
				return false
			end
		end
		search_index = search_index +1
	end
	return true
end

#first sorts the array of characters then proceeds to check them one after another
def uniqueness_second_approach(string)
	string_ary = string.split(//)
	string_ary.sort!
	
	string_ary[1..-1].each_index do |letter|
		if string_ary[letter+1] == string_ary[letter]
			return false
		end
	end
	return true
end

#algorithm using a data structure #hash to store all indc
def uniqueness_third_approach(string)
	char_hash = Hash.new(1)
	string.each_char do |letter|
		unless char_hash.has_key? letter
			char_hash[letter] = 1
		else
			return false
		end
	end
	return true
end

print uniqueness_third_approach("steven")