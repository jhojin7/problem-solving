import java.io.*;
import java.util.*;

public class Main {
    static int M,N,K;
    static int[][] box;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            String s = br.readLine();
            if (s.equals("#")) return;
            int tmp=0;
            for (char c:s.toCharArray()){
                if ("AEIOUaeiou".indexOf(c)!=-1)
                    tmp += 1;
            }
            System.out.println(tmp);
        }
    }
}