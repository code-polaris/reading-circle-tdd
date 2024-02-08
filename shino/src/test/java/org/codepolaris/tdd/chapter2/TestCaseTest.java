package org.codepolaris.tdd.chapter2;

import static org.assertj.core.api.Assertions.assertThat;

public class TestCaseTest extends TestCase {

  private static final String TEST_NAME = "testTemplateMethod";
  private static final String TEST_METHOD_NAME = "testMethod";
  private static final String TEST_BROKEN_METHOD_NAME = "testBrokenMethod";

  private TestResult result;

  /**
   * Java はUnit Test内でconstructorを呼び出すのが困難な為、
   * default constructorを作成の上、必要な値を親クラスであるTestCaseに渡す
   */
  public TestCaseTest() {
    super(TEST_NAME);
  }

  public TestCaseTest(String testName) {
    super(testName);
  }

  @Override
  public void setUp() {
    super.setUp();
    result = new TestResult();
  }

  void testTemplateMethod() {
    var test = new WasRun(TEST_METHOD_NAME);
    test.run(result);
    assertThat(test.getStoredLog()).isEqualTo("setUp testMethod tearDown ");
  }

  void testResult() {
    var test = new WasRun(TEST_METHOD_NAME);
    test.run(result);
    assertThat(result.summary()).isEqualTo("1 run, 0 failed");
  }

  void testFailedResult() {
    var test = new WasRun(TEST_BROKEN_METHOD_NAME);
    test.run(result);
    assertThat(result.summary()).isEqualTo("1 run, 1 failed");
  }

  void testFailedResultFormatting() {
    result.testStarted();
    result.testFailed();
    assertThat(result.summary()).isEqualTo("1 run, 1 failed");
  }

  void testSuite() {
    var suite = new TestSuite();
    suite.add(new WasRun(TEST_METHOD_NAME));
    suite.add(new WasRun(TEST_BROKEN_METHOD_NAME));
    suite.run(result);
    assertThat(result.summary()).isEqualTo("2 run, 1 failed");
  }
}
