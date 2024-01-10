import java.io.*;
import java.util.*;

public class Main {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer st = new StringTokenizer(br.readLine());
        String A = br.readLine();
        String B = br.readLine();
        int N = A.length()*2;
        int[] arr = new int[N];
        int[] alpha = new int[]{3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1};
        for (int i=0;i<A.length();i++)
            arr[2*i] = alpha[A.charAt(i)-'A'];
        for (int i=0;i<B.length();i++)
            arr[2*i+1] = alpha[B.charAt(i)-'A'];
        while (N>2){
            int[] tmp = new int[N-1];
            for (int i=0;i<N-1;i++){
                tmp[i] = (arr[i]+arr[i+1])%10;
            }
            arr = tmp;
            N-=1;
        }
        System.out.println(arr[0]+""+arr[1]);
    }
}