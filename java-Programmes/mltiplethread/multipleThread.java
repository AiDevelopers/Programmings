package com.company;

public class multipleThread {
    public static void main(String args[]){
        A a = new A();
        Thread thread = new Thread(a);
        B b = new B();
        thread.start();
        b.start();
    }
}
