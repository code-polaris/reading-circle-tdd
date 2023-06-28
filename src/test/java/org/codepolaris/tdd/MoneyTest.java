package org.codepolaris.tdd;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class MoneyTest {

  @Test
  void testMultiplication() {
    Dollar five = new Dollar(5);
    Dollar product = five.times(2);
    assertThat(product.amount).isEqualTo(10);
    product = five.times(3);
    assertThat(product.amount).isEqualTo(15);
  }
}
