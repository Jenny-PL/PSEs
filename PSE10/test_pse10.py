from pse10 import max_profit 

def test_no_profit_returns_0():
    # arrange
    stock_list = [7,6,4,3,1]
    
    # act 
    result = max_profit(stock_list)
    
    # assert
    assert result == 0

def test_stock_list_returns_max_profit():
    # arrange
    stock_list = [7,1,5,3,6,4]
    # act
    result = max_profit(stock_list)
    # assert
    assert result == 7
    