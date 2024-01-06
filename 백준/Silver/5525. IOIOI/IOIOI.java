import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        String S = br.readLine();
        int w = N*2+1;
        int ans=0;
        int cntN=0;

        int i=0;
        while (i+2<M){
            if (
                S.charAt(i)=='I' &&
                S.charAt(i+1)=='O' &&
                S.charAt(i+2)=='I'
            ){
                cntN++;
                i+=2;
                if (cntN==N){
                    ans++;
                    cntN--;
                }
            } 
            else {
                i++;
                cntN=0;
            }
            
        }
        System.out.println(ans);
    }
}
