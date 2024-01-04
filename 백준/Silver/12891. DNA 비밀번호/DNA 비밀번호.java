import java.io.*;
import java.util.*;

public class Main {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        String str = br.readLine();
        st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        String ACGT = "ACGT";
        int[] arr = new int[4];
        for (int i=0;i<P;i++)
            arr[ACGT.indexOf(str.charAt(i))]++;

        int cnt=0;
        if (!(arr[0]<A || arr[1]<C || arr[2]<G || arr[3]<T))
            cnt++;

        for (int l=1;l+P<=S;l++){
            int r = l+P-1;
            arr[ACGT.indexOf(str.charAt(l-1))]--;
            // if (ACGT.indexOf(str.charAt(r))==-1) continue;
            arr[ACGT.indexOf(str.charAt(r))]++;
            // System.out.println(Arrays.toString(arr));
            if (arr[0]<A) continue;
            if (arr[1]<C) continue;
            if (arr[2]<G) continue;
            if (arr[3]<T) continue;
            cnt++;
        }
        System.out.println(cnt);

    }
}
