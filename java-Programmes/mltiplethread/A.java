package com.company;

class A implements Runnable {

    public void run() {
        int i;
        for(i=0;i<5;i++) {
            System.out.println("class A " + i);
        }
    }
}

