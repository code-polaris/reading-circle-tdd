package org.codepolaris.tdd.chapter2;

import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;

@Slf4j
class SuiteTest {

  @Test
  void testAll() {
    var result = new TestResult();
    var suite = new TestSuite();
    suite.add(new TestCaseTest("testTemplateMethod"));
    suite.add(new TestCaseTest("testResult"));
    suite.add(new TestCaseTest("testFailedResult"));
    suite.add(new TestCaseTest("testFailedResultFormatting"));
    suite.add(new TestCaseTest("testSuite"));

    suite.run(result);
    log.info(result.summary());
  }
}
