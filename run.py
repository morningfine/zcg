import os
import pytest

pytest.main()
#pytest.main(['--alluredir=results/allure_reports','--count=3'])
#pytest.main(["-m","login","--alluredir=Outputs/allure_reports"])

#os.system('allure serve results/allure_reports')