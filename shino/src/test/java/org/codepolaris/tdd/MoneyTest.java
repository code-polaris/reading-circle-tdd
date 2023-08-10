package org.codepolaris.tdd;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class MoneyTest {

  @Test
  void testMultiplication() {
    Dollar five = new Dollar(5);
    assertThat(five.times(2)).isEqualTo(new Dollar(10));
    assertThat(five.times(3)).isEqualTo(new Dollar(15));
  }

  @Test
  void testEquality() {
    assertThat(new Dollar(5).equals(new Dollar(5))).isTrue();
    assertThat(new Dollar(5).equals(new Dollar(6))).isFalse();
    assertThat(new Franc(5).equals(new Franc(5))).isTrue();
    assertThat(new Franc(5).equals(new Franc(6))).isFalse();
  }

  @Test
  void testFrancMultiplication() {
    Franc five = new Franc(5);
    assertThat(five.times(2)).isEqualTo(new Franc(10));
    assertThat(five.times(3)).isEqualTo(new Franc(15));
  }
}
