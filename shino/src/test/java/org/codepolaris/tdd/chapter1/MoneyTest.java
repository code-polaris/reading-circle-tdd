package org.codepolaris.tdd.chapter1;

import org.codepolaris.tdd.chapter1.Bank;
import org.codepolaris.tdd.chapter1.Expression;
import org.codepolaris.tdd.chapter1.Money;
import org.codepolaris.tdd.chapter1.Sum;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.codepolaris.tdd.chapter1.utils.Currency.CHF;
import static org.codepolaris.tdd.chapter1.utils.Currency.USD;

class MoneyTest {

  private static final Money FIVE_DOLLAR = Money.dollar(5);
  private static final Money TEN_FRANC = Money.franc(10);
  public static final Money ONE_DOLLAR = Money.dollar(1);
  private Bank bank;

  @BeforeEach
  public void setUp() {
    bank = new Bank();
    bank.addRate(CHF, USD, 2);
  }

  @Test
  void testMultiplication() {
    Money five = FIVE_DOLLAR;
    assertThat(five.times(2)).isEqualTo(Money.dollar(10));
    assertThat(five.times(3)).isEqualTo(Money.dollar(15));
  }

  @Test
  void testEquality() {
    assertThat(Money.dollar(5).equals(Money.dollar(5))).isTrue();
    assertThat(Money.dollar(5).equals(Money.dollar(6))).isFalse();
    assertThat(Money.franc(5).equals(Money.dollar(5))).isFalse();
  }

  @Test
  void testCurrency() {
    assertThat(Money.dollar(1).currency()).isEqualTo(USD);
    assertThat(Money.franc(1).currency()).isEqualTo(CHF);
  }

  @Test
  void testSimpleAddition() {
    Expression sum = FIVE_DOLLAR.plus(FIVE_DOLLAR);
    Money reduced = bank.reduce(sum, USD);
    assertThat(reduced).isEqualTo(Money.dollar(10));
  }

  @Test
  void testPlusReturnsSum() {
    Expression result = FIVE_DOLLAR.plus(FIVE_DOLLAR);
    Sum sum = (Sum) result;
    assertThat(sum.augend).isEqualTo(FIVE_DOLLAR);
    assertThat(sum.addend).isEqualTo(FIVE_DOLLAR);
  }

  @Test
  void testReduceSum() {
    Expression sum = new Sum(Money.dollar(3), Money.dollar(4));
    Money result = bank.reduce(sum, USD);
    assertThat(result).isEqualTo(Money.dollar(7));
  }

  @Test
  void testReduceMoney() {
    Money result = bank.reduce(ONE_DOLLAR, USD);
    assertThat(result).isEqualTo(ONE_DOLLAR);
  }

  @Test
  void testReduceMoneyDifferentCurrency() {
    Money result = bank.reduce(Money.franc(2), USD);
    assertThat(result).isEqualTo(ONE_DOLLAR);
  }

  @Test
  void testIdentityRate() {
    assertThat(new Bank().rate(USD, USD)).isEqualTo(1);
  }

  @Test
  void testMixedAddition() {
    Money result = bank.reduce(FIVE_DOLLAR.plus(TEN_FRANC), USD);
    assertThat(result).isEqualTo(Money.dollar(10));
  }

  @Test
  void testSumPlusMoney() {
    Expression sum = new Sum(FIVE_DOLLAR, TEN_FRANC).plus(FIVE_DOLLAR);
    Money result = bank.reduce(sum, USD);
    assertThat(result).isEqualTo(Money.dollar(15));
  }

  @Test
  void testSumTimes() {
    Expression sum = new Sum(FIVE_DOLLAR, TEN_FRANC).times(2);
    Money result = bank.reduce(sum, USD);
    assertThat(result).isEqualTo(Money.dollar(20));
  }
}
