import java.io.*;
import java.util.*;

public class Main {
    public static int[][] arr;
    public static boolean[][] graph;
    public static boolean[] vis;
    public static int N, M;
    public static int[] dx = new int[]{-1,0,1,0};
    public static int[] dy = new int[]{0,-1,0,1};


    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = br.readLine();
        Set<String> strs = new HashSet<>();

        for (int i=0;i<s.length();i++){
            for (int j=i;j<s.length();j++){
                strs.add(s.substring(i,j+1));
            }
        }
        System.out.println(strs.size());
    }
}

