/*
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
*/
#include <iostream>
using namespace std;

int ** create2D(int ** image,int numRows, int numCols){
  image = new int *[numRows];
  for(int i = 0; i < numRows; ++i)
    image[i] = new int[numCols];
  return image;
}

void fillMatrixOneValue(int ** matrix,int row,int col, int value){
	for(int i = 0; i < row; ++i){
		for(int j = 0; j < col; ++j){
			matrix[i][j] = value;
		}
	}
}

void clearRow(int ** matrix, int rowValue, int col){
	for(int c = 0; c < col; ++c)
		matrix[rowValue][c] = 0;
}

void clearCol(int ** matrix, int colValue, int row){
	for(int r = 0; r < row; ++r)
		matrix[colValue][r] = 0;
}

void clear_row_col(int ** matrix, int row, int col, int * row_map, int * col_map){
	for(int i = 0; i < row; ++i){
		if(row_map[i] == 1){
			clearRow(matrix,i,col);
		}
	}

	for(int i = 0; i < col; ++i){
		if(col_map[i] == 1){
			clearCol(matrix,i,row);
		}
	}
}

void zeroOut(int ** matrix, int m, int n){
	int * row_map = new int [m];
	int * col_map = new int [n];
	fillMatrixOneValue(row_map,m,0,0);
	fillMatrixOneValue(col_map,n,0,0);

	for(int row = 0; row < m; ++row){
		for(int col = 0; col < n; ++col){
			if(matrix[row][col] == 0){
				row_map[row] = 1;
				col_map[col] = 1;
			}
			
		}
	}
	
	clear_row_col(matrix,m,n,row_map,col_map);
}

void printOut(int ** matrix,int row, int col){
	for(int i = 0; i < row; ++i){
		for(int j = 0; j < col; ++j){
			cout << matrix[i][j];
		}
		cout << endl;
	}
}
int main(){
	
	int ** matrix;
	int row = 3,col = 3;
	matrix = create2D(matrix,row,col);
	

	fillMatrixOneValue(matrix,row,col,3);
	matrix[2][2] = 0;
	printOut(matrix,row,col);
	zeroOut(matrix,row,col);
	printOut(matrix,row,col);

	return 0;
}