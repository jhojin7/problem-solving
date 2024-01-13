import java.io.*;
import java.util.*;

public class Main {
    public static int[][] arr;
    public static int N, M;
    public static int[] dx = new int[]{-1,0,1,0};
    public static int[] dy = new int[]{0,-1,0,1};

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i=0;i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int M = Integer.parseInt(br.readLine());
        for (int t=0;t<M;t++){
            String[] s = br.readLine().split(" ");
            int a = Integer.parseInt(s[0]);
            int b = Integer.parseInt(s[1])-1;
            if (a==1){
                for (int i=b;i<N;i+=b+1){
                    if (arr[i]==0) arr[i] = 1;
                    else arr[i] = 0;
                }

            } else {
                int i=0;
                while (arr[b-i]==arr[b+i]){
                    int n = arr[b-i];
                    if (n==0) n = 1;
                    else n=0;
                    arr[b-i] = n;
                    arr[b+i] = n;
                    i++;
                    if (!(0<=b-i && b+i<N)) break;
                }
            }

        }
        StringBuilder sb = new StringBuilder();
        for (int i=0;i<N;i++){
            sb.append(arr[i]).append(' ');
            if (i%20==19) sb.append('\n');
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }
}