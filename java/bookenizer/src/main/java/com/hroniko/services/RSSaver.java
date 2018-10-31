package com.hroniko.services;

import java.math.BigInteger;
import java.util.List;

public class RSSaver {

//    private static List<BigInteger> idAuthor

    private static RSSaver ourInstance = new RSSaver();

    public static RSSaver getInstance() {
        return ourInstance;
    }

    private RSSaver() {
    }
}
