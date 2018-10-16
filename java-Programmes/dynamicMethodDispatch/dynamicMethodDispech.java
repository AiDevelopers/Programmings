package com.company;

/*Dynamic mathod dispatch*/
public class dynamicMethodDispech {

    public static void main(String args[]) {


        A1 bj = new A1();
        B1 bj1 = new B1();

        A1 bj2;
        bj2 = bj;
        bj2.show();
    }
}