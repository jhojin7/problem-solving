import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int[] A = new int[N];
            int[] B = new int[M];

            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < N; x++) {
                A[x] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < M; x++) {
                B[x] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(A);
            Arrays.sort(B);
            // for (int x:A) System.out.println(x);
            // for (int x:B) System.out.println(x);
            int cnt = 0;
            for (int a : A) {
                for (int b : B) {
                    if (a <= b)
                        break;
                    else
                        cnt += 1;
                }
            }
            System.out.println(cnt);
        }
    }
}
