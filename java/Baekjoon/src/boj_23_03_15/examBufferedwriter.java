package boj_23_03_15;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class examBufferedwriter {
	public static void main(String[] args) throws IOException {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write("Hello Word\n");
		bw.write("Hello Word\n");
		bw.write("Hello Word\n");
		bw.flush();
		bw.write("11Hello Word\n");
		bw.flush();

		bw.write("22Hello Word\n");
		bw.flush();
		bw.close();
	}
}
