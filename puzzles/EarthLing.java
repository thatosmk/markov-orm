import java.util.*;
import java.util.concurrent.RecursiveAction;
import java.util.concurrent.ForkJoinPool;
import java.io.*;

public class EarthLing extends RecursiveAction
{

		// variables
		ArrayList<Double> words;
		private static final int[]  digits = new int[]{3,7,4,5,6,1,0,8,9,2};
		private static final char[] letters = new char[]{'S','R','W','A','H','N','O', 'E', 'T', 'U'};
		public static String word;
		public static int start;
		public static int end;

		public EarthLing(int start, int end)
		{
		}

		public void form_words()
		{
			// iterate the entire array and find a combination of the digits
			// that do form any of the words in the shared variable	
			for(int i=start; i<end; i++)
			{
				System.out.println("Letters :"+letters[digits[i]]);	
			}
		}
		public void compute()
		{
			if((end-start) <= 4)
			{
				// run the form words method
					for(int i=start; i<=end; i++)
					{
						System.out.println("Letters :"+letters[digits[i]]+" start: "+start+" , end: "+end);	
					}
				System.out.println("Done.");	
			}
			else
			{
				// divide and conquer
				int mid = (end - start)/2;
				System.out.println("mid is: "+mid);
				EarthLing left  = new EarthLing(start, mid);
				EarthLing right = new EarthLing(mid, end);


				// spawn threads 
				right.fork();
				left.compute();
				right.join();
			}
		
		}


		public static void main(String[] args)
		{

			try
			{
			 	// instantiate the fjp
			    EarthLing one = new EarthLing(0,10);	
				ForkJoinPool fjpool = new ForkJoinPool();		

				// run the threads
				fjpool.invoke(one);

			}catch(Exception ex){ex.printStackTrace();}
		}
}
