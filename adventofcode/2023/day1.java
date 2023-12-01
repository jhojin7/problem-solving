import java.io.File;
import java.util.Scanner;

public class AdventOfCode {
    public static void main(String[] args) {
        Part2();
    }
    public static void Part2() {
        String my_input = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
                """;
        String[] arr = my_input.split("\n");
        for(String s:arr){
            Integer[] ans;
            String[] nums = {"one","two","three"};
            for(String num:nums){
                if(s.contains(num)){
                    s = s.replaceFirst(num,"0");
                }
            }
            System.out.println(s);
        }
    }
    public static void Part1(String[] args) {
        String my_input = """
                1abc2
                pqr3stu8vwx
                a1b2c3d4e5f
                treb7uchet
                """;
        String[] arr = my_input.split("\n");
        Integer ans = 0;
        for(String s:arr){
            int a=0;
            int b=0;
            for(int i=0;i<s.length();i++){
                char c = s.charAt(i);
                try{
                    Integer x = Integer.parseInt(String.valueOf(c));
                    a = x;
                    break;
                } catch(Exception e) {
                    continue;
                }
            }
            for(int i=s.length()-1;i>=0;i--){
                char c = s.charAt(i);
                try{
                    Integer x = Integer.parseInt(String.valueOf(c));
                    b = x;
                    break;
                } catch(Exception e) {
                    continue;
                }
            }
            Integer tmp = a*10+b;
            System.out.println(tmp);
            ans = ans+tmp;
        }
        System.out.println(ans);
    }
}
