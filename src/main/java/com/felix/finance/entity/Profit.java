package com.felix.finance.entity;

public class Profit {
    private String quantity;
    private String time;

    public String getQuantity() {
        return quantity;
    }

    public Profit setQuantity(String quantity) {
        this.quantity = quantity;
        return this;
    }

    public String getTime() {
        return time;
    }

    public Profit setTime(String time) {
        this.time = time;
        return this;
    }

    public Profit(String quantity, String time) {
        this.quantity = quantity;
        this.time = time;
    }
}
