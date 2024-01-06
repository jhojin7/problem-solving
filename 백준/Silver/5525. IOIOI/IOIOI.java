import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        String S = br.readLine();
        int w = N*2+1;
        boolean isIOI = true;
        int ans=0;

        for (int i=0;i+w<=M;i++){
            // System.out.println(i);
            if (S.charAt(i)=='O') continue;
            // System.out.println(S.substring(i,i+w));
            isIOI = true;
            for (int j=i+1;j<i+w;j++){
                if (S.charAt(j-1)==S.charAt(j)) {
                    isIOI=false;
                    break;
                }
            }
            if (isIOI) ans++;
        }
        System.out.println(ans);
    }
}
