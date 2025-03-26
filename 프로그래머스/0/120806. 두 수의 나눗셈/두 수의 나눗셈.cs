using System;

public class Solution {
    public int solution(int num1, int num2) {
        float div_num = (float)num1 / num2;
        return (int)(div_num * 1000);
    }
}