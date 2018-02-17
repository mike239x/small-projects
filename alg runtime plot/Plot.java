import java.io.File;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Random;

//! the code requires R and java 8 !

public class Plot {

	//main 2 functions to be used here are 
	//report(f,name,random,checkCorectness) for saving data
	//and plot(name,logScale) for drawing the plot
	public static void main(String[] args) {
		reportAndPlot(Plot::quickSort, "quick", new Random(), false);
		//reportAndPlot(Plot::bubbleSort, "bubble", new Random(239), true);
	}

//--------------------------------------------------------

	private static final String ext = ".sort";
	
	public static void reportAndPlot(Sortfunction f, String name, Random r, boolean logScale) {
		report(f,name,r,false);//not checking correctness here
		plot(name,logScale);
	}
	
	//draws a plot of the given data and saves it to $name.jpeg 
	//R and in particular Rscript is required
	public static void plot(String name, boolean logScale) {
		try {
			PrintWriter out = new PrintWriter(new File(name + ".R"));
			String[] code = {
					"data <- read.table('"+name+ext+"',sep='',header=F)",
					"n <- data[[1]]",
					"time <- data[[2]]",
					"jpeg('"+name+".jpeg')", //requires jpeg driver
					"par(pch = '*')",
					logScale?"plot (log(time)~log(n))":"plot (time~n)",
					"grid(nx = NULL, ny = NULL, col = 'lightgray', lty = 'dotted')",
					"dev.off()"
			};
			for (String line : code) {
				out.println(line);
			}
			out.close();
			Process p = Runtime.getRuntime().exec("Rscript "+name+".R");
			p.waitFor();
		} catch (Exception e) {
			System.out.println("We encountered an error :(");
			e.printStackTrace();
			System.exit(0);
		}
	}
	//function to collect information on speed of the sorting algorithm
	public static void report(Sortfunction f, String name, Random r, boolean checkCorrectness) {
		try {
			PrintWriter out = new PrintWriter(new File(name + ext));
			//TODO: add a number generator for the size in function header
			for (int n = 10; n < 5001; n+=10) {
				out.print(n);
				out.print(" ");
				out.println(time(f, n, r, checkCorrectness));
			}
			out.close();
		} catch (Exception e) {
			System.out.println("We encountered an error!");
			e.printStackTrace();
			System.exit(0);
		}
	}

	//checks if the given array is properly sorted.
	public static boolean isSorted(int[] arr) {
		for (int i = 1; i < arr.length; i++) {
			if (arr[i] < arr[i-1]) return false;
		}
		return true;
	}
	/**
	 * measures time used by a sorting algorithm 
	 * @param f sorting function
	 * @param n size of array to be sorted
	 * @param r random number generator
	 * @param checkCorrectness flag if check of the result is required
	 * @return time used by sorting function in nanoseconds
	 */
	public static long time(Sortfunction f, int n, Random r, boolean checkCorrectness){
		int[] arr = new int[n];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Math.abs(r.nextInt());
		}
		long time = System.nanoTime();
		f.sort(arr);
		time = System.nanoTime() - time;
		if (checkCorrectness) {
			if (!isSorted(arr)) {
				System.out.println("Error with sorting argorithm detected!");
			}
		}
		return time;
	}	

//--------------------------------------------------------
	
	//java implementation of qSort
	public static void javaQSort(int[] arr) {
		Arrays.sort(arr);
	}
	//bubbleSort
	public static void bubbleSort(int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < i; j++) {
				if (arr[i] < arr[j]) {
					swap(arr, i, j);
				}
			}
		}
	}
	//qSort from the lecture
	public static void quickSort(int[] arr) {
		qSort(arr, 0, arr.length-1);
	}
	private static void qSort(int[ ] arr, int l, int r) {
		// arr[l . . . r]: zu sortierendes Feld
		if (l < r) {
			int p = arr[r]; // Pivot
			int i = l - 1; int j = r;
			do { // spalte Elemente in a[l, . . . , r − 1] nach Pivot p
				do i++; while (arr[i] < p);
				do j--; while (j >= l && arr[j] > p);
				if (i < j) swap(arr, i, j);
			} while (i < j);
			swap (arr, i, r); // Pivot an richtige Stelle
			qSort(arr, l, i - 1);
			qSort(arr, i + 1, r);
		}
	}
	//swap method, used all the time
	private static void swap (int[] arr, int i, int j) {
		int tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}
}
//--------------------------------------------------------
@FunctionalInterface
interface Sortfunction {
	void sort(int[] arr);
}
