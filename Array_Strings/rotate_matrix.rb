=begin
	
Given a nimage represented by an NxN matrix, where each pixel in teh image is 4 bytes, 
write a method to rotate the image by 90 degrees
	
=end

def create_n_by_n(size)
	matrix = []
	size.times do
		matrix << []
	end
	return matrix
end

def rotate_matrix(matrix)
	size = matrix.size
	new_image = create_n_by_n(size)
	row = 0
	
	size.times do
		col = 0
		
		size.times do
			new_image[row][col] =  matrix[size-1-col][row]
			col += 1
		end
		
		row += 1
	end
	return new_image
end

image = [

	[1,1,1],
	[2,2,2],
	[3,3,3]
]

print rotate_matrix(image)