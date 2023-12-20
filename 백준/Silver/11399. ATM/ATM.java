import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();
        String[] s = br.readLine().split(" ");
        List<Integer> arr = new ArrayList<Integer>();
        for (String ss : s)
            arr.add(Integer.parseInt(ss));
        // arr = arr.stream().sorted().toList();
        // arr = Arrays.sort(arr.stream().toList());
        arr.sort(new Comparator<Integer>(){
            @Override
            public int compare(Integer a, Integer b){
                return a>b?1:-1;
            }
        });
        // System.out.println(arr.toString());
        int ans = 0;
        for (int i = 0; i < arr.size(); i++) {
            int tmp = 0;
            // arr.subList(i,arr.size()).stream().map((Integer n)->{
            // System.out.println(n);
            // });
            for (int t : arr.subList(0, i + 1))
                tmp += t;
            ans += tmp;
        }
        System.out.println(ans);
    }
}