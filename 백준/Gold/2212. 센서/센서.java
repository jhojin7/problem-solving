import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        Integer[] arr2 = new Integer[N - 1];
        for (int i = 0; i < N - 1; i++) {
            arr2[i] = arr[i + 1] - arr[i];
        }
        Arrays.sort(arr2,Comparator.reverseOrder());
        int ans = 0;
        for (int i=K-1;i<N-1;i++)
            ans += arr2[i];
        System.out.println(ans);
    }
}