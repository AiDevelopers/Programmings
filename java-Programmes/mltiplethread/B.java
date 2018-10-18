package com.company;

public class B extends Thread {
    public void run() {
        int i;
        for(i=0;i<5;i++) {
            System.out.println("class B " + i);
        }
    }
}
