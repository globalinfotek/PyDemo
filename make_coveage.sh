rm -rf .coverage
coverage run --parallel-mode --omit "/usr/*" TestShoppingCart.py
coverage combine
coverage report
coverage xml

sonar.python.coverage.reportPath=coverage.xml
