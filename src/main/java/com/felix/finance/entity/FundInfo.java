package com.felix.finance.entity;

public class FundInfo {
    private String add;
    private String zhangfu;
    private String yingli;
    private String amountChange;
    private String fundcode;
    private String fundamount;
    private String buyTime;
    private String fundName;
    private String zeroInterestRate;

    public FundInfo(String add, String zhangfu, String yingli, String amountChange, String fundcode, String fundamount, String buyTime, String fundName, String zeroInterestRate) {
        this.add = add;
        this.zhangfu = zhangfu;
        this.yingli = yingli;
        this.amountChange = amountChange;
        this.fundcode = fundcode;
        this.fundamount = fundamount;
        this.buyTime = buyTime;
        this.fundName = fundName;
        this.zeroInterestRate = zeroInterestRate;
    }

    public String getAdd() {
        return add;
    }

    public FundInfo setAdd(String add) {
        this.add = add;
        return this;
    }

    public String getZhangfu() {
        return zhangfu;
    }

    public FundInfo setZhangfu(String zhangfu) {
        this.zhangfu = zhangfu;
        return this;
    }

    public String getYingli() {
        return yingli;
    }

    public FundInfo setYingli(String yingli) {
        this.yingli = yingli;
        return this;
    }

    public String getAmountChange() {
        return amountChange;
    }

    public FundInfo setAmountChange(String amountChange) {
        this.amountChange = amountChange;
        return this;
    }

    public String getFundcode() {
        return fundcode;
    }

    public FundInfo setFundcode(String fundcode) {
        this.fundcode = fundcode;
        return this;
    }

    public String getFundamount() {
        return fundamount;
    }

    public FundInfo setFundamount(String fundamount) {
        this.fundamount = fundamount;
        return this;
    }

    public String getBuyTime() {
        return buyTime;
    }

    public FundInfo setBuyTime(String buyTime) {
        this.buyTime = buyTime;
        return this;
    }

    public String getFundName() {
        return fundName;
    }

    public FundInfo setFundName(String fundName) {
        this.fundName = fundName;
        return this;
    }

    public String getZeroInterestRate() {
        return zeroInterestRate;
    }

    public FundInfo setZeroInterestRate(String zeroInterestRate) {
        this.zeroInterestRate = zeroInterestRate;
        return this;
    }
}
