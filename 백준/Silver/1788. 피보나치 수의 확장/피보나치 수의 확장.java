import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int mod = (int)Math.pow(10,9);
        Map<Integer,Integer> fib = new HashMap<>();
        fib.put(2,1);
        fib.put(1,1);
        fib.put(0,0);
        fib.put(-1,1);
        fib.put(-2,-1);
        // f(0) = f(-1) + f(-2) === f(-2) = f(0) - f(-1)
        for (int i=-3;i>=-1000000;i--){
            fib.put(i,(fib.get(i+2)-fib.get(i+1))%mod);
            // System.out.println(i+" "+fib.get(i));
            fib.put(-i,(fib.get(-i-1)+fib.get(-i-2))%mod);
            // System.out.println(-i+" "+fib.get(-i));
        }

        int N = Integer.parseInt(br.readLine());
        int ans = fib.get(N);
        if (ans>0) System.out.println(1);
        else if (ans==0) System.out.println(0);
        else System.out.println(-1);
        System.out.println(Math.abs(ans%mod));


    }
}
