package com.company;

class B extends A{

    int z;
    public void f1()
    {
        super.f1();
    }
    public void f2(){
        int z;
        z=2;
        this.z=3;/*z access only subclass instances according to this keyword */
        /*accoring to super keyword z access to super class instancess*/
        System.out.print("class B " + super.z);

    }
}

