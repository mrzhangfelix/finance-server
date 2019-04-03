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
//    单位净值
    private String dwjz;
//    持有数量
    private String holdShare;
//    持有金额
    private String amountNow;
//    估算值
    private String gusuanzhi;
//    7日买入金额
    private String buyamount7;
//    7日买入份额
    private String buyshare7;

    public FundInfo(String add, String zhangfu, String yingli, String amountChange, String fundcode, String fundamount, String buyTime, String fundName) {
        this.add = add;
        this.zhangfu = zhangfu;
        this.yingli = yingli;
        this.amountChange = amountChange;
        this.fundcode = fundcode;
        this.fundamount = fundamount;
        this.buyTime = buyTime;
        this.fundName = fundName;
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

}
