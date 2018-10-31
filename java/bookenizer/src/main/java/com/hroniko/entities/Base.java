package com.hroniko.entities;

import com.hroniko.Utils.IdGenerator;

import java.math.BigInteger;
import java.util.Objects;

public class Base {
    private BigInteger id;

    public Base() {
        this.id = IdGenerator.generate();
    }

    public BigInteger getId() {
        return id;
    }

    public void setId(BigInteger id) {
        this.id = id;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Base base = (Base) o;
        return Objects.equals(id, base.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    @Override
    public String toString() {
        return "Base{" +
                "id=" + id +
                '}';
    }
}
