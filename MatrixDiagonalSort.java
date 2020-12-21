package LeetCode;

import java.util.ArrayList;
import java.util.Collections;

public class MatrixDiagonalSort {

	 public int[][] diagonalSort(int[][] mat) {
	        int rows = mat.length;
	        int cols = mat[0].length;
	        //first we traverse row
	        for(int i= mat.length-2;i>=0;i--){
	            int j =0;
	            int k = i;
	            ArrayList<Integer> list = new ArrayList<>();
	            while(k<rows && j<cols){
	                list.add(mat[k][j]);
	                k++;
	                j++;
	            }
	            Collections.sort(list);
	            k = i;
	            j=0;
	            int l = 0;
	            while(k<rows && j<cols && l<list.size()){
	                mat[k++][j++]= list.get(l++);
	            }
	        }
	        
	        //second we traverse the columns
	        for(int j=1;j<cols-1;j++){
	            int i =0;
	            int k = j;
	            ArrayList<Integer> list = new ArrayList<>();
	            while(i<rows && k<cols) {
	            	list.add(mat[i++][k++]);
	            }
	            Collections.sort(list);
	            k = j;
	            i=0;
	            int l =0;
	            while(k<cols && i<rows && l<list.size()) {
	            	mat[i++][k++]= list.get(l++);
	            }
	        }
	        
	        return mat;
	        
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MatrixDiagonalSort s = new MatrixDiagonalSort();
		s.diagonalSort(new int[][] {{3,3,1,1},{2,2,1,2},{1,1,1,2}});
	}

}
