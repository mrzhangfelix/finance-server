package com.felix.finance.entity;

import com.alibaba.fastjson.JSONObject;

import java.util.List;

public class FundJson{
    private String gztime;
    private String todayIncameSum;
    private List<FundInfo> fundlist;

    public FundJson(String gztime, String todayIncameSum, List<FundInfo> fundlist) {
        this.gztime = gztime;
        this.todayIncameSum = todayIncameSum;
        this.fundlist = fundlist;
    }

    public String getGztime() {
        return gztime;
    }

    public FundJson setGztime(String gztime) {
        this.gztime = gztime;
        return this;
    }

    public String getTodayIncameSum() {
        return todayIncameSum;
    }

    public FundJson setTodayIncameSum(String todayIncameSum) {
        this.todayIncameSum = todayIncameSum;
        return this;
    }

    public List<FundInfo> getFundlist() {
        return fundlist;
    }

    public FundJson setFundlist(List<FundInfo> fundlist) {
        this.fundlist = fundlist;
        return this;
    }
}
