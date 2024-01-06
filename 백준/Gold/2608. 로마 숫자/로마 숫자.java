import java.io.*;
import java.util.*;

public class Main {
    public static int calc(String roman) {
        int n = 0;

        if (roman.contains("CM")) {
            roman = roman.replace("CM", "");
            n += 900;
        }
        if (roman.contains("CD")) {
            roman = roman.replace("CD", "");
            n += 400;
        }
        if (roman.contains("XC")) {
            roman = roman.replace("XC", "");
            n += 90;
        }
        if (roman.contains("XL")) {
            roman = roman.replace("XL", "");
            n += 40;
        }
        if (roman.contains("IX")) {
            roman = roman.replace("IX", "");
            n += 9;
        }
        if (roman.contains("IV")) {
            roman = roman.replace("IV", "");
            n += 4;
        }

        for (char c : roman.toCharArray()) {
            if (c == 'I')
                n += 1;
            else if (c == 'V')
                n += 5;
            else if (c == 'X')
                n += 10;
            else if (c == 'L')
                n += 50;
            else if (c == 'C')
                n += 100;
            else if (c == 'D')
                n += 500;
            else if (c == 'M')
                n += 1000;
        }
        return n;
    }

    public static String roman(int n) {
        String roman = "";
        boolean v, l, d, iv, xl;
        v = l = d = iv = xl = false;

        while (true) {
            // if (roman.contains("III")) continue;
            // else if (roman.contains("XXX")) continue;
            // else if (roman.contains("CCC")) continue;
            // if (roman.contains("MMM")) continue;
            if (n >= 1000) {
                roman += "M";
                n -= 1000;
            } else if (n >= 900) {
                roman += "CM";
                n -= 900;
            } else if (n >= 500 && !d) {
                roman += "D";
                n -= 500;
                d = true;
            } else if (n >= 400 && !d) {
                roman += "CD";
                n -= 400;
                d = true;
            } else if (n >= 100) {
                roman += "C";
                n -= 100;
            } else if (n >= 90) {
                roman += "XC";
                n -= 90;
            } else if (n >= 50 && !l) {
                roman += "L";
                n -= 50;
                l = true;
            } else if (n >= 40 && !l) {
                roman += "XL";
                n -= 40;
                l = true;
            } else if (n >= 10) {
                roman += "X";
                n -= 10;
            } else if (n >= 9 && !iv) {
                roman += "IX";
                n -= 9;
                iv = true;
            } else if (n >= 5 && !v) {
                roman += "V";
                n -= 5;
                v = true;
            } else if (n >= 4 && !iv && !v) {
                roman += "IV";
                n -= 4;
                v = true;
                iv = true;
            } else if (n >= 1) {
                roman += "I";
                n -= 1;
            } else
                break;
        }
        return roman;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String roman1 = br.readLine();
        String roman2 = br.readLine();

        int n1 = calc(roman1);
        int n2 = calc(roman2);
        int n3 = n1 + n2;
        System.out.println(n3);
        System.out.println(roman(n3));
    }
}
