import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        if (N == 1) {
            System.out.println(arr[0]);
            return;
        }
        int[] dp = new int[N];
        dp[0] = arr[0];
        dp[1] = arr[0] + arr[1];
        if (N==2){
            System.out.println(dp[1]);
            return;
        }
        dp[2] = Math.max(arr[0], arr[1])+arr[2];
        for (int i = 3; i < N; i++) {
            dp[i] =arr[i] + Math.max(
                dp[i-2], dp[i-3]+arr[i-1]);
        }
        System.out.println(dp[N - 1]);
    }
}