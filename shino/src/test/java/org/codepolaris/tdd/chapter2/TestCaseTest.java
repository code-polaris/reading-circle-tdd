package org.codepolaris.tdd.chapter2;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class TestCaseTest extends TestCase {

  private static final String TEST_NAME = "testTemplateMethod";
  private static final String TEST_METHOD_NAME = "testMethod";
  private static final String TEST_BROKEN_METHOD_NAME = "testBrokenMethod";

  /**
   * Java はUnit Test内でconstructorを呼び出すのが困難な為、
   * default constructorを作成の上、必要な値を親クラスであるTestCaseに渡す
   */
  public TestCaseTest() {
    super(TEST_NAME);
  }

  @Test
  void testTemplateMethod() {
    var test = new WasRun(TEST_METHOD_NAME);
    test.run();
    assertThat(test.getStoredLog()).isEqualTo("setUp testMethod tearDown ");
  }

  @Test
  void testResult() {
    var test = new WasRun(TEST_METHOD_NAME);
    var result = test.run();
    assertThat(result.summary()).isEqualTo("1 run, 0 failed");
  }

  @Test
  void testFailedResult() {
    var test = new WasRun(TEST_BROKEN_METHOD_NAME);
    var result = test.run();
//    assertThat(result.summary()).isEqualTo("1 run, 1 failed");
  }
}
