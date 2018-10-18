package com.company;

import java.util.Scanner;

public class customexcetion {
    public static void main(String args[]) throws userexception {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        if(input!=12) {
            throw new userexception("U R not eligible for take admission");
        }else {
            System.out.print("Welcome");
        }
    }
}
