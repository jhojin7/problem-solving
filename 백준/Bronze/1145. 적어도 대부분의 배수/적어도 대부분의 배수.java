import java.io.*;
import java.util.*;

public class Main {

    static int gcd (int a, int b){
        int m = Math.min(a, b);
        int M = Math.max(a, b);
        a = m; b = M;
        while (b!=0){
            int tmp = a;
            a = b;
            b = tmp%b;
        }
        return Math.abs(a);
    }

    static int lcm (int a, int b){
        return (int)(a*b/gcd(a,b));
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[5];
        for (int i=0;i<5;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        // System.out.println(Arrays.toString(arr));
        int ans = 100000000;
        for (int i=0;i<5;i++){
            for (int j=i+1;j<5;j++){
                for (int k=j+1;k<5;k++){
                    int a = arr[i];
                    int b = arr[j];
                    int c = arr[k];
                    ans = Math.min(ans,lcm(a,lcm(b,c)));
                }
            }
        }
        System.out.println(ans);
    }
}
