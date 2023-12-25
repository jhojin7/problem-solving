import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int vis = 1;
        if (N == 1 || M == 1) {
            System.out.println(1);
            return;
        } else if (N == 2) {
            if (M == 2)
                System.out.println(1);
            else if (M == 3)
                System.out.println(2);
            else if (M == 4)
                System.out.println(2);
            else if (M == 5)
                System.out.println(3);
            else if (M == 6)
                System.out.println(3);
            else
                System.out.println(4);
        } else if (N == 3) {
            if (M == 2)
                System.out.println(2);
            else if (M == 3)
                System.out.println(3);
            else if (M < 7)
                System.out.println(4);
            else
                System.out.println(calc(N, M - 7, vis + 4));
        } else {
            // ..2.4.67
            if (M == 2)
                System.out.println(2);
            else if (M == 3)
                System.out.println(3);
            else if (M < 7)
                System.out.println(4);
            else
                System.out.println(calc(N, M - 7, vis + 4));
        }

    }

    static int calc(int N, int M, int vis) {
        return vis + M;
    }
}