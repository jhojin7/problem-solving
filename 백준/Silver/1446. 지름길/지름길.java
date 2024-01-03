import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][3];
        for (int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            arr[i] = new int[]{a,b,c};
        }
        Arrays.sort(arr, Comparator
                            .comparing((int[] x)->x[0])
                            .thenComparing((int[] x)->x[1])
                            .thenComparing((int[] x)->x[2])
                            );

        int[] dp = new int[10001];
        for (int i=0;i<10001;i++)dp[i] = i;

        for (int i=0;i<10001;i++){
            // System.out.println(Arrays.toString(arr[i]));
            for (int j=0;j<N;j++){
                if (arr[j][0] == i)
                    dp[arr[j][1]] = Math.min(
                        // dp[i]+dp[arr[j][1]],
                        dp[arr[j][1]],
                        Math.min(
                            dp[i]+arr[j][2],
                            dp[i]+(arr[j][1]-arr[j][0])
                        )
                    );
            }
            for (int j=i+1;j<10001;j++){
                dp[j] = Math.min(dp[j],dp[j-1]+1);
            }
        }

        System.out.println(dp[D]);
        // System.out.println(Arrays.toString(dp));
    }
}
