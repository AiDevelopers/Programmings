package com.company;

/*Dynamic mathod dispatch*/
public class dynamicMethodDispech {

    public static void main(String args[]) {


        A1 bj = new A1();/*bj object of class A1*/
        B1 bj1 = new B1();/*bj1 object of class B1*/

        A1 bj2;/*bj2 refrence of class A1*/
        bj2 = bj;
        bj2.show();
       
        B1 bj3;/*bj3 refrence of class B1*/
        bj3 = bj1;
        bj3.show();


    }
}