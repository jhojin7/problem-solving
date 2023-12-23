import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(br.readLine());
        s = s + h * 3600 + m * 60 + d;
        // System.out.println(s);

        h = s / 3600 % 24;
        m = s % 3600 / 60;
        s = s % 3600 % 60;
        System.out.println(h + " " + m + " " + s);
    }
}