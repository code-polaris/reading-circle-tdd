package org.codepolaris.tdd.chapter2;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class TestCaseTest extends TestCase {

  private static final String TEST_NAME = "testTemplateMethod";
  private static final String TEST_METHOD_NAME = "testMethod";

  private final WasRun test;

  /**
   * Java はUnit Test内でconstructorを呼び出すのが困難な為、
   * default constructorを作成の上、必要な値を親クラスであるTestCaseに渡す
   */
  public TestCaseTest() {
    super(TEST_NAME);
    this.test = new WasRun(TEST_METHOD_NAME);
  }

  @Test
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
