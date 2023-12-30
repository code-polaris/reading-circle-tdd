package org.codepolaris.tdd.chapter2;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class TestCaseTest {

  private static final String TEST_METHOD_NAME = "testMethod";

  private WasRun test;

  @BeforeEach
  public void setUp() {
    this.test = new WasRun(TEST_METHOD_NAME);
  }

  void testSetup() {
    this.test.run();
    assertThat(test.isSetUp()).isTrue();
  }

  @Test
  void testRunning() {
    this.test.run();
    assertThat(test.isRan()).isTrue();
  }
}
