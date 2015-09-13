def nth_fib(n)
	if n <=0
		return "Wrong input"
	end
	if n == 1 
		return 0
	end

	if n == 2
		return 1
	end

	return nth_fib(n-1) + nth_fib(n-2)
end