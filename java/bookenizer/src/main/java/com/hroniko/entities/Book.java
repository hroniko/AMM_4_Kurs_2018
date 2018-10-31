package com.hroniko.entities;

import java.math.BigInteger;
import java.util.Date;
import java.util.List;

public class Book extends Base {
    private String title;
    private String introduction;
    private Date year;
    private Long pageCount;
    private List<String> keyWorlds;

    public Book() {
        super();
    }

    public Book(String title, String introduction, Date year, Long pageCount, List<String> keyWorlds) {
        super();
        this.title = title;
        this.introduction = introduction;
        this.year = year;
        this.pageCount = pageCount;
        this.keyWorlds = keyWorlds;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getIntroduction() {
        return introduction;
    }

    public void setIntroduction(String introduction) {
        this.introduction = introduction;
    }

    public Date getYear() {
        return year;
    }

    public void setYear(Date year) {
        this.year = year;
    }

    public Long getPageCount() {
        return pageCount;
    }

    public void setPageCount(Long pageCount) {
        this.pageCount = pageCount;
    }

    public List<String> getKeyWorlds() {
        return keyWorlds;
    }

    public void setKeyWorlds(List<String> keyWorlds) {
        this.keyWorlds = keyWorlds;
    }

    @Override
    public String toString() {
        return "Book{" +
                "title='" + title + '\'' +
                ", introduction='" + introduction + '\'' +
                ", year=" + year +
                ", pageCount=" + pageCount +
                ", keyWorlds=" + keyWorlds +
                '}';
    }
}
