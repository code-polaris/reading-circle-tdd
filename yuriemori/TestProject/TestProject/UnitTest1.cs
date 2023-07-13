namespace TestProject;
using Project;

[TestClass]
public class UnitTest1
{
    //　掛け算のテスト        
    [TestMethod]
    public void TestMethod1()
    {
            // Arrange
            var dollar = new Dollar(5);
            // Act
            dollar.Times(2);

            // Assert
            Assert.AreEqual(10, dollar.Amount);        
    }
}