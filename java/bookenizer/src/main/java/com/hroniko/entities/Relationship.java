package com.hroniko.entities;

import java.math.BigInteger;
import java.util.List;

public class Relationship extends Base{

    private List<Author> authorList;
    private  List<Book> bookList;

    public Relationship() {
        super();
    }

    public Relationship(List<Author> authorList, List<Book> bookList) {
        super();
        this.authorList = authorList;
        this.bookList = bookList;
    }
}
