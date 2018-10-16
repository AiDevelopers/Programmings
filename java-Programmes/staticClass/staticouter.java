package com.company;

public class staticouter {
    static int s = 25;
    static class Sclass{
        int b=10;
        int  add1 = b + s;
        public void add(){

            System.out.print("static class value" + add1 );
        }
    }
}
