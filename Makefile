.PHONY: run_tests


lint_tests:
	pylint tests/tests/test_demo.py


run_tests:
	poetry run pytest tests/test_demo.py -n2 -v -s --html=./test_reports/debugbear.html --self-contained-html --capture sys -rP -rF
