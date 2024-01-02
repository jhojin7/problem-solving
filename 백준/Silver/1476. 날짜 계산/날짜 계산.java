import java.io.*;
import java.util.*;

public class Main {

    public static void main(String args[]) throws IOException {
        int E,S,M;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        E = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int e,s,m, ans;
        e=s=m=ans=0;
        while (e<16 || s<29 || m<20){
            // System.out.println(e+" "+s+" "+m);
            if (e==E && s==S && m==M) break;
            ans++;
            e++;
            s++;
            m++;
            if (e==16) e=1;
            if (s==29) s=1;
            if (m==20) m=1;
        }
        System.out.println(ans);
    }
}