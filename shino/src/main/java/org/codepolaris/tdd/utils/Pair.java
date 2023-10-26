package org.codepolaris.tdd.utils;

import java.util.Objects;

public class Pair {

  private String from;
  private String to;

  public Pair(String from, String to) {
    this.from = from;
    this.to = to;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o instanceof Pair pair) {
      return from.equals(pair.from) && to.equals(pair.to);
    }
    return false;

  }

  // hashが0を返すのがどうしても許せないので、Defaultの実装をさせて貰った
  @Override
  public int hashCode() {
    return Objects.hash(from, to);
  }
}
