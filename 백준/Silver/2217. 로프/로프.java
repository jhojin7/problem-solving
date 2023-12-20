import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++)
            arr[i] = Integer.parseInt(br.readLine());
        Arrays.sort(arr);
        int ans = 0;
        for (int i = N - 1; i >= 0; i--) {
            // System.out.println(N-i);
            // System.out.println(arr[i]);
            ans = Math.max(ans, (N - i) * arr[i]);
        }
        System.out.println(ans);
    }
}