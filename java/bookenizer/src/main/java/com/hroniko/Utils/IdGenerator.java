package com.hroniko.Utils;

import java.math.BigInteger;

public class IdGenerator {

    private static BigInteger currentId = BigInteger.ZERO;


    private static IdGenerator ourInstance = new IdGenerator();

    public static IdGenerator getInstance() {
        return ourInstance;
    }

    private IdGenerator() {
    }

    public static BigInteger generate(){
        currentId = currentId.and(BigInteger.ONE);
        return currentId;
    }


}
